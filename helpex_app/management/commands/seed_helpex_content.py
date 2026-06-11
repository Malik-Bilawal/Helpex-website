import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from helpex_app.models import (
    SiteSettings, HeroSection, Service, Testimonial, ProcessStep,
    PortfolioCategory, PortfolioItem, TeamMember, Client, BlogCategory, BlogPost,
    ProductCategory, Product, ProductFeature, ProductScreenshot,
    WhyChooseUsSection, WhyChooseUsReason, WhyChooseUsStat,
    RegisteredCompany
)


class Command(BaseCommand):
    help = 'Update all website content to match The Helpex brand'

    def handle(self, *args, **options):
        self.stdout.write('Updating website content to The Helpex...')

        # --- 1. SiteSettings ---
        settings, _ = SiteSettings.objects.get_or_create(pk=1)
        settings.company_name = "The Helpex"
        settings.tagline = "Your Tech Helpers — Helping You Excel in the Digital World"
        settings.description = "The Helpex is a Karachi-based software, AI, and business systems company that helps organizations streamline operations, improve visibility, and accelerate growth through smart digital solutions. We specialize in hospitality technology, ERP systems, AI automation, and custom software development."
        settings.email = "info@thehelpex.com"
        settings.phone = "+92 319 4959219"
        settings.address = "Karachi, Pakistan"
        settings.office_hours = "Mon-Fri: 9AM - 6PM"
        settings.social_twitter = "https://twitter.com/thehelpex"
        settings.social_instagram = "https://instagram.com/thehelpex"
        settings.social_linkedin = "https://linkedin.com/company/thehelpex"
        settings.social_github = "https://github.com/thehelpex"
        settings.primary_color = "#4D5FF1"
        settings.secondary_color = "#0B0B0B"
        settings.meta_title = "The Helpex — Software, AI & Business Systems Company"
        settings.meta_description = "Your Tech Helpers — Helping You Excel in the Digital World. Custom software, AI automation, ERP systems, and hospitality technology solutions."
        settings.copyright_text = "The Helpex. All rights reserved."
        settings.save()
        self.stdout.write('  [OK] SiteSettings')

        # --- 2. Hero Section ---
        HeroSection.objects.all().delete()
        HeroSection.objects.create(
            title_line_1="Your Tech Helpers",
            title_line_2="Helping You Excel in the Digital World",
            typing_texts=['hospitality technology', 'AI-powered systems', 'ERP solutions', 'custom software', 'business automation'],
            description='The Helpex is a Karachi-based software, AI, and business systems company that helps organizations streamline operations, improve visibility, and accelerate growth through smart digital solutions.',
            cta_button_text='Explore Our Products',
            cta_button_url='/products/',
            secondary_cta_text='Our Story',
            secondary_cta_url='/about/',
            stats_number_1='5', stats_label_1='Products',
            stats_number_2='7', stats_label_2='Organizations',
            stats_number_3='88%', stats_label_3='Client Retention',
            badge_text='YOUR TECH HELPERS',
            show_badge=True,
            is_active=True,
        )
        self.stdout.write('  [OK] Hero Section')

        # --- 3. Services ---
        Service.objects.all().delete()
        services = [
            {
                'title': 'Custom Software Development',
                'short_description': 'Tailor-made systems built around your exact business needs',
                'description': 'Full-cycle custom software development from idea to live deployment. We build tailor-made systems designed around your exact business needs — whether you need a CRM, ERP, POS, or any other business application.',
                'icon_class': 'fa-laptop-code',
                'tags': ['Python', 'Django', 'React', 'PostgreSQL'],
                'features': [
                    {'title': 'Full-Cycle Development', 'description': 'From ideation and architecture to development, testing, and deployment.', 'icon': 'fa-sync-alt'},
                    {'title': 'Scalable Architecture', 'description': 'Systems built to grow with your business, handling increased loads seamlessly.', 'icon': 'fa-chart-line'},
                    {'title': 'Integration Ready', 'description': 'Seamless integration with existing tools, APIs, and third-party services.', 'icon': 'fa-plug'},
                ],
                'order': 1,
            },
            {
                'title': 'Web & Mobile Development',
                'short_description': 'Professional websites, web apps, and mobile solutions',
                'description': 'Professional websites, web applications, and mobile solutions built with the latest technologies — React, Next.js, Flutter, and Django. Responsive, fast, and built for user experience.',
                'icon_class': 'fa-globe',
                'tags': ['React', 'Next.js', 'Flutter', 'Django'],
                'features': [
                    {'title': 'Responsive Design', 'description': 'Beautiful, mobile-first designs that work flawlessly across all devices.', 'icon': 'fa-mobile-alt'},
                    {'title': 'Progressive Web Apps', 'description': 'Native-like experiences through modern PWA technologies.', 'icon': 'fa-download'},
                    {'title': 'Cross-Platform Mobile', 'description': 'Flutter-based mobile apps for both iOS and Android from a single codebase.', 'icon': 'fa-apple-alt'},
                ],
                'order': 2,
            },
            {
                'title': 'ERP / CRM / POS Solutions',
                'short_description': 'Complete business management and operational systems',
                'description': 'End-to-end ERP, CRM, and POS systems that give you complete control over accounting, inventory, sales, purchases, and business operations. Multi-branch support with real-time reporting.',
                'icon_class': 'fa-cogs',
                'tags': ['ERP', 'CRM', 'POS', 'Accounting'],
                'features': [
                    {'title': 'Multi-Branch Support', 'description': 'Manage multiple locations with centralized control and reporting.', 'icon': 'fa-layer-group'},
                    {'title': 'Real-Time Ledger', 'description': 'Live financial tracking with running balances and audit trail.', 'icon': 'fa-book'},
                    {'title': 'Inventory Control', 'description': 'Complete stock management with purchase, sales, and transfer tracking.', 'icon': 'fa-boxes'},
                ],
                'order': 3,
            },
            {
                'title': 'AI Agents & Automation',
                'short_description': 'Intelligent automation and AI-powered workflows',
                'description': 'AI agents, LLM integration, workflow bots, and agentic AI systems that automate repetitive tasks, improve decision-making, and transform your business operations.',
                'icon_class': 'fa-robot',
                'tags': ['AI', 'LLM', 'Automation', 'Agents'],
                'features': [
                    {'title': 'LLM Integration', 'description': 'Integrate large language models into your workflows for intelligent assistance.', 'icon': 'fa-brain'},
                    {'title': 'Workflow Automation', 'description': 'Automate repetitive tasks with intelligent bots and custom workflows.', 'icon': 'fa-robot'},
                    {'title': 'Agentic AI', 'description': 'Deploy autonomous AI agents that learn, adapt, and act on your behalf.', 'icon': 'fa-microchip'},
                ],
                'order': 4,
            },
            {
                'title': 'Digital Marketing',
                'short_description': 'Strategic online presence and growth',
                'description': 'Strategic digital marketing services to boost your online visibility. SEO, content marketing, and paid advertising campaigns that deliver measurable results.',
                'icon_class': 'fa-bullhorn',
                'tags': ['SEO', 'Content', 'Ads', 'Analytics'],
                'features': [
                    {'title': 'Search Optimization', 'description': 'Improve your search rankings and drive organic traffic.', 'icon': 'fa-search'},
                    {'title': 'Content Strategy', 'description': 'Compelling content that engages your audience and builds brand authority.', 'icon': 'fa-newspaper'},
                    {'title': 'Paid Campaigns', 'description': 'Targeted advertising campaigns optimized for ROI.', 'icon': 'fa-ad'},
                ],
                'order': 5,
            },
            {
                'title': 'SaaS Product Development',
                'short_description': 'From concept to scalable SaaS platforms',
                'description': 'Design, build, and launch scalable SaaS products. From architecture planning to subscription management, we help you transform your software idea into a market-ready platform.',
                'icon_class': 'fa-cloud-upload-alt',
                'tags': ['SaaS', 'Payments', 'Multi-Tenant', 'API'],
                'features': [
                    {'title': 'Multi-Tenant Architecture', 'description': 'Scalable SaaS infrastructure designed for growth.', 'icon': 'fa-building'},
                    {'title': 'Subscription Management', 'description': 'Integrated billing, plans, and user management.', 'icon': 'fa-credit-card'},
                    {'title': 'API-First Design', 'description': 'RESTful APIs and webhook support for extensibility.', 'icon': 'fa-code-branch'},
                ],
                'order': 6,
            },
        ]
        for s in services:
            svc = Service.objects.create(
                title=s['title'],
                short_description=s['short_description'],
                description=s['description'],
                icon_class=s['icon_class'],
                tags=s['tags'],
                features=s['features'],
                order=s['order'],
                is_active=True,
                is_featured=True,
            )
        self.stdout.write(f'  [OK] {len(services)} Services')

        # --- 4. Process Steps ---
        ProcessStep.objects.all().delete()
        steps = [
            ('Discovery', 'We dive deep into your business, understanding your operations, challenges, and goals.', 'fa-lightbulb'),
            ('Strategy', 'We craft a tailored roadmap with clear milestones and deliverables.', 'fa-chess'),
            ('Development', 'Agile development sprints with regular demos and feedback loops.', 'fa-code'),
            ('Deployment', 'We deploy, train your team, and provide ongoing support.', 'fa-rocket'),
        ]
        for i, (title, desc, icon) in enumerate(steps, 1):
            ProcessStep.objects.create(step_number=i, title=title, description=desc, icon_class=icon, order=i)
        self.stdout.write(f'  [OK] {len(steps)} Process Steps')

        # --- 5. Testimonials ---
        Testimonial.objects.all().delete()
        testimonial_data = [
            {'name': 'Hasnain A. Samad', 'role': 'Founder & CEO', 'company': 'The Helpex', 'quote': 'Technology should serve people. That belief drives everything we build at The Helpex.', 'rating': 5, 'order': 1},
            {'name': 'Drive Inn Management', 'role': 'Operations Director', 'company': 'Drive Inn Marquees', 'quote': 'Hollox transformed how we manage our banquet operations. From bookings to reconciliation, everything is now in one place.', 'rating': 5, 'order': 2},
            {'name': 'Saltanat Management', 'role': 'General Manager', 'company': 'Saltanat Restaurant', 'quote': 'Bookara helped us eliminate fragmented reservation processes and improved our guest experience significantly.', 'rating': 5, 'order': 3},
            {'name': 'Client', 'role': 'CEO', 'company': 'SME Partner', 'quote': 'The Helpex ERP gave us the financial visibility and operational control we needed to scale our business.', 'rating': 5, 'order': 4},
        ]
        for t in testimonial_data:
            Testimonial.objects.create(**t)
        self.stdout.write(f'  [OK] {len(testimonial_data)} Testimonials')

        # --- 6. Team ---
        TeamMember.objects.all().delete()
        team = [
            ('Hasnain A. Samad', 'Founder & CEO', 'Visionary leader who started freelancing at 16 and built The Helpex around a human-centered technology philosophy.'),
            ('The Helpex Team', 'Engineering & Design', 'A dedicated team of software engineers, AI specialists, and designers committed to building systems that serve people.'),
        ]
        for name, role, bio in team:
            TeamMember.objects.create(name=name, role=role, bio=bio)
        self.stdout.write(f'  [OK] {len(team)} Team Members')

        # --- 7. Clients ---
        Client.objects.all().delete()
        clients = [
            ('Drive Inn Marquees', 'Hospitality', True),
            ('Saltanat Banquet', 'Hospitality', True),
            ('Saltanat Restaurant', 'Hospitality', True),
            ('SME Partners', 'Technology', False),
            ('Karachi Businesses', 'Retail', False),
        ]
        for name, industry, featured in clients:
            Client.objects.create(name=name, slug=slugify(name), industry=industry, is_featured=featured)
        self.stdout.write(f'  [OK] {len(clients)} Clients')

        # --- 8. Products (Replace with Hollox, Bookara, The Helpex ERP) ---
        Product.objects.all().delete()
        ProductFeature.objects.all().delete()
        ProductScreenshot.objects.all().delete()

        # Get or create categories
        cat_hospitality, _ = ProductCategory.objects.get_or_create(
            slug='hospitality', defaults={'name': 'Hospitality Technology', 'icon_class': 'fa-hotel', 'order': 1}
        )
        cat_erp, _ = ProductCategory.objects.get_or_create(
            slug='business-systems', defaults={'name': 'Business Systems', 'icon_class': 'fa-building', 'order': 2}
        )

        # Product 1: Hollox
        hollox = Product.objects.create(
            name='Hollox',
            slug='hollox',
            category=cat_hospitality,
            tagline='Banquet Operations & Financial Management System',
            short_description='Hollox is a comprehensive hospitality operations platform designed for banquet halls, event venues, resorts, hotels, clubs, and marquee businesses.',
            description='Hollox is a comprehensive hospitality operations platform designed for banquet halls, event venues, resorts, hotels, clubs, and marquee businesses.\n\nBuilt in collaboration with hospitality professionals, Hollox helps organizations manage the complete event and booking lifecycle while providing real-time financial visibility and operational control.\n\nFrom quotation generation to final payment reconciliation, Hollox centralizes every stage of event management into a single platform.',
            icon_class='fa-hotel',
            pricing_type='contact',
            version='v1.0',
            tech_stack=['Django', 'PostgreSQL', 'React', 'Docker'],
            features=[
                {'title': 'Booking & Event Lifecycle', 'description': 'Complete booking management from inquiry to closing, with full lifecycle tracking.', 'icon': 'fa-calendar-check'},
                {'title': 'Venue Availability Tracking', 'description': 'Real-time hall and venue availability calendar with instant status updates.', 'icon': 'fa-calendar-day'},
                {'title': 'Quotation Generation', 'description': 'Professional PDF quotations with automated pricing and customizable templates.', 'icon': 'fa-file-invoice'},
                {'title': 'Payment & Balance Tracking', 'description': 'Track payments, outstanding balances, and payment schedules per booking.', 'icon': 'fa-credit-card'},
                {'title': 'Cash Reconciliation', 'description': 'Daily cash reconciliation with petty cash management and audit trail.', 'icon': 'fa-coins'},
                {'title': 'Management Dashboards', 'description': 'CEO and management dashboards with real-time operational and financial metrics.', 'icon': 'fa-chart-pie'},
            ],
            faqs=[
                {'question': 'Is Hollox suitable for small venues?', 'answer': 'Yes! Hollox is designed for venues of all sizes — from single-hall marquees to multi-venue resorts and hotels.'},
                {'question': 'Can Hollox prevent double bookings?', 'answer': 'Absolutely. Real-time availability tracking ensures no venue is double-booked, with automated conflict detection.'},
                {'question': 'Does it support cash reconciliation?', 'answer': 'Yes, Hollox has a comprehensive cash reconciliation module with daily closing, petty cash, and audit trail features.'},
            ],
            order=1,
            is_active=True,
            is_featured=True,
        )
        self.stdout.write('  [OK] Product: Hollox')

        # Product 2: Bookara
        bookara = Product.objects.create(
            name='Bookara',
            slug='bookara',
            category=cat_hospitality,
            tagline='Reservation & Events Management System',
            short_description='Bookara connects Reservations, Events, and GRO departments for restaurants and hospitality businesses in a single operational ecosystem.',
            description='Bookara is a hospitality management platform designed to connect Reservations, Events, and Guest Relations Operations (GRO) departments within a single operational ecosystem.\n\nThe platform helps hospitality organizations eliminate fragmented reservation processes, improve interdepartmental coordination, and provide management with real-time visibility into bookings and events.',
            icon_class='fa-calendar-alt',
            pricing_type='contact',
            version='v1.0',
            tech_stack=['Django', 'PostgreSQL', 'React', 'Docker'],
            features=[
                {'title': 'Reservation Management', 'description': 'Centralized reservation system with real-time availability and instant booking confirmation.', 'icon': 'fa-book'},
                {'title': 'Event Coordination', 'description': 'Coordinate events across departments with shared calendars and task management.', 'icon': 'fa-calendar-week'},
                {'title': 'Venue Capacity Management', 'description': 'Track venue capacities, manage seating layouts, and optimize space utilization.', 'icon': 'fa-vector-square'},
                {'title': 'Payment Tracking', 'description': 'Monitor payments, deposits, and outstanding balances per reservation.', 'icon': 'fa-money-bill-wave'},
                {'title': 'Digital Booking Slips', 'description': 'Generate and manage digital booking slips with real-time status updates.', 'icon': 'fa-file-alt'},
                {'title': 'Operational Reporting', 'description': 'Real-time reports on reservations, events, revenue, and operational metrics.', 'icon': 'fa-chart-bar'},
            ],
            faqs=[
                {'question': 'How does Bookara differ from Hollox?', 'answer': 'While Hollox focuses on banquet hall operations, Bookara is designed for restaurants and hospitality venues managing reservations, events, and guest relations.'},
                {'question': 'Can Bookara handle multiple restaurant branches?', 'answer': 'Yes, Bookara supports multi-branch management with centralized reporting and per-branch operational control.'},
            ],
            order=2,
            is_active=True,
            is_featured=True,
        )
        self.stdout.write('  [OK] Product: Bookara')

        # Product 3: The Helpex ERP
        erp = Product.objects.create(
            name='The Helpex ERP',
            slug='the-helpex-erp',
            category=cat_erp,
            tagline='Cloud ERP for Growing Businesses',
            short_description='A cloud-based business management platform for SMEs that integrates accounting, inventory, sales, purchases, payments, CRM, and reporting.',
            description='The Helpex ERP is a cloud-based business management platform designed for small and medium-sized enterprises seeking greater operational control, financial visibility, and process automation.\n\nBuilt using Django and PostgreSQL/MySQL, the platform integrates accounting, inventory, sales, purchases, payments, CRM, and reporting into a single system.',
            icon_class='fa-building',
            pricing_type='contact',
            version='v1.0',
            tech_stack=['Django', 'PostgreSQL', 'MySQL', 'React', 'Docker'],
            features=[
                {'title': 'CRM Module', 'description': 'Manage customers, suppliers, and contacts with full interaction history.', 'icon': 'fa-users'},
                {'title': 'Inventory Management', 'description': 'Complete stock control with purchase, sales, and transfer management.', 'icon': 'fa-boxes'},
                {'title': 'Sales & Purchases', 'description': 'End-to-end sales and purchase management with invoice generation.', 'icon': 'fa-shopping-cart'},
                {'title': 'Ledger & Accounting', 'description': 'Real-time ledger with running balances, journal entries, and financial reporting.', 'icon': 'fa-book'},
                {'title': 'Multi-Branch Support', 'description': 'Manage multiple branches with centralized or per-branch control.', 'icon': 'fa-layer-group'},
                {'title': 'Reports & Analytics', 'description': 'Financial reports, stock reports, and business intelligence dashboards.', 'icon': 'fa-chart-line'},
            ],
            faqs=[
                {'question': 'Is The Helpex ERP suitable for my business?', 'answer': 'If you are an SME looking for an integrated accounting, inventory, and operations system, The Helpex ERP is a great fit.'},
                {'question': 'Does it support multi-branch operations?', 'answer': 'Yes! Multi-branch support is one of our core features, with both centralized and per-branch configurations.'},
                {'question': 'Is it cloud-based?', 'answer': 'Yes, The Helpex ERP is fully cloud-based and accessible from anywhere with an internet connection.'},
            ],
            order=3,
            is_active=True,
            is_featured=True,
        )
        self.stdout.write('  [OK] Product: The Helpex ERP')

        # --- 9. Portfolio Categories & Items ---
        PortfolioCategory.objects.all().delete()
        PortfolioItem.objects.all().delete()

        cat_hospitality_portfolio = PortfolioCategory.objects.create(name='Hospitality Technology')
        cat_erp_portfolio = PortfolioCategory.objects.create(name='ERP Systems')
        cat_web = PortfolioCategory.objects.create(name='Web Development')

        PortfolioItem.objects.create(
            title='Hollox - Banquet Management',
            description='Comprehensive banquet operations and financial management platform for Drive Inn Marquees and Saltanat Banquet.',
            category=cat_hospitality_portfolio,
            client_name='Drive Inn Marquees',
            tags=['Django', 'React', 'Hospitality'],
            is_active=True,
        )
        PortfolioItem.objects.create(
            title='Bookara - Reservation System',
            description='Reservation and events management platform for Saltanat Restaurant, connecting Reservations, Events, and GRO departments.',
            category=cat_hospitality_portfolio,
            client_name='Saltanat Restaurant',
            tags=['Django', 'PostgreSQL', 'Hospitality'],
            is_active=True,
        )
        PortfolioItem.objects.create(
            title='The Helpex ERP',
            description='Cloud-based ERP system for SMEs with CRM, inventory, sales, purchases, ledger, and multi-branch support.',
            category=cat_erp_portfolio,
            tags=['Django', 'PostgreSQL', 'ERP'],
            is_active=True,
        )
        self.stdout.write('  [OK] Portfolio')

        # --- 10. Blog ---
        BlogCategory.objects.all().delete()
        BlogPost.objects.all().delete()
        blog_cats = {
            'Hospitality Tech': BlogCategory.objects.create(name='Hospitality Tech', description='Technology for hospitality businesses'),
            'ERP & Operations': BlogCategory.objects.create(name='ERP & Operations', description='ERP systems and business operations insights'),
            'AI & Automation': BlogCategory.objects.create(name='AI & Automation', description='AI and automation trends'),
        }
        BlogPost.objects.create(
            title='Why Hospitality Businesses Need Integrated Software',
            excerpt='Learn how integrated systems like Hollox and Bookara can transform your hospitality operations.',
            content='Hospitality businesses face unique operational challenges — fragmented processes, manual tracking, and lack of visibility...',
            category=blog_cats['Hospitality Tech'],
            author='The Helpex Team',
            is_published=True,
            is_featured=True,
        )
        BlogPost.objects.create(
            title='The Helpex ERP vs Spreadsheets: Why You Need to Upgrade',
            excerpt='Discover why growing businesses are moving from spreadsheets to integrated ERP systems.',
            content='Spreadsheets have their place, but as your business grows, they become a liability...',
            category=blog_cats['ERP & Operations'],
            author='The Helpex Team',
            is_published=True,
            is_featured=True,
        )
        BlogPost.objects.create(
            title='AI Agents: The Next Frontier in Business Automation',
            excerpt='How AI agents and agentic AI are transforming business operations.',
            content='Artificial intelligence is entering a new phase — one where AI agents can act autonomously...',
            category=blog_cats['AI & Automation'],
            author='The Helpex Team',
            is_published=True,
            is_featured=False,
        )
        self.stdout.write('  [OK] Blog')

        # --- 11. Why Choose Us ---
        WhyChooseUsSection.objects.all().delete()
        WhyChooseUsReason.objects.all().delete()
        WhyChooseUsStat.objects.all().delete()

        WhyChooseUsSection.objects.create(
            title='Why Choose The Helpex',
            subtitle='We build technology with empathy — not just software, but partnerships that drive real results.',
            is_active=True,
        )

        reasons = [
            ('Industry-Specific Solutions', 'We build systems designed for your specific industry — hospitality, retail, manufacturing, and more.', 'fa-industry', 1),
            ('Hands-On Training & Support', 'We don\'t just deploy software; we train your team and provide ongoing support.', 'fa-chalkboard-teacher', 2),
            ('Long-Term Partnership', 'We believe in long-term relationships, not one-off projects. Your success is our success.', 'fa-handshake', 3),
            ('Operational & Financial Visibility', 'Real-time dashboards and reports that give you complete visibility into your operations.', 'fa-chart-line', 4),
            ('Automation That Reduces Manual Work', 'We identify repetitive tasks and build automation that saves your team hours of manual work.', 'fa-robot', 5),
            ('Scalable Cloud-Based Systems', 'Our systems are cloud-based and designed to scale with your business as you grow.', 'fa-cloud', 6),
        ]
        for title, desc, icon, order in reasons:
            WhyChooseUsReason.objects.create(title=title, description=desc, icon_class=icon, order=order)

        stats = [
            ('5', 'Products Built', 'fa-cube', 1),
            ('7', 'Organizations Served', 'fa-building', 2),
            ('88%', 'Client Retention', 'fa-heart', 3),
            ('3+', 'Years of Impact', 'fa-calendar-alt', 4),
        ]
        for number, label, icon, order in stats:
            WhyChooseUsStat.objects.create(number=number, label=label, icon_class=icon, order=order)

        self.stdout.write('  [OK] Why Choose Us')

        # --- 12. Registered Companies ---
        RegisteredCompany.objects.all().delete()
        companies = [
            {'name': 'SECP Pakistan', 'description': 'Securities & Exchange Commission of Pakistan'},
            {'name': 'P@SHA', 'description': 'Pakistan Software Houses Association'},
            {'name': 'NTN Registered', 'description': 'National Tax Number — FBR'},
        ]
        for i, c in enumerate(companies):
            RegisteredCompany.objects.create(name=c['name'], description=c['description'], order=i)
        self.stdout.write('  [OK] Registered Companies')

        self.stdout.write('\n======================================')
        self.stdout.write('All content updated to The Helpex brand!')
        self.stdout.write('======================================')
