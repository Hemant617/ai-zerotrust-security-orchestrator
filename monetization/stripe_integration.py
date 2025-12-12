"""
Stripe Payment Integration for Monetization
"""

import stripe
import os
from typing import Dict, Any, Optional
from datetime import datetime

# Set your Stripe API key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', 'sk_test_...')


class PaymentProcessor:
    """
    Handle payment processing and subscription management.
    """
    
    # Pricing plans
    PLANS = {
        'free': {
            'name': 'Free',
            'price': 0,
            'scans_per_day': 10,
            'api_access': False,
            'support': 'community'
        },
        'pro': {
            'name': 'Pro',
            'price': 9.99,
            'price_id': 'price_pro_monthly',  # Replace with your Stripe price ID
            'scans_per_day': -1,  # Unlimited
            'api_access': True,
            'support': 'email'
        },
        'enterprise': {
            'name': 'Enterprise',
            'price': 99.00,
            'price_id': 'price_enterprise_monthly',  # Replace with your Stripe price ID
            'scans_per_day': -1,  # Unlimited
            'api_access': True,
            'support': 'priority',
            'custom_integration': True,
            'white_label': True
        }
    }
    
    def __init__(self):
        """Initialize payment processor."""
        self.stripe = stripe
    
    def create_checkout_session(
        self, 
        plan: str, 
        success_url: str, 
        cancel_url: str,
        customer_email: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a Stripe checkout session for subscription.
        
        Args:
            plan: Plan name ('pro' or 'enterprise')
            success_url: URL to redirect after successful payment
            cancel_url: URL to redirect if payment is cancelled
            customer_email: Optional customer email
            
        Returns:
            Checkout session data including URL
        """
        if plan not in ['pro', 'enterprise']:
            raise ValueError("Invalid plan. Choose 'pro' or 'enterprise'")
        
        plan_data = self.PLANS[plan]
        
        session_params = {
            'payment_method_types': ['card'],
            'line_items': [{
                'price': plan_data['price_id'],
                'quantity': 1,
            }],
            'mode': 'subscription',
            'success_url': success_url + '?session_id={CHECKOUT_SESSION_ID}',
            'cancel_url': cancel_url,
        }
        
        if customer_email:
            session_params['customer_email'] = customer_email
        
        session = self.stripe.checkout.Session.create(**session_params)
        
        return {
            'session_id': session.id,
            'url': session.url,
            'plan': plan,
            'price': plan_data['price']
        }
    
    def create_customer_portal_session(
        self, 
        customer_id: str, 
        return_url: str
    ) -> Dict[str, Any]:
        """
        Create a customer portal session for managing subscription.
        
        Args:
            customer_id: Stripe customer ID
            return_url: URL to return to after managing subscription
            
        Returns:
            Portal session data including URL
        """
        session = self.stripe.billing_portal.Session.create(
            customer=customer_id,
            return_url=return_url,
        )
        
        return {
            'url': session.url
        }
    
    def verify_webhook(self, payload: bytes, signature: str) -> Optional[Dict[str, Any]]:
        """
        Verify and process Stripe webhook events.
        
        Args:
            payload: Request body
            signature: Stripe signature header
            
        Returns:
            Event data if valid, None otherwise
        """
        webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
        
        try:
            event = self.stripe.Webhook.construct_event(
                payload, signature, webhook_secret
            )
            return event
        except ValueError:
            # Invalid payload
            return None
        except stripe.error.SignatureVerificationError:
            # Invalid signature
            return None
    
    def handle_webhook_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle different webhook event types.
        
        Args:
            event: Stripe event data
            
        Returns:
            Processing result
        """
        event_type = event['type']
        
        if event_type == 'checkout.session.completed':
            # Payment successful
            session = event['data']['object']
            return self._handle_successful_payment(session)
        
        elif event_type == 'customer.subscription.updated':
            # Subscription updated
            subscription = event['data']['object']
            return self._handle_subscription_update(subscription)
        
        elif event_type == 'customer.subscription.deleted':
            # Subscription cancelled
            subscription = event['data']['object']
            return self._handle_subscription_cancellation(subscription)
        
        elif event_type == 'invoice.payment_failed':
            # Payment failed
            invoice = event['data']['object']
            return self._handle_payment_failure(invoice)
        
        return {'status': 'unhandled', 'event_type': event_type}
    
    def _handle_successful_payment(self, session: Dict[str, Any]) -> Dict[str, Any]:
        """Handle successful payment."""
        customer_id = session.get('customer')
        subscription_id = session.get('subscription')
        
        # TODO: Update user's plan in your database
        # user.plan = 'pro' or 'enterprise'
        # user.stripe_customer_id = customer_id
        # user.stripe_subscription_id = subscription_id
        # user.save()
        
        return {
            'status': 'success',
            'customer_id': customer_id,
            'subscription_id': subscription_id
        }
    
    def _handle_subscription_update(self, subscription: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription update."""
        customer_id = subscription.get('customer')
        status = subscription.get('status')
        
        # TODO: Update subscription status in database
        
        return {
            'status': 'updated',
            'customer_id': customer_id,
            'subscription_status': status
        }
    
    def _handle_subscription_cancellation(self, subscription: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription cancellation."""
        customer_id = subscription.get('customer')
        
        # TODO: Downgrade user to free plan
        # user.plan = 'free'
        # user.save()
        
        return {
            'status': 'cancelled',
            'customer_id': customer_id
        }
    
    def _handle_payment_failure(self, invoice: Dict[str, Any]) -> Dict[str, Any]:
        """Handle payment failure."""
        customer_id = invoice.get('customer')
        
        # TODO: Send email notification to user
        # TODO: Maybe suspend account after multiple failures
        
        return {
            'status': 'payment_failed',
            'customer_id': customer_id
        }
    
    def get_subscription_status(self, subscription_id: str) -> Dict[str, Any]:
        """
        Get current subscription status.
        
        Args:
            subscription_id: Stripe subscription ID
            
        Returns:
            Subscription details
        """
        subscription = self.stripe.Subscription.retrieve(subscription_id)
        
        return {
            'id': subscription.id,
            'status': subscription.status,
            'current_period_end': datetime.fromtimestamp(subscription.current_period_end),
            'cancel_at_period_end': subscription.cancel_at_period_end,
            'plan': subscription['items']['data'][0]['price']['id']
        }
    
    def cancel_subscription(self, subscription_id: str, at_period_end: bool = True) -> Dict[str, Any]:
        """
        Cancel a subscription.
        
        Args:
            subscription_id: Stripe subscription ID
            at_period_end: If True, cancel at end of billing period
            
        Returns:
            Cancellation result
        """
        if at_period_end:
            subscription = self.stripe.Subscription.modify(
                subscription_id,
                cancel_at_period_end=True
            )
        else:
            subscription = self.stripe.Subscription.delete(subscription_id)
        
        return {
            'status': 'cancelled',
            'subscription_id': subscription_id,
            'cancel_at_period_end': at_period_end
        }


# Usage example
if __name__ == "__main__":
    processor = PaymentProcessor()
    
    # Create checkout session
    session = processor.create_checkout_session(
        plan='pro',
        success_url='https://yourapp.com/success',
        cancel_url='https://yourapp.com/cancel',
        customer_email='user@example.com'
    )
    
    print(f"Checkout URL: {session['url']}")
    print(f"Session ID: {session['session_id']}")
