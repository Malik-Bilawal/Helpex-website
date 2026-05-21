import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from django.core.management.base import BaseCommand
from helpex_app.models import ProductCategory, Product, ProductFeature, ProductScreenshot
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Seed products, categories, and features'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding product categories...')

        categories_data = [
            {'name': 'Developer Tools', 'icon_class': 'fa-code', 'color': '#4D5FF1'},
            {'name': 'Analytics', 'icon_class': 'fa-chart-line', 'color': '#6B7FFF'},
            {'name': 'Security', 'icon_class': 'fa-shield-alt', 'color': '#0C33C2'},
            {'name': 'Productivity', 'icon_class': 'fa-bolt', 'color': '#4D5FF1'},
        ]

        categories = {}
        for i, cat in enumerate(categories_data):
            category, _ = ProductCategory.objects.update_or_create(
                slug=slugify(cat['name']),
                defaults={
                    'name': cat['name'],
                    'icon_class': cat['icon_class'],
                    'color': cat['color'],
                    'order': i,
                    'is_active': True,
                }
            )
            categories[cat['name']] = category
            self.stdout.write(f'  Category: {cat["name"]} [OK]')

        self.stdout.write('\nSeeding products...')

        products_data = [
            {
                'name': 'HelpEx CRM',
                'tagline': 'Customer Relationship Management Reimagined',
                'short_description': 'A powerful, intuitive CRM platform that helps teams manage leads, track deals, and close more sales with AI-powered insights.',
                'description': 'HelpEx CRM is a next-generation customer relationship management platform built for modern teams. With AI-powered lead scoring, automated pipeline management, and real-time analytics, your sales team can focus on what matters most - closing deals.\n\nKey capabilities include contact management, deal tracking, email integration, task automation, custom reporting, and team collaboration tools. The platform integrates seamlessly with popular email providers, calendar apps, and communication tools.',
                'icon_class': 'fa-users-cog',
                'category': 'Productivity',
                'pricing_type': 'paid',
                'price': '29.00',
                'currency': '$',
                'billing_period': '/month',
                'version': 'v3.2.1',
                'tech_stack': ['React', 'Node.js', 'PostgreSQL', 'Redis', 'Docker'],
                'features': [
                    {'title': 'AI Lead Scoring', 'description': 'Automatically prioritize leads based on engagement, demographics, and behavior patterns.', 'icon': 'fa-brain'},
                    {'title': 'Pipeline Automation', 'description': 'Custom workflows that move deals through stages automatically based on triggers and actions.', 'icon': 'fa-cogs'},
                    {'title': 'Real-time Analytics', 'description': 'Live dashboards with customizable reports, forecasts, and performance metrics.', 'icon': 'fa-chart-bar'},
                    {'title': 'Email Integration', 'description': 'Two-way sync with Gmail and Outlook. Track opens, clicks, and replies automatically.', 'icon': 'fa-envelope'},
                    {'title': 'Team Collaboration', 'description': 'Shared notes, task assignments, mentions, and real-time activity feeds.', 'icon': 'fa-users'},
                    {'title': 'Mobile App', 'description': 'Full-featured iOS and Android apps for managing your pipeline on the go.', 'icon': 'fa-mobile-alt'},
                ],
                'faqs': [
                    {'question': 'Can I import data from other CRMs?', 'answer': 'Yes! We support one-click imports from Salesforce, HubSpot, Pipedrive, and Zoho CRM. Custom CSV imports are also available.'},
                    {'question': 'Is there a free trial?', 'answer': 'Absolutely. All plans come with a 14-day free trial with full access to all features. No credit card required.'},
                    {'question': 'How many users can I add?', 'answer': 'The Starter plan supports up to 5 users, Professional up to 25, and Enterprise has unlimited users.'},
                ],
            },
            {
                'name': 'CodeGuard Pro',
                'tagline': 'Automated Code Security Scanner',
                'short_description': 'Enterprise-grade static code analysis and vulnerability detection for modern development teams.',
                'description': 'CodeGuard Pro is an advanced static code analysis tool that integrates directly into your CI/CD pipeline. It automatically scans your codebase for security vulnerabilities, code smells, and performance issues before they reach production.\n\nSupporting over 25 programming languages and frameworks, CodeGuard Pro provides detailed remediation guidance, compliance reporting (SOC 2, HIPAA, GDPR), and team collaboration features to keep your code secure and your developers productive.',
                'icon_class': 'fa-shield-alt',
                'category': 'Security',
                'pricing_type': 'freemium',
                'version': 'v2.0.5',
                'tech_stack': ['Python', 'Rust', 'Elasticsearch', 'GraphQL', 'AWS'],
                'features': [
                    {'title': 'Multi-Language Support', 'description': 'Analyze code in 25+ languages including Python, JavaScript, Java, Go, Rust, and more.', 'icon': 'fa-language'},
                    {'title': 'CI/CD Integration', 'description': 'Seamless plugins for GitHub Actions, GitLab CI, Jenkins, and CircleCI.', 'icon': 'fa-sync-alt'},
                    {'title': 'Compliance Reports', 'description': 'Generate SOC 2, HIPAA, and GDPR compliance reports with a single click.', 'icon': 'fa-file-alt'},
                    {'title': 'Remediation Guidance', 'description': 'Detailed fix suggestions with code examples for every vulnerability found.', 'icon': 'fa-wrench'},
                ],
                'faqs': [
                    {'question': 'Which languages are supported?', 'answer': 'We support 25+ languages including Python, JavaScript/TypeScript, Java, C#, Go, Rust, Ruby, PHP, and more.'},
                    {'question': 'Can I run it locally?', 'answer': 'Yes, CodeGuard Pro offers both cloud-hosted and self-hosted deployment options.'},
                ],
            },
            {
                'name': 'DataPulse Analytics',
                'tagline': 'Real-Time Business Intelligence',
                'short_description': 'Transform raw data into actionable insights with beautiful dashboards and predictive analytics.',
                'description': 'DataPulse Analytics is a comprehensive business intelligence platform that turns your data into actionable insights. Connect to any data source, build stunning dashboards with our drag-and-drop builder, and leverage machine learning for predictive analytics.\n\nWhether you are a startup tracking growth metrics or an enterprise monitoring complex KPIs, DataPulse scales with your needs. Our platform handles millions of records with sub-second query performance.',
                'icon_class': 'fa-chart-line',
                'category': 'Analytics',
                'pricing_type': 'paid',
                'price': '49.00',
                'currency': '$',
                'billing_period': '/month',
                'version': 'v4.1.0',
                'tech_stack': ['Vue.js', 'Python', 'ClickHouse', 'Apache Kafka', 'TensorFlow'],
                'features': [
                    {'title': 'Drag-and-Drop Builder', 'description': 'Create beautiful dashboards without writing a single line of code.', 'icon': 'fa-th-large'},
                    {'title': '50+ Data Connectors', 'description': 'Connect to databases, APIs, spreadsheets, and cloud services instantly.', 'icon': 'fa-plug'},
                    {'title': 'Predictive Analytics', 'description': 'ML-powered forecasts and anomaly detection built into every dashboard.', 'icon': 'fa-magic'},
                    {'title': 'Real-Time Streaming', 'description': 'Process and visualize streaming data with sub-second latency.', 'icon': 'fa-bolt'},
                ],
                'faqs': [
                    {'question': 'What data sources do you support?', 'answer': 'We support 50+ connectors including PostgreSQL, MySQL, MongoDB, BigQuery, Snowflake, Salesforce, Google Analytics, and many more.'},
                    {'question': 'How much data can I process?', 'answer': 'Professional plans handle up to 100M rows/month. Enterprise plans have custom limits based on your needs.'},
                ],
            },
            {
                'name': 'DevKit CLI',
                'tagline': 'The Ultimate Developer Toolkit',
                'short_description': 'A powerful command-line interface that scaffolds projects, manages deployments, and automates dev workflows.',
                'description': 'DevKit CLI is the Swiss Army knife for developers. From scaffolding new projects with best-practice templates to managing cloud deployments, DevKit streamlines your entire development workflow.\n\nBuilt with speed and extensibility in mind, DevKit supports custom plugins, team-shared configurations, and integrates with all major cloud providers and development tools.',
                'icon_class': 'fa-terminal',
                'category': 'Developer Tools',
                'pricing_type': 'free',
                'version': 'v1.8.3',
                'tech_stack': ['Go', ' Cobra', 'Docker', 'Terraform', 'GitHub API'],
                'features': [
                    {'title': 'Project Scaffolding', 'description': 'Generate production-ready project templates for React, Django, Next.js, and 20+ frameworks.', 'icon': 'fa-folder-plus'},
                    {'title': 'Cloud Deployments', 'description': 'One-command deployments to AWS, GCP, Azure, and Vercel with zero configuration.', 'icon': 'fa-cloud-upload-alt'},
                    {'title': 'Plugin System', 'description': 'Extend functionality with community plugins or build your own custom commands.', 'icon': 'fa-puzzle-piece'},
                    {'title': 'Team Configs', 'description': 'Share configurations across your team with version-controlled devkit.yml files.', 'icon': 'fa-share-alt'},
                ],
                'faqs': [
                    {'question': 'Is DevKit really free?', 'answer': 'Yes! DevKit CLI is completely free and open-source under the MIT license.'},
                    {'question': 'Can I create custom plugins?', 'answer': 'Absolutely. Our plugin SDK makes it easy to build and publish custom commands.'},
                ],
            },
        ]

        for i, prod in enumerate(products_data):
            category = categories.get(prod['category'])
            features = prod.pop('features')
            faqs = prod.pop('faqs')
            tech_stack = prod.pop('tech_stack')

            product, created = Product.objects.update_or_create(
                slug=slugify(prod['name']),
                defaults={
                    'name': prod['name'],
                    'category': category,
                    'tagline': prod['tagline'],
                    'short_description': prod['short_description'],
                    'description': prod['description'],
                    'icon_class': prod['icon_class'],
                    'pricing_type': prod['pricing_type'],
                    'price': prod.get('price'),
                    'currency': prod.get('currency', '$'),
                    'billing_period': prod.get('billing_period', ''),
                    'version': prod.get('version', ''),
                    'tech_stack': tech_stack,
                    'faqs': faqs,
                    'order': i,
                    'is_active': True,
                    'is_featured': i < 2,
                }
            )

            # Create detailed features
            for j, feat in enumerate(features):
                ProductFeature.objects.update_or_create(
                    product=product,
                    title=feat['title'],
                    defaults={
                        'description': feat['description'],
                        'icon_class': feat['icon'],
                        'order': j,
                        'is_active': True,
                    }
                )

            status = 'CREATED' if created else 'UPDATED'
            self.stdout.write(f'  Product: {prod["name"]} [{status}]')

        self.stdout.write('\nDone!')
