import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from helpex_app.models import PricingPlan, PricingFeature

plans_data = [
    {
        'name': 'Starter',
        'description': 'Perfect for small projects and startups',
        'plan_type': 'monthly',
        'price': '299.00',
        'currency': '$',
        'billing_period': '/month',
        'popular_badge': 'none',
        'cta_text': 'Get Started',
        'icon_class': 'fa-rocket',
        'color_accent': '#28A197',
        'features': [
            '5 Pages Website',
            'Responsive Design',
            'Basic SEO Setup',
            'Contact Form',
            '1 Month Support'
        ]
    },
    {
        'name': 'Professional',
        'description': 'Ideal for growing businesses',
        'plan_type': 'monthly',
        'price': '599.00',
        'currency': '$',
        'billing_period': '/month',
        'popular_badge': 'popular',
        'cta_text': 'Start Now',
        'icon_class': 'fa-star',
        'color_accent': '#28A197',
        'features': [
            '15 Pages Website',
            'Custom Design',
            'Advanced SEO',
            'CMS Integration',
            'E-commerce Ready',
            '3 Months Support',
            'Analytics Setup'
        ]
    },
    {
        'name': 'Enterprise',
        'description': 'For large-scale digital solutions',
        'plan_type': 'monthly',
        'price': '999.00',
        'currency': '$',
        'billing_period': '/month',
        'popular_badge': 'best_value',
        'cta_text': 'Contact Us',
        'icon_class': 'fa-crown',
        'color_accent': '#1A1F3B',
        'features': [
            'Unlimited Pages',
            'Premium Design',
            'Full SEO Suite',
            'Custom Features',
            'API Integration',
            'Priority Support',
            'Performance Optimization',
            'Security Audit'
        ]
    }
]

created = 0
for plan_data in plans_data:
    features = plan_data.pop('features')
    plan = PricingPlan.objects.create(**plan_data)
    for i, feat in enumerate(features):
        PricingFeature.objects.create(plan=plan, text=feat, included=True, order=i)
    created += 1
    print(f'Created: {plan.name}')

print(f'\nSuccessfully created {created} pricing plans with features!')
