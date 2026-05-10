from django.core.management.base import BaseCommand
from helpex_app.models import (
    HeroSection, Service, Testimonial, ProcessStep, PortfolioCategory, 
    PortfolioItem, TeamMember, Client, BlogCategory, BlogPost, 
    GalleryCategory, GalleryImage, SiteSettings, ContactMessage
)
from django.utils import timezone
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Seed all data for the HELPEX website'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.stdout.reconfigure(encoding='utf-8')
        
        self.seed_site_settings()
        self.seed_hero_section()
        self.seed_services()
        self.seed_testimonials()
        self.seed_process_steps()
        self.seed_portfolio()
        self.seed_team_members()
        self.seed_clients()
        self.seed_blog()
        self.seed_gallery()
        
        self.stdout.write(self.style.SUCCESS('All data seeded successfully!'))
    
    def seed_site_settings(self):
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        settings.company_name = "HELPEX BRO"
        settings.tagline = "Adaptive Digital Studio"
        settings.description = "Adaptive digital studio crafting exceptional digital experiences. We combine creative design, cutting-edge technology, and strategic thinking."
        settings.email = "hello@helpexbro.com"
        settings.phone = "+1 (555) 123-4567"
        settings.address = "123 Innovation Street, Tech City, TC 12345"
        settings.office_hours = "Mon-Fri: 9AM - 6PM"
        settings.social_twitter = "https://twitter.com"
        settings.social_instagram = "https://instagram.com"
        settings.social_linkedin = "https://linkedin.com"
        settings.social_dribbble = "https://dribbble.com"
        settings.social_github = "https://github.com"
        settings.primary_color = "#28A197"
        settings.secondary_color = "#1A1F3B"
        settings.meta_title = "HELPEX BRO - Adaptive Digital Studio"
        settings.meta_description = "Premium web apps, custom software, and iconic visual identities"
        settings.hero_tagline = "Innovating the Future"
        settings.hero_subtagline = "One Solution at a Time"
        settings.section_services_title = "Our Services"
        settings.section_testimonials_title = "What Our Clients Say"
        settings.section_process_title = "Our Working Process"
        settings.section_portfolio_title = "Our Portfolio"
        settings.section_team_title = "Our Team"
        settings.section_clients_title = "Our Clients"
        settings.section_blog_title = "Latest Insights"
        settings.section_gallery_title = "Our Gallery"
        settings.section_contact_title = "Get In Touch"
        settings.section_about_title = "About Us"
        settings.copyright_text = "HELPEX BRO. All rights reserved."
        settings.save()
        self.stdout.write(f'  [OK] Site Settings {"created" if created else "updated"}')
    
    def seed_hero_section(self):
        hero, created = HeroSection.objects.get_or_create(
            defaults={
                'title_line_1': 'Innovating the Future',
                'title_line_2': 'One Solution at a Time',
                'typing_texts': ['Web Development', 'App Design', 'Digital Marketing', 'AI Solutions'],
                'description': 'HELPEX is an adaptive digital studio crafting exceptional digital experiences. We combine creative design, cutting-edge technology, and strategic thinking to deliver transformative solutions that drive business growth and success.',
                'cta_button_text': 'Start Your Project',
                'cta_button_url': '/contact/',
                'secondary_cta_text': 'Watch Showreel',
                'secondary_cta_url': '#portfolio',
                'stats_label_1': 'Projects',
                'stats_number_1': '180+',
                'stats_label_2': 'Satisfaction',
                'stats_number_2': '98%',
                'stats_label_3': 'Team',
                'stats_number_3': '50+',
                'badge_text': 'ADAPTIVE DIGITAL STUDIO',
                'show_badge': True,
                'is_active': True
            }
        )
        if not created:
            hero.title_line_1 = 'Innovating the Future'
            hero.title_line_2 = 'One Solution at a Time'
            hero.typing_texts = ['Web Development', 'App Design', 'Digital Marketing', 'AI Solutions']
            hero.save()
        self.stdout.write(f'  [OK] Hero Section {"created" if created else "updated"}')
    
    def seed_services(self):
        services_data = [
            {
                'title': 'Web Development',
                'description': 'We build high-performance websites and web applications using modern technologies. From simple landing pages to complex enterprise solutions, we deliver scalable and secure web solutions that drive business growth.',
                'short_description': 'High-performance websites & web apps',
                'icon_class': 'fa-code',
                'tags': ['React', 'Django', 'Node.js', 'TypeScript'],
                'order': 1
            },
            {
                'title': 'Mobile App Development',
                'description': 'Create stunning, high-performance mobile applications for iOS and Android. We deliver native and cross-platform apps that provide seamless user experiences and help your business reach customers on any device.',
                'short_description': 'Native & cross-platform mobile apps',
                'icon_class': 'fa-mobile-alt',
                'tags': ['Flutter', 'React Native', 'Swift', 'Kotlin'],
                'order': 2
            },
            {
                'title': 'UI/UX Design',
                'description': 'Transform your ideas into beautiful, intuitive user interfaces. Our design team creates engaging experiences that not only look great but also drive user engagement and conversion rates.',
                'short_description': 'Beautiful, intuitive interfaces',
                'icon_class': 'fa-paint-brush',
                'tags': ['Figma', 'Adobe XD', 'Prototyping', 'User Research'],
                'order': 3
            },
            {
                'title': 'Digital Marketing',
                'description': 'Boost your online presence with our comprehensive digital marketing services. From SEO and social media to paid advertising, we help you reach and engage your target audience effectively.',
                'short_description': 'Grow your online presence',
                'icon_class': 'fa-bullhorn',
                'tags': ['SEO', 'Social Media', 'PPC', 'Content'],
                'order': 4
            },
            {
                'title': 'Software Solutions',
                'description': 'Custom software development tailored to your business needs. We build robust, scalable solutions that streamline operations, improve efficiency, and give you a competitive edge.',
                'short_description': 'Tailored software solutions',
                'icon_class': 'fa-cogs',
                'tags': ['Custom Dev', 'API Integration', 'Cloud', 'Security'],
                'order': 5
            },
            {
                'title': 'AI Solutions',
                'description': 'Leverage the power of artificial intelligence to transform your business. From machine learning models to intelligent automation, we help you implement cutting-edge AI solutions.',
                'short_description': 'Intelligent AI-powered solutions',
                'icon_class': 'fa-brain',
                'tags': ['Machine Learning', 'NLP', 'Automation', 'Chatbots'],
                'order': 6
            }
        ]
        
        for data in services_data:
            service, created = Service.objects.update_or_create(
                title=data['title'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(services_data)} Services')
    
    def seed_testimonials(self):
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'role': 'CEO',
                'company': 'TechStart Inc.',
                'quote': 'HELPEX transformed our digital presence. Their team delivered a stunning website that increased our conversions by 150%. Professional, responsive, and truly exceptional work.',
                'rating': 5,
                'order': 1
            },
            {
                'name': 'Michael Chen',
                'role': 'Product Manager',
                'company': 'InnovateTech',
                'quote': 'Working with HELPEX was incredible. They understood our vision perfectly and delivered a mobile app that exceeded our expectations. The attention to detail was outstanding.',
                'rating': 5,
                'order': 2
            },
            {
                'name': 'Emily Rodriguez',
                'role': 'Marketing Director',
                'company': 'GrowthBox',
                'quote': 'Our digital marketing campaign with HELPEX resulted in 300% growth in leads. Their strategic approach and creative content made all the difference. Highly recommended!',
                'rating': 5,
                'order': 3
            },
            {
                'name': 'David Kim',
                'role': 'Founder',
                'company': 'StartupHub',
                'quote': 'HELPEX built our entire platform from scratch. The quality of their code and design is exceptional. They are true partners in our success.',
                'rating': 5,
                'order': 4
            },
            {
                'name': 'Lisa Thompson',
                'role': 'CTO',
                'company': 'CloudScale',
                'quote': 'The AI solution HELPEX implemented revolutionized our operations. Their expertise in machine learning is unmatched. Fantastic team to work with.',
                'rating': 5,
                'order': 5
            }
        ]
        
        for data in testimonials_data:
            Testimonial.objects.update_or_create(
                name=data['name'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(testimonials_data)} Testimonials')
    
    def seed_process_steps(self):
        steps_data = [
            {
                'step_number': 1,
                'title': 'Discovery',
                'description': 'We start by understanding your business, goals, and challenges. Through detailed discussions and research, we gather all the information needed to create a tailored solution.',
                'icon_class': 'fa-search',
                'order': 1
            },
            {
                'step_number': 2,
                'title': 'Strategy',
                'description': 'Based on our findings, we develop a comprehensive strategy. This includes technical specifications, design concepts, timelines, and resource allocation to ensure project success.',
                'icon_class': 'fa-chess',
                'order': 2
            },
            {
                'step_number': 3,
                'title': 'Design',
                'description': 'Our creative team designs intuitive interfaces and visual elements that align with your brand. We create prototypes and iterate until the design perfectly matches your vision.',
                'icon_class': 'fa-palette',
                'order': 3
            },
            {
                'step_number': 4,
                'title': 'Development',
                'description': 'Our expert developers bring the designs to life using cutting-edge technologies. We follow best practices to ensure clean, maintainable, and scalable code.',
                'icon_class': 'fa-code',
                'order': 4
            },
            {
                'step_number': 5,
                'title': 'Testing',
                'description': 'Rigorous testing ensures everything works perfectly. We conduct unit tests, integration tests, and user acceptance testing to deliver a bug-free experience.',
                'icon_class': 'fa-vial',
                'order': 5
            },
            {
                'step_number': 6,
                'title': 'Launch',
                'description': 'We deploy your project to production with zero downtime. Post-launch, we provide ongoing support and maintenance to ensure continued success.',
                'icon_class': 'fa-rocket',
                'order': 6
            }
        ]
        
        for data in steps_data:
            ProcessStep.objects.update_or_create(
                step_number=data['step_number'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(steps_data)} Process Steps')
    
    def seed_portfolio(self):
        categories_data = [
            {'name': 'Web Development', 'slug': 'web-development', 'order': 1},
            {'name': 'Mobile Apps', 'slug': 'mobile-apps', 'order': 2},
            {'name': 'UI/UX Design', 'slug': 'ui-ux-design', 'order': 3},
            {'name': 'Branding', 'slug': 'branding', 'order': 4},
        ]
        
        categories = {}
        for data in categories_data:
            cat, _ = PortfolioCategory.objects.update_or_create(
                slug=data['slug'],
                defaults={'name': data['name'], 'order': data['order']}
            )
            categories[data['slug']] = cat
        
        portfolio_data = [
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'category': categories['web-development'],
                'description': 'A full-featured e-commerce platform with payment integration, inventory management, and analytics dashboard.',
                'client_name': 'ShopMax',
                'tags': ['E-commerce', 'Django', 'React', 'Stripe'],
                'order': 1
            },
            {
                'title': 'Fitness Tracking App',
                'slug': 'fitness-tracking-app',
                'category': categories['mobile-apps'],
                'description': 'Mobile app for tracking workouts, nutrition, and fitness goals with social features and wearable integration.',
                'client_name': 'FitLife',
                'tags': ['Mobile', 'Flutter', 'Health', 'Wearable'],
                'order': 2
            },
            {
                'title': 'Banking Dashboard',
                'slug': 'banking-dashboard',
                'category': categories['ui-ux-design'],
                'description': 'Modern banking dashboard with intuitive financial management tools and real-time transaction monitoring.',
                'client_name': 'SecureBank',
                'tags': ['Dashboard', 'Figma', 'FinTech', 'UX'],
                'order': 3
            },
            {
                'title': 'Brand Identity System',
                'slug': 'brand-identity-system',
                'category': categories['branding'],
                'description': 'Complete brand identity including logo, typography, color palette, and brand guidelines.',
                'client_name': 'GreenEnergy',
                'tags': ['Branding', 'Logo', 'Identity', 'Guidelines'],
                'order': 4
            },
            {
                'title': 'SaaS Dashboard',
                'slug': 'saas-dashboard',
                'category': categories['web-development'],
                'description': 'Analytics dashboard for SaaS businesses with real-time metrics, reporting, and team collaboration features.',
                'client_name': 'DataViz',
                'tags': ['SaaS', 'Analytics', 'React', 'D3.js'],
                'order': 5
            },
            {
                'title': 'Food Delivery App',
                'slug': 'food-delivery-app',
                'category': categories['mobile-apps'],
                'description': 'Full-featured food delivery app with real-time tracking, restaurant management, and payment integration.',
                'client_name': 'QuickEats',
                'tags': ['Delivery', 'Mobile', 'Flutter', 'GPS'],
                'order': 6
            }
        ]
        
        for data in portfolio_data:
            PortfolioItem.objects.update_or_create(
                slug=data['slug'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(portfolio_data)} Portfolio Items')
    
    def seed_team_members(self):
        team_data = [
            {
                'name': 'Alex Rivera',
                'role': 'CEO & Founder',
                'bio': 'Visionary leader with 15+ years in digital transformation. Passionate about building great products and great teams.',
                'email': 'alex@helpexbro.com',
                'order': 1
            },
            {
                'name': 'Jordan Smith',
                'role': 'Chief Technology Officer',
                'bio': 'Tech enthusiast specializing in scalable architectures and emerging technologies. Expert in AI/ML solutions.',
                'email': 'jordan@helpexbro.com',
                'order': 2
            },
            {
                'name': 'Sam Williams',
                'role': 'Creative Director',
                'bio': 'Award-winning designer with a passion for creating memorable digital experiences. Believes in design that connects.',
                'email': 'sam@helpexbro.com',
                'order': 3
            },
            {
                'name': 'Taylor Brown',
                'role': 'Head of Operations',
                'bio': 'Operations expert ensuring smooth project delivery. Focuses on efficiency and client satisfaction.',
                'email': 'taylor@helpexbro.com',
                'order': 4
            },
            {
                'name': 'Casey Miller',
                'role': 'Lead Developer',
                'bio': 'Full-stack developer passionate about clean code and innovative solutions. Expert in React and Python.',
                'email': 'casey@helpexbro.com',
                'order': 5
            },
            {
                'name': 'Morgan Lee',
                'role': 'Senior UX Designer',
                'bio': 'User-centered designer creating intuitive interfaces._specializes in research-driven design solutions.',
                'email': 'morgan@helpexbro.com',
                'order': 6
            }
        ]
        
        for data in team_data:
            TeamMember.objects.update_or_create(
                name=data['name'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(team_data)} Team Members')
    
    def seed_clients(self):
        clients_data = [
            {'name': 'TechStart Inc.', 'industry': 'Technology', 'is_featured': True, 'order': 1},
            {'name': 'InnovateTech', 'industry': 'Software', 'is_featured': True, 'order': 2},
            {'name': 'GrowthBox', 'industry': 'Marketing', 'is_featured': True, 'order': 3},
            {'name': 'StartupHub', 'industry': 'Startup', 'is_featured': False, 'order': 4},
            {'name': 'CloudScale', 'industry': 'Cloud Services', 'is_featured': True, 'order': 5},
            {'name': 'GreenEnergy', 'industry': 'Energy', 'is_featured': False, 'order': 6},
            {'name': 'SecureBank', 'industry': 'Finance', 'is_featured': True, 'order': 7},
            {'name': 'DataViz', 'industry': 'Analytics', 'is_featured': False, 'order': 8},
            {'name': 'ShopMax', 'industry': 'E-commerce', 'is_featured': True, 'order': 9},
            {'name': 'FitLife', 'industry': 'Health', 'is_featured': False, 'order': 10},
            {'name': 'QuickEats', 'industry': 'Food Tech', 'is_featured': False, 'order': 11},
            {'name': 'MediaPro', 'industry': 'Media', 'is_featured': False, 'order': 12},
        ]
        
        for data in clients_data:
            Client.objects.update_or_create(
                name=data['name'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(clients_data)} Clients')
    
    def seed_blog(self):
        categories_data = [
            {'name': 'Technology', 'slug': 'technology', 'description': 'Latest tech trends and insights', 'order': 1},
            {'name': 'Design', 'slug': 'design', 'description': 'UI/UX design tips and trends', 'order': 2},
            {'name': 'Marketing', 'slug': 'marketing', 'description': 'Digital marketing strategies', 'order': 3},
            {'name': 'Business', 'slug': 'business', 'description': 'Business growth and insights', 'order': 4},
        ]
        
        categories = {}
        for data in categories_data:
            cat, _ = BlogCategory.objects.update_or_create(
                slug=data['slug'],
                defaults={'name': data['name'], 'description': data['description'], 'order': data['order']}
            )
            categories[data['slug']] = cat
        
        posts_data = [
            {
                'title': 'The Future of AI in Web Development',
                'slug': 'future-of-ai-web-development',
                'category': categories['technology'],
                'excerpt': 'Explore how artificial intelligence is revolutionizing web development and what it means for the future of digital solutions.',
                'content': '''Artificial Intelligence is transforming web development in unprecedented ways. From intelligent code completion to automated testing, AI tools are becoming essential in the modern development workflow.

In this article, we explore the latest AI technologies and how they're reshaping how we build websites and web applications.

## Key AI Technologies in Web Development

### 1. Intelligent Code Assistance
AI-powered code completion tools are helping developers write better code faster. These tools analyze context and provide relevant suggestions.

### 2. Automated Testing
Machine learning algorithms can identify potential bugs and security vulnerabilities before they become issues.

### 3. Dynamic Content Generation
AI can generate personalized content based on user behavior and preferences.

## What This Means for Your Business

The integration of AI in web development leads to:
- Faster development cycles
- More reliable code
- Better user experiences
- Cost-effective solutions

Ready to leverage AI for your next project? Contact us today!''',
                'tags': ['AI', 'Web Development', 'Technology'],
                'is_published': True,
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Design Systems: The Key to Consistent UI',
                'slug': 'design-systems-consistent-ui',
                'category': categories['design'],
                'excerpt': 'Learn how implementing a design system can improve your product consistency and development efficiency.',
                'content': '''A design system is more than just a style guide. It's a comprehensive set of standards, documentation, and principles along with the tools to implement them.

## Why Design Systems Matter

### Consistency
Design systems ensure visual and functional consistency across all touchpoints.

### Efficiency
Developers can work faster with pre-built components and clear guidelines.

### Scalability
As your product grows, a design system makes it easier to maintain consistency.

## Key Components

1. **Design Tokens**: Colors, typography, spacing
2. **Components**: Reusable UI elements
3. **Patterns**: Common interaction patterns
4. **Documentation**: Usage guidelines

Start building your design system today!''',
                'tags': ['Design', 'UI/UX', 'Systems'],
                'is_published': True,
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'SEO Strategies for 2024',
                'slug': 'seo-strategies-2024',
                'category': categories['marketing'],
                'excerpt': 'Stay ahead of the curve with these essential SEO strategies for the coming year.',
                'content': '''Search engine optimization continues to evolve. Here's what you need to know for 2024.

## Core Ranking Factors

### 1. User Experience
Google prioritizes sites that provide excellent user experiences.

### 2. Content Quality
Quality content that truly helps users ranks higher than keyword-stuffed pages.

### 3. Mobile-First
With mobile-first indexing, your mobile site is what matters most.

## Technical SEO

- Site speed optimization
- Structured data implementation
- Core Web Vitals compliance

## Content Strategy

Focus on creating comprehensive, valuable content that answers user questions.

Let us help you improve your SEO!''',
                'tags': ['SEO', 'Marketing', 'Digital'],
                'is_published': True,
                'is_featured': False,
                'order': 3
            },
            {
                'title': 'Building a Successful Digital Product',
                'slug': 'building-successful-digital-product',
                'category': categories['business'],
                'excerpt': 'Insights from our experience building digital products for startups and enterprises.',
                'content': '''Creating a successful digital product requires more than just great code. It requires a strategic approach.

## The Product Development Lifecycle

### 1. Discovery
Understanding the problem and defining the solution.

### 2. Design
Creating intuitive user experiences.

### 3. Development
Building the actual product.

### 4. Launch
Getting the product to market.

### 5. Iterate
Continuous improvement based on feedback.

## Key Success Factors

1. **Clear Vision**: Know what you're building and why
2. **User-Centered Design**: Focus on user needs
3. **Agile Methodology**: Iterate and improve
4. **Quality Assurance**: Deliver reliable products

Ready to build your digital product? Let's talk!''',
                'tags': ['Product', 'Strategy', 'Business'],
                'is_published': True,
                'is_featured': True,
                'order': 4
            }
        ]
        
        for data in posts_data:
            BlogPost.objects.update_or_create(
                slug=data['slug'],
                defaults=data
            )
        self.stdout.write(f'  [OK] {len(posts_data)} Blog Posts')
    
    def seed_gallery(self):
        categories_data = [
            {'name': 'Web Design', 'slug': 'web-design', 'icon': 'fa-globe', 'color': '#28A197', 'order': 1},
            {'name': 'Mobile Apps', 'slug': 'mobile-apps', 'icon': 'fa-mobile', 'color': '#3BC4B5', 'order': 2},
            {'name': 'Branding', 'slug': 'branding', 'icon': 'fa-paint-brush', 'color': '#1A1F3B', 'order': 3},
            {'name': 'Marketing', 'slug': 'marketing', 'icon': 'fa-bullhorn', 'color': '#6366F1', 'order': 4},
        ]
        
        categories = {}
        for data in categories_data:
            cat, _ = GalleryCategory.objects.update_or_create(
                slug=data['slug'],
                defaults=data
            )
            categories[data['slug']] = cat
        
        images_data = [
            {'title': 'Modern Dashboard Design', 'category': categories['web-design'], 'aspect_ratio': 'landscape', 'is_featured': True},
            {'title': 'E-Commerce Mobile App', 'category': categories['mobile-apps'], 'aspect_ratio': 'portrait', 'is_featured': True},
            {'title': 'Brand Identity Showcase', 'category': categories['branding'], 'aspect_ratio': 'square', 'is_featured': False},
            {'title': 'Creative Landing Page', 'category': categories['web-design'], 'aspect_ratio': 'landscape', 'is_featured': True},
            {'title': 'App Interface Design', 'category': categories['mobile-apps'], 'aspect_ratio': 'portrait', 'is_featured': False},
            {'title': 'Logo Collection', 'category': categories['branding'], 'aspect_ratio': 'square', 'is_featured': True},
            {'title': 'Marketing Campaign Graphics', 'category': categories['marketing'], 'aspect_ratio': 'landscape', 'is_featured': False},
            {'title': 'SaaS Platform Design', 'category': categories['web-design'], 'aspect_ratio': 'landscape', 'is_featured': True},
            {'title': 'Fitness App Interface', 'category': categories['mobile-apps'], 'aspect_ratio': 'portrait', 'is_featured': False},
            {'title': 'Brand Guidelines PDF', 'category': categories['branding'], 'aspect_ratio': 'portrait', 'is_featured': False},
            {'title': 'Social Media Templates', 'category': categories['marketing'], 'aspect_ratio': 'square', 'is_featured': True},
            {'title': 'Portfolio Website', 'category': categories['web-design'], 'aspect_ratio': 'landscape', 'is_featured': False},
            {'title': 'Food Delivery UI', 'category': categories['mobile-apps'], 'aspect_ratio': 'portrait', 'is_featured': True},
            {'title': 'Corporate Identity', 'category': categories['branding'], 'aspect_ratio': 'square', 'is_featured': False},
            {'title': 'Email Campaign Design', 'category': categories['marketing'], 'aspect_ratio': 'landscape', 'is_featured': False},
            {'title': 'Analytics Dashboard', 'category': categories['web-design'], 'aspect_ratio': 'landscape', 'is_featured': True},
        ]
        
        for i, data in enumerate(images_data):
            GalleryImage.objects.update_or_create(
                title=data['title'],
                defaults={
                    'category': data['category'],
                    'description': f'Beautiful {data["category"].name.lower()} work - Project {i+1}',
                    'aspect_ratio': data['aspect_ratio'],
                    'is_featured': data['is_featured'],
                    'tags': [data['category'].name],
                    'order': i
                }
            )
        self.stdout.write(f'  [OK] {len(images_data)} Gallery Images')