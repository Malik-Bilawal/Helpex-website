from django.core.management.base import BaseCommand
from helpex_app.models import HeroSection, Service, Testimonial, ProcessStep, PortfolioCategory, PortfolioItem, SiteSettings, TeamMember


class Command(BaseCommand):
    help = 'Creates all sample content for the website'

    def handle(self, *args, **options):
        print('Creating sample data...')
        
        # 1. Site Settings
        settings, _ = SiteSettings.objects.get_or_create(pk=1)
        settings.company_name = "HELPEX BRO"
        settings.tagline = "Adaptive Digital Studio"
        settings.email = "hello@helpex.com"
        settings.phone = "+1 (555) 123-4567"
        settings.save()
        print('[OK] Site Settings')
        
        # 2. Hero
        HeroSection.objects.all().delete()
        HeroSection.objects.create(
            title_line_1="We craft",
            title_line_2="experiences",
            typing_texts=['digital experiences', 'web applications', 'software solutions'],
            description='HELPEX delivers premium web applications and iconic visual identities.',
            cta_button_text='Start Your Project',
            cta_button_url='/contact/',
            stats_number_1='180+', stats_label_1='Projects',
            stats_number_2='98%', stats_label_2='Satisfaction',
            stats_number_3='50+', stats_label_3='Team',
            badge_text='ADAPTIVE DIGITAL STUDIO',
            show_badge=True,
            is_active=True,
        )
        print('[OK] Hero Section')
        
        # 3. Services
        Service.objects.all().delete()
        services = [
            {'title': 'Web Development', 'short_description': 'Modern websites', 'description': 'Modern, responsive websites.', 'icon_class': 'fa-code', 'tags': ['React', 'Vue'], 'order': 1},
            {'title': 'Software Solutions', 'short_description': 'Custom SaaS', 'description': 'Custom software solutions.', 'icon_class': 'fa-cogs', 'tags': ['SaaS', 'ERP'], 'order': 2},
            {'title': 'Brand & Design', 'short_description': 'Visual identities', 'description': 'Visual identities and branding.', 'icon_class': 'fa-palette', 'tags': ['Logo', 'UI/UX'], 'order': 3},
            {'title': 'Mobile Apps', 'short_description': 'Cross-platform', 'description': 'Mobile applications.', 'icon_class': 'fa-mobile-alt', 'tags': ['iOS', 'Android'], 'order': 4},
            {'title': 'Cloud & DevOps', 'short_description': 'Scalable infrastructure', 'description': 'Cloud solutions.', 'icon_class': 'fa-cloud', 'tags': ['AWS', 'Azure'], 'order': 5},
            {'title': 'AI & Automation', 'short_description': 'Smart workflows', 'description': 'AI integration.', 'icon_class': 'fa-brain', 'tags': ['ML', 'LLM'], 'order': 6},
        ]
        for s in services:
            Service.objects.create(**s)
        print(f'[OK] {len(services)} Services')
        
        # 4. Process
        ProcessStep.objects.all().delete()
        for i, (title, desc, icon) in enumerate([
            ('Discovery', 'We dive deep into your goals.', 'fa-lightbulb'),
            ('Strategy', 'We craft a tailored roadmap.', 'fa-chess'),
            ('Development', 'Agile development sprints.', 'fa-code'),
            ('Launch', 'We deploy your product.', 'fa-rocket'),
        ], 1):
            ProcessStep.objects.create(step_number=i, title=title, description=desc, icon_class=icon, order=i)
        print('[OK] 4 Process Steps')
        
        # 5. Testimonials
        Testimonial.objects.all().delete()
        for t in [
            {'name': 'Sarah Johnson', 'role': 'CEO', 'company': 'TechStartup', 'quote': 'Amazing work!', 'rating': 5, 'order': 1},
            {'name': 'Michael Chen', 'role': 'Founder', 'company': 'InnovateLab', 'quote': 'Highly professional!', 'rating': 5, 'order': 2},
            {'name': 'Emily Davis', 'role': 'PM', 'company': 'GrowthCo', 'quote': 'Highly recommend!', 'rating': 5, 'order': 3},
            {'name': 'James Wilson', 'role': 'CTO', 'company': 'DataFlow', 'quote': 'Best team ever!', 'rating': 5, 'order': 4},
        ]:
            Testimonial.objects.create(**t)
        print('[OK] 4 Testimonials')
        
        # 6. Portfolio Categories
        PortfolioCategory.objects.all().delete()
        cat_ids = {}
        for name in ['Web Apps', 'Mobile', 'Branding', 'Cloud']:
            cat = PortfolioCategory.objects.create(name=name)
            cat_ids[name] = cat
        print('[OK] 4 Portfolio Categories')
        
        # 7. Portfolio Items
        PortfolioItem.objects.all().delete()
        for title, desc, cat_name in [
            ('Fintech Dashboard', 'Real-time analytics', 'Web Apps'),
            ('Health App', 'Health tracking', 'Mobile'),
            ('Lumos Identity', 'Complete rebrand', 'Branding'),
            ('E-commerce Platform', 'Online store', 'Web Apps'),
            ('SaaS Analytics', 'Business intelligence', 'Web Apps'),
            ('Fitness Pro', 'Workout app', 'Mobile'),
        ]:
            PortfolioItem.objects.create(
                title=title,
                description=desc,
                category=cat_ids[cat_name],
            )
        print('[OK] 6 Portfolio Items')
        
        # 8. Team
        TeamMember.objects.all().delete()
        for name, role, bio in [
            ('Alex Thompson', 'CEO', 'Visionary leader'),
            ('Maria Garcia', 'Creative Director', 'Award-winning designer'),
            ('John Smith', 'Lead Developer', 'Full-stack expert'),
            ('Lisa Wang', 'UX Strategist', 'UX specialist'),
        ]:
            TeamMember.objects.create(name=name, role=role, bio=bio)
        print('[OK] 4 Team Members')
        
        print('')
        print('======================================')
        print('All data seeded successfully!')
        print('======================================')
        print('Admin: http://127.0.0.1:8000/admin/')
        print('Login: admin / admin123')