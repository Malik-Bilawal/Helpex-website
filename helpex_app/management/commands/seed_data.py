from django.core.management.base import BaseCommand
from helpex_app.models import HeroSection, Service, Testimonial, ProcessStep, PortfolioCategory, PortfolioItem, SiteSettings, TeamMember, Client, BlogCategory, BlogPost


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
            title_line_1="Innovating the Future",
            title_line_2="One Solution at a Time",
            typing_texts=['digital experiences', 'web applications', 'software solutions'],
            description='HELPEX is an adaptive digital studio crafting exceptional digital experiences. We combine creative design, cutting-edge technology, and strategic thinking to deliver transformative solutions that drive business growth and success.',
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
        
        # 3. Services (from PDF: 6 core services)
        Service.objects.all().delete()
        services = [
            {'title': 'Web Development', 'short_description': 'Modern, responsive websites and web applications', 'description': 'Modern, responsive, and performant. From interactive frontends to robust backends, we build scalable web solutions using cutting-edge technologies.', 'icon_class': 'fa-code', 'tags': ['React', 'Vue', 'Next.js'], 'order': 1},
            {'title': 'App Development', 'short_description': 'Cross-platform mobile applications', 'description': 'Native and cross-platform mobile applications. We create intuitive, high-performance apps that engage users and drive business growth.', 'icon_class': 'fa-mobile-alt', 'tags': ['React Native', 'Flutter', 'iOS'], 'order': 2},
            {'title': 'Software Solutions', 'short_description': 'Custom SaaS and enterprise systems', 'description': 'Custom SaaS, automation, and enterprise systems. We design and develop scalable software solutions tailored to your unique business needs.', 'icon_class': 'fa-cogs', 'tags': ['SaaS', 'ERP', 'API'], 'order': 3},
            {'title': 'Digital Marketing', 'short_description': 'Strategic online presence', 'description': 'Strategic digital marketing services to boost your online visibility. SEO, content marketing, and paid advertising campaigns that deliver results.', 'icon_class': 'fa-bullhorn', 'tags': ['SEO', 'Content', 'Ads'], 'order': 4},
            {'title': 'UI/UX Design', 'short_description': 'User-centered design experiences', 'description': 'User-centered design that creates meaningful experiences. From research to prototyping, we craft interfaces that users love.', 'icon_class': 'fa-pencil-ruler', 'tags': ['Figma', 'Research', 'Prototyping'], 'order': 5},
            {'title': 'AI Solutions', 'short_description': 'Intelligent automation and insights', 'description': 'Intelligent automation and AI-powered insights. We integrate machine learning and AI into your workflows for smarter business decisions.', 'icon_class': 'fa-brain', 'tags': ['ML', 'LLM', 'Automation'], 'order': 6},
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
        
        # 9. Clients
        Client.objects.all().delete()
        for name, industry, featured in [
            ('TechCorp', 'Technology', True),
            ('InnovateLab', 'Fintech', True),
            ('GrowthStart', 'SaaS', True),
            ('DataFlow', 'Analytics', False),
            ('CloudNine', 'Cloud Services', False),
            ('SmartApp', 'Mobile', False),
            ('FinEdge', 'Finance', False),
            ('MediTech', 'Healthcare', False),
        ]:
            Client.objects.create(name=name, industry=industry, is_featured=featured)
        print('[OK] 8 Clients')
        
        # 10. Blog Categories
        BlogCategory.objects.all().delete()
        for name, desc in [
            ('Web Development', 'Tips and tutorials for web development'),
            ('Design', 'UI/UX design insights'),
            ('Business', 'Business and strategy advice'),
            ('Technology', 'Tech trends and updates'),
        ]:
            BlogCategory.objects.create(name=name, description=desc)
        print('[OK] 4 Blog Categories')
        
        # 11. Blog Posts
        BlogPost.objects.all().delete()
        cats = list(BlogCategory.objects.all())
        for i, (title, excerpt, content, featured) in enumerate([
            ('Getting Started with React in 2024', 'Learn the fundamentals of React and build your first app.', 'React continues to be one of the most popular JavaScript frameworks...', True),
            ('10 UI/UX Design Tips', 'Best practices for creating user-friendly interfaces.', 'Design can make or break your product. Here are 10 tips...', True),
            ('How to Choose the Right Tech Stack', 'A guide to selecting the best technology for your project.', 'Choosing a tech stack is one of the most important decisions...', False),
            ('The Future of AI in Web Development', 'How artificial intelligence is changing the way we build websites.', 'AI is revolutionizing web development in unprecedented ways...', False),
            ('Responsive Design Best Practices', 'Ensure your website looks great on all devices.', 'With so many devices and screen sizes, responsive design is essential...', False),
        ], 1):
            BlogPost.objects.create(
                title=title,
                excerpt=excerpt,
                content=content,
                category=cats[i % len(cats)] if cats else None,
                author='HELPEX Team',
                is_published=True,
                is_featured=featured,
                view_count=i * 50,
            )
        print('[OK] 5 Blog Posts')
        
        print('')
        print('======================================')
        print('All data seeded successfully!')
        print('======================================')
        print('Admin: http://127.0.0.1:8000/admin/')
        print('Login: admin / admin123')