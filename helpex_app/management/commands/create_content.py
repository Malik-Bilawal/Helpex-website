from django.core.management.base import BaseCommand
from helpex_app.models import HeroSection, Service, Testimonial, ProcessStep, SiteSettings


class Command(BaseCommand):
    help = 'Creates sample content for the website'

    def handle(self, *args, **options):
        # Create SiteSettings
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        if created:
            self.stdout.write(self.style.SUCCESS('Created Site Settings'))
        
        # Create Hero Section
        hero, created = HeroSection.objects.get_or_create(
            title_line_1="We craft",
            defaults={
                'title_line_2': 'experiences',
                'typing_texts': ['digital experiences', 'web applications', 'software solutions'],
                'description': 'HELPEX delivers premium web applications, custom software solutions, and iconic visual identities that transform businesses worldwide.',
                'cta_button_text': 'Start Your Project',
                'cta_button_url': '/contact/',
                'secondary_cta_text': 'Watch Showreel',
                'secondary_cta_url': '#portfolio',
                'stats_number_1': '180+',
                'stats_label_1': 'Projects',
                'stats_number_2': '98%',
                'stats_label_2': 'Satisfaction',
                'stats_number_3': '50+',
                'stats_label_3': 'Team',
                'badge_text': 'ADAPTIVE DIGITAL STUDIO',
                'show_badge': True,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Hero Section'))
        
        # Create Services
        services_data = [
            {'title': 'Web Development', 'short_description': 'Modern, responsive, and performant websites', 'description': 'Modern, responsive, and performant. From interactive frontends to robust backends.', 'icon_class': 'fa-code', 'tags': ['React', 'Vue', 'Next.js'], 'order': 1},
            {'title': 'Software Solutions', 'short_description': 'Custom SaaS and enterprise systems', 'description': 'Custom SaaS, automation, and enterprise systems. Scalable and secure.', 'icon_class': 'fa-cogs', 'tags': ['SaaS', 'ERP', 'API'], 'order': 2},
            {'title': 'Brand & Design', 'short_description': 'Visual identities and brand systems', 'description': 'Visual identities, brand systems, UI/UX. Memorable and human-centric.', 'icon_class': 'fa-palette', 'tags': ['Logo', 'UI/UX', 'Brand'], 'order': 3},
            {'title': 'Mobile Apps', 'short_description': 'Cross-platform mobile applications', 'description': 'End-to-end UX research and interface design. Intuitive and delightful.', 'icon_class': 'fa-mobile-alt', 'tags': ['iOS', 'Android', 'Flutter'], 'order': 4},
            {'title': 'Cloud & DevOps', 'short_description': 'Scalable infrastructure', 'description': 'Scalable infrastructure, CI/CD, cloud migration. Reliable deployments.', 'icon_class': 'fa-cloud', 'tags': ['AWS', 'Azure', 'K8s'], 'order': 5},
            {'title': 'AI & Automation', 'short_description': 'Smart workflows and AI', 'description': 'Integrate AI. Chatbots, predictive analytics, smart workflows.', 'icon_class': 'fa-brain', 'tags': ['ML', 'LLM', 'RPA'], 'order': 6},
        ]
        
        for svc in services_data:
            Service.objects.get_or_create(title=svc['title'], defaults=svc)
        self.stdout.write(self.style.SUCCESS(f'Created {len(services_data)} Services'))
        
        # Create Testimonials
        testimonials_data = [
            {'name': 'Sarah Johnson', 'role': 'CEO', 'company': 'TechStartup Inc', 'quote': 'HELPEX transformed our vision into reality. Their team delivered beyond our expectations.', 'rating': 5, 'order': 1},
            {'name': 'Michael Chen', 'role': 'Founder', 'company': 'InnovateLab', 'quote': 'Professional, creative, and highly skilled. We continue to partner with HELPEX.', 'rating': 5, 'order': 2},
            {'name': 'Emily Davis', 'role': 'Product Manager', 'company': 'GrowthCo', 'quote': 'Outstanding results and communication throughout the project. Highly recommend!', 'rating': 5, 'order': 3},
        ]
        
        for testimonial in testimonials_data:
            Testimonial.objects.get_or_create(name=testimonial['name'], defaults=testimonial)
        self.stdout.write(self.style.SUCCESS(f'Created {len(testimonials_data)} Testimonials'))
        
        # Create Process Steps
        process_data = [
            {'step_number': 1, 'title': 'Discovery', 'description': 'We dive deep into your business goals and challenges.', 'icon_class': 'fa-lightbulb', 'order': 1},
            {'step_number': 2, 'title': 'Strategy', 'description': 'We craft a tailored roadmap with wireframes.', 'icon_class': 'fa-chess', 'order': 2},
            {'step_number': 3, 'title': 'Development', 'description': 'Agile sprints with transparent communication.', 'icon_class': 'fa-code', 'order': 3},
            {'step_number': 4, 'title': 'Launch', 'description': 'We deploy and support your product 24/7.', 'icon_class': 'fa-rocket', 'order': 4},
        ]
        
        for step in process_data:
            ProcessStep.objects.get_or_create(step_number=step['step_number'], defaults=step)
        self.stdout.write(self.style.SUCCESS(f'Created {len(process_data)} Process Steps'))
        
        self.stdout.write(self.style.SUCCESS('Sample content created successfully!'))