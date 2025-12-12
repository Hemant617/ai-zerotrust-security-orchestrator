"""
Usage Limits and Rate Limiting for Freemium Model
"""

from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, Tuple, Optional
import redis
import json


class UsageLimiter:
    """
    Manage usage limits for different subscription tiers.
    """
    
    # Plan limits
    LIMITS = {
        'free': {
            'scans_per_day': 10,
            'scans_per_month': 100,
            'api_calls_per_day': 0,  # No API access
            'concurrent_scans': 1
        },
        'pro': {
            'scans_per_day': -1,  # Unlimited
            'scans_per_month': -1,  # Unlimited
            'api_calls_per_day': 1000,
            'concurrent_scans': 5
        },
        'enterprise': {
            'scans_per_day': -1,  # Unlimited
            'scans_per_month': -1,  # Unlimited
            'api_calls_per_day': -1,  # Unlimited
            'concurrent_scans': 20
        }
    }
    
    def __init__(self, redis_url: Optional[str] = None):
        """
        Initialize usage limiter.
        
        Args:
            redis_url: Redis connection URL (optional, uses in-memory if not provided)
        """
        self.use_redis = redis_url is not None
        
        if self.use_redis:
            self.redis_client = redis.from_url(redis_url)
        else:
            # In-memory storage (for development)
            self.usage_data = defaultdict(lambda: {
                'daily_scans': [],
                'monthly_scans': [],
                'api_calls': []
            })
    
    def check_limit(
        self, 
        user_id: str, 
        plan: str = 'free',
        action: str = 'scan'
    ) -> Tuple[bool, str]:
        """
        Check if user has exceeded their usage limit.
        
        Args:
            user_id: User identifier
            plan: User's subscription plan
            action: Type of action ('scan' or 'api_call')
            
        Returns:
            (allowed, message) tuple
        """
        if plan not in self.LIMITS:
            return False, f"Invalid plan: {plan}"
        
        limits = self.LIMITS[plan]
        
        if action == 'scan':
            return self._check_scan_limit(user_id, limits)
        elif action == 'api_call':
            return self._check_api_limit(user_id, limits)
        else:
            return False, f"Invalid action: {action}"
    
    def _check_scan_limit(self, user_id: str, limits: Dict) -> Tuple[bool, str]:
        """Check scan limits."""
        daily_limit = limits['scans_per_day']
        monthly_limit = limits['scans_per_month']
        
        # Unlimited
        if daily_limit == -1:
            return True, "OK"
        
        # Get usage
        daily_count = self._get_daily_count(user_id, 'scans')
        monthly_count = self._get_monthly_count(user_id, 'scans')
        
        # Check daily limit
        if daily_count >= daily_limit:
            return False, f"Daily limit reached ({daily_limit} scans/day). Upgrade to Pro for unlimited scans!"
        
        # Check monthly limit
        if monthly_limit != -1 and monthly_count >= monthly_limit:
            return False, f"Monthly limit reached ({monthly_limit} scans/month). Upgrade to continue!"
        
        return True, f"OK ({daily_count + 1}/{daily_limit} today)"
    
    def _check_api_limit(self, user_id: str, limits: Dict) -> Tuple[bool, str]:
        """Check API call limits."""
        daily_limit = limits['api_calls_per_day']
        
        # No API access
        if daily_limit == 0:
            return False, "API access not available on Free plan. Upgrade to Pro!"
        
        # Unlimited
        if daily_limit == -1:
            return True, "OK"
        
        # Get usage
        daily_count = self._get_daily_count(user_id, 'api_calls')
        
        # Check limit
        if daily_count >= daily_limit:
            return False, f"Daily API limit reached ({daily_limit} calls/day). Upgrade to Enterprise for unlimited!"
        
        return True, f"OK ({daily_count + 1}/{daily_limit} today)"
    
    def record_usage(self, user_id: str, action: str = 'scan'):
        """
        Record a usage event.
        
        Args:
            user_id: User identifier
            action: Type of action ('scan' or 'api_call')
        """
        timestamp = datetime.now()
        
        if self.use_redis:
            self._record_usage_redis(user_id, action, timestamp)
        else:
            self._record_usage_memory(user_id, action, timestamp)
    
    def _record_usage_redis(self, user_id: str, action: str, timestamp: datetime):
        """Record usage in Redis."""
        key = f"usage:{user_id}:{action}"
        
        # Add timestamp to sorted set
        self.redis_client.zadd(key, {timestamp.isoformat(): timestamp.timestamp()})
        
        # Set expiry (keep data for 31 days)
        self.redis_client.expire(key, 31 * 24 * 60 * 60)
    
    def _record_usage_memory(self, user_id: str, action: str, timestamp: datetime):
        """Record usage in memory."""
        if action == 'scan':
            self.usage_data[user_id]['daily_scans'].append(timestamp)
            self.usage_data[user_id]['monthly_scans'].append(timestamp)
        elif action == 'api_call':
            self.usage_data[user_id]['api_calls'].append(timestamp)
    
    def _get_daily_count(self, user_id: str, action: str) -> int:
        """Get count of actions today."""
        if self.use_redis:
            return self._get_daily_count_redis(user_id, action)
        else:
            return self._get_daily_count_memory(user_id, action)
    
    def _get_daily_count_redis(self, user_id: str, action: str) -> int:
        """Get daily count from Redis."""
        key = f"usage:{user_id}:{action}"
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        count = self.redis_client.zcount(
            key,
            today_start.timestamp(),
            datetime.now().timestamp()
        )
        
        return count
    
    def _get_daily_count_memory(self, user_id: str, action: str) -> int:
        """Get daily count from memory."""
        today = datetime.now().date()
        
        if action == 'scan':
            timestamps = self.usage_data[user_id]['daily_scans']
        else:
            timestamps = self.usage_data[user_id]['api_calls']
        
        # Clean old entries
        timestamps[:] = [ts for ts in timestamps if ts.date() == today]
        
        return len(timestamps)
    
    def _get_monthly_count(self, user_id: str, action: str) -> int:
        """Get count of actions this month."""
        if self.use_redis:
            return self._get_monthly_count_redis(user_id, action)
        else:
            return self._get_monthly_count_memory(user_id, action)
    
    def _get_monthly_count_redis(self, user_id: str, action: str) -> int:
        """Get monthly count from Redis."""
        key = f"usage:{user_id}:{action}"
        month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        count = self.redis_client.zcount(
            key,
            month_start.timestamp(),
            datetime.now().timestamp()
        )
        
        return count
    
    def _get_monthly_count_memory(self, user_id: str, action: str) -> int:
        """Get monthly count from memory."""
        this_month = datetime.now().replace(day=1).date()
        
        timestamps = self.usage_data[user_id]['monthly_scans']
        
        # Clean old entries
        timestamps[:] = [ts for ts in timestamps if ts.date() >= this_month]
        
        return len(timestamps)
    
    def get_usage_stats(self, user_id: str, plan: str = 'free') -> Dict:
        """
        Get usage statistics for a user.
        
        Args:
            user_id: User identifier
            plan: User's subscription plan
            
        Returns:
            Usage statistics
        """
        limits = self.LIMITS.get(plan, self.LIMITS['free'])
        
        daily_scans = self._get_daily_count(user_id, 'scans')
        monthly_scans = self._get_monthly_count(user_id, 'scans')
        daily_api_calls = self._get_daily_count(user_id, 'api_calls')
        
        return {
            'plan': plan,
            'scans': {
                'today': daily_scans,
                'daily_limit': limits['scans_per_day'],
                'this_month': monthly_scans,
                'monthly_limit': limits['scans_per_month'],
                'remaining_today': limits['scans_per_day'] - daily_scans if limits['scans_per_day'] != -1 else -1
            },
            'api_calls': {
                'today': daily_api_calls,
                'daily_limit': limits['api_calls_per_day'],
                'remaining_today': limits['api_calls_per_day'] - daily_api_calls if limits['api_calls_per_day'] != -1 else -1
            }
        }


# Usage example
if __name__ == "__main__":
    # Initialize limiter
    limiter = UsageLimiter()  # In-memory for development
    # limiter = UsageLimiter(redis_url='redis://localhost:6379')  # Production
    
    # Check if user can scan
    user_id = "user123"
    plan = "free"
    
    allowed, message = limiter.check_limit(user_id, plan, action='scan')
    
    if allowed:
        print(f"✅ Scan allowed: {message}")
        limiter.record_usage(user_id, action='scan')
    else:
        print(f"❌ Scan blocked: {message}")
    
    # Get usage stats
    stats = limiter.get_usage_stats(user_id, plan)
    print(f"\nUsage Stats: {json.dumps(stats, indent=2)}")
