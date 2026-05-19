import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from django.core.management.base import BaseCommand
from helpex_app.models import Service, ServiceImage, ServiceCaseStudy
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile


def generate_placeholder_image(width, height, bg_color, text_color, text, subtext=None):
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 48)
        small_font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    draw.text(((width - text_width) // 2, (height - text_height) // 2 - 20), text, fill=text_color, font=font)
    
    if subtext:
        sub_bbox = draw.textbbox((0, 0), subtext, font=small_font)
        sub_width = sub_bbox[2] - sub_bbox[0]
        draw.text(((width - sub_width) // 2, (height + text_height) // 2 + 10), subtext, fill=text_color, font=small_font)
    
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=90)
    return ContentFile(buffer.getvalue())


class Command(BaseCommand):
    help = 'Seed service detail pages with rich content and images'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding service detail data...')

        services_data = [
            {
                'title': 'Custom Software Development',
                'slug': 'custom-software',
                'short_description': 'Tailored software solutions built to streamline your operations and drive growth.',
                'description': '''We design and develop custom software solutions that perfectly align with your business processes. From enterprise resource planning systems to specialized industry applications, our team delivers robust, scalable, and maintainable software.

Our development process is transparent and collaborative. We work closely with your team to understand requirements, define architecture, and deliver incrementally so you see progress every step of the way.

Every solution we build is designed with scalability in mind, ensuring your software grows with your business. We use modern frameworks and best practices to ensure your investment lasts for years.''',
                'icon_class': 'fa-code',
                'tags': ['Python', 'Django', 'React', 'Node.js', 'AWS', 'Docker', 'PostgreSQL', 'REST APIs'],
                'features': [
                    {'title': 'Custom Architecture', 'description': 'Software designed specifically for your business workflows and requirements.', 'icon': 'fa-sitemap'},
                    {'title': 'Scalable Design', 'description': 'Built to handle growth from startup to enterprise-level operations.', 'icon': 'fa-expand'},
                    {'title': 'API Integration', 'description': 'Seamless connectivity with your existing tools and third-party services.', 'icon': 'fa-plug'},
                    {'title': 'Security First', 'description': 'Enterprise-grade security with encryption, authentication, and audit trails.', 'icon': 'fa-shield-halved'},
                    {'title': 'Cloud Native', 'description': 'Deployed on AWS, Azure, or GCP with auto-scaling and high availability.', 'icon': 'fa-cloud'},
                    {'title': 'Ongoing Support', 'description': 'Dedicated maintenance and support to keep your software running smoothly.', 'icon': 'fa-headset'},
                ],
                'process_steps': [
                    {'title': 'Requirements Analysis', 'description': 'Deep dive into your business needs, user stories, and technical requirements.'},
                    {'title': 'Architecture Design', 'description': 'System architecture, database design, and technology stack selection.'},
                    {'title': 'Agile Development', 'description': 'Iterative development with regular demos and feedback cycles.'},
                    {'title': 'Testing & Launch', 'description': 'Comprehensive QA, performance testing, and smooth deployment.'},
                ],
                'faqs': [
                    {'question': 'How long does custom software development take?', 'answer': 'Typically 8-16 weeks depending on complexity. We provide detailed timelines during the discovery phase.'},
                    {'question': 'Do you provide source code?', 'answer': 'Yes, you own 100% of the source code and intellectual property upon project completion.'},
                    {'question': 'Can you integrate with our existing systems?', 'answer': 'Absolutely. We specialize in integrating with legacy systems, CRMs, ERPs, and third-party APIs.'},
                    {'question': 'What technologies do you use?', 'answer': 'We use Python/Django, React, Node.js, and cloud platforms like AWS and Azure, choosing the best stack for your needs.'},
                ],
                'stats': [
                    {'value': '150+', 'label': 'Projects Delivered'},
                    {'value': '99.9%', 'label': 'Uptime SLA'},
                    {'value': '40%', 'label': 'Cost Reduction'},
                    {'value': '3x', 'label': 'Faster Delivery'},
                ],
                'timeline': '8-16 weeks',
                'starting_price': '$5,000',
                'support': '24/7 Premium',
                'is_featured': True,
            },
            {
                'title': 'Web & Mobile Development',
                'slug': 'web-mobile-dev',
                'short_description': 'Stunning websites and mobile apps that engage users and drive conversions.',
                'description': '''We create beautiful, high-performance websites and mobile applications that captivate your audience and deliver measurable results. From responsive corporate websites to complex web applications and native mobile apps.

Our team specializes in modern frameworks and progressive web app technologies, ensuring your digital presence works flawlessly across all devices and platforms.

Every project begins with user research and ends with rigorous testing to guarantee an exceptional user experience that keeps visitors coming back.''',
                'icon_class': 'fa-mobile-screen-button',
                'tags': ['React', 'Next.js', 'Flutter', 'React Native', 'Swift', 'Kotlin', 'Firebase', 'PWA'],
                'features': [
                    {'title': 'Responsive Design', 'description': 'Pixel-perfect layouts that look stunning on every device and screen size.', 'icon': 'fa-display'},
                    {'title': 'Performance Optimized', 'description': 'Lightning-fast load times with optimized assets and caching strategies.', 'icon': 'fa-gauge-high'},
                    {'title': 'Cross-Platform Apps', 'description': 'Native-quality apps for iOS and Android from a single codebase.', 'icon': 'fa-mobile'},
                    {'title': 'SEO Ready', 'description': 'Built-in SEO best practices to maximize your search engine visibility.', 'icon': 'fa-magnifying-glass'},
                    {'title': 'Analytics Integration', 'description': 'Track user behavior and conversions with integrated analytics dashboards.', 'icon': 'fa-chart-line'},
                    {'title': 'CMS Integration', 'description': 'Easy content management with headless CMS or traditional platforms.', 'icon': 'fa-pen-to-square'},
                ],
                'process_steps': [
                    {'title': 'UX Research', 'description': 'User interviews, competitor analysis, and persona development.'},
                    {'title': 'Wireframing & Design', 'description': 'Interactive prototypes and high-fidelity visual designs.'},
                    {'title': 'Development', 'description': 'Frontend and backend development with continuous integration.'},
                    {'title': 'Launch & Optimize', 'description': 'Deployment, A/B testing, and performance optimization.'},
                ],
                'faqs': [
                    {'question': 'Do you build native or cross-platform apps?', 'answer': 'We build both. For most projects, we recommend Flutter or React Native for cost-effective cross-platform development.'},
                    {'question': 'How do you handle app store submissions?', 'answer': 'We handle the entire submission process for both Apple App Store and Google Play Store.'},
                    {'question': 'Can you redesign our existing website?', 'answer': 'Yes, we specialize in website redesigns that improve UX, performance, and conversions.'},
                ],
                'stats': [
                    {'value': '200+', 'label': 'Websites Built'},
                    {'value': '50+', 'label': 'Mobile Apps'},
                    {'value': '95%', 'label': 'Client Retention'},
                    {'value': '2s', 'label': 'Avg Load Time'},
                ],
                'timeline': '6-12 weeks',
                'starting_price': '$3,000',
                'support': 'Business Hours',
                'is_featured': True,
            },
            {
                'title': 'Business Solutions',
                'slug': 'business-solutions',
                'short_description': 'Streamline operations with ERP, CRM, and workflow automation solutions.',
                'description': '''Transform your business operations with our comprehensive suite of business solutions. We implement and customize ERP systems, CRM platforms, and workflow automation tools that eliminate bottlenecks and boost productivity.

Our consultants work alongside your team to identify inefficiencies and design solutions that deliver immediate ROI. From inventory management to customer relationship tracking, we have the expertise to optimize every aspect of your business.

We partner with leading platforms and also build custom solutions when off-the-shelf products don't meet your unique requirements.''',
                'icon_class': 'fa-briefcase',
                'tags': ['ERP', 'CRM', 'Automation', 'Salesforce', 'SAP', 'Zoho', 'Power BI', 'Tableau'],
                'features': [
                    {'title': 'ERP Implementation', 'description': 'End-to-end ERP setup customized for your industry and workflows.', 'icon': 'fa-building'},
                    {'title': 'CRM Optimization', 'description': 'Maximize your CRM investment with custom pipelines and automation.', 'icon': 'fa-users'},
                    {'title': 'Workflow Automation', 'description': 'Eliminate manual tasks with intelligent process automation.', 'icon': 'fa-robot'},
                    {'title': 'Data Analytics', 'description': 'Turn raw data into actionable insights with custom dashboards.', 'icon': 'fa-chart-pie'},
                    {'title': 'Inventory Management', 'description': 'Real-time inventory tracking with automated reorder points.', 'icon': 'fa-boxes-stacked'},
                    {'title': 'Reporting Suite', 'description': 'Automated reports delivered to stakeholders on schedule.', 'icon': 'fa-file-lines'},
                ],
                'process_steps': [
                    {'title': 'Business Audit', 'description': 'Comprehensive analysis of current processes and pain points.'},
                    {'title': 'Solution Design', 'description': 'Custom solution architecture tailored to your operations.'},
                    {'title': 'Implementation', 'description': 'Phased rollout with data migration and team training.'},
                    {'title': 'Optimization', 'description': 'Continuous improvement based on usage data and feedback.'},
                ],
                'faqs': [
                    {'question': 'Which ERP systems do you work with?', 'answer': 'We work with SAP, Odoo, Microsoft Dynamics, and custom-built ERP solutions.'},
                    {'question': 'How long does implementation take?', 'answer': 'Typically 4-12 weeks depending on the scope and complexity of your operations.'},
                    {'question': 'Do you provide training?', 'answer': 'Yes, comprehensive training for all users and administrators is included.'},
                ],
                'stats': [
                    {'value': '80+', 'label': 'Businesses Served'},
                    {'value': '35%', 'label': 'Avg Efficiency Gain'},
                    {'value': '60%', 'label': 'Less Manual Work'},
                    {'value': 'ROI 6mo', 'label': 'Average Payback'},
                ],
                'timeline': '4-12 weeks',
                'starting_price': '$4,000',
                'support': 'Dedicated Manager',
                'is_featured': False,
            },
            {
                'title': 'AI Tools & Automation',
                'slug': 'ai-tools-automation',
                'short_description': 'Leverage artificial intelligence and machine learning to automate and innovate.',
                'description': '''Harness the power of artificial intelligence to transform your business operations. We develop custom AI models, implement machine learning pipelines, and deploy intelligent automation solutions that learn and improve over time.

From natural language processing for customer service to computer vision for quality control, our AI solutions deliver measurable results. We work with the latest frameworks including TensorFlow, PyTorch, and OpenAI APIs.

Our team stays at the cutting edge of AI research, ensuring your business benefits from the latest breakthroughs in machine learning and automation.''',
                'icon_class': 'fa-brain',
                'tags': ['Machine Learning', 'NLP', 'Computer Vision', 'TensorFlow', 'PyTorch', 'OpenAI', 'RPA', 'Chatbots'],
                'features': [
                    {'title': 'Custom ML Models', 'description': 'Machine learning models trained on your specific data and use cases.', 'icon': 'fa-microchip'},
                    {'title': 'Natural Language Processing', 'description': 'Text analysis, sentiment detection, and intelligent chatbots.', 'icon': 'fa-comments'},
                    {'title': 'Computer Vision', 'description': 'Image recognition, quality inspection, and visual search capabilities.', 'icon': 'fa-eye'},
                    {'title': 'Predictive Analytics', 'description': 'Forecast trends, demand, and customer behavior with AI.', 'icon': 'fa-crystal-ball'},
                    {'title': 'Process Automation', 'description': 'Intelligent RPA that handles complex decision-making tasks.', 'icon': 'fa-gears'},
                    {'title': 'AI Consulting', 'description': 'Strategic guidance on AI adoption and implementation roadmap.', 'icon': 'fa-lightbulb'},
                ],
                'process_steps': [
                    {'title': 'AI Assessment', 'description': 'Identify high-impact AI opportunities in your business.'},
                    {'title': 'Data Preparation', 'description': 'Clean, label, and prepare data for model training.'},
                    {'title': 'Model Development', 'description': 'Build, train, and validate AI models for your use case.'},
                    {'title': 'Deployment & Monitor', 'description': 'Production deployment with continuous model monitoring.'},
                ],
                'faqs': [
                    {'question': 'Do we need a lot of data for AI?', 'answer': 'It depends on the use case. We can work with existing data or help you collect and label new data.'},
                    {'question': 'How accurate are AI models?', 'answer': 'Accuracy depends on data quality and use case. We typically achieve 85-98% accuracy for well-defined problems.'},
                    {'question': 'Can AI integrate with our current systems?', 'answer': 'Yes, AI models are deployed as APIs that integrate seamlessly with existing applications.'},
                ],
                'stats': [
                    {'value': '25+', 'label': 'AI Projects'},
                    {'value': '90%+', 'label': 'Model Accuracy'},
                    {'value': '70%', 'label': 'Time Saved'},
                    {'value': '5x', 'label': 'ROI Average'},
                ],
                'timeline': '6-14 weeks',
                'starting_price': '$8,000',
                'support': 'AI Specialist',
                'is_featured': True,
            },
            {
                'title': 'SaaS Products',
                'slug': 'saas-products',
                'short_description': 'Build, launch, and scale subscription-based software products.',
                'description': '''Launch your own SaaS product with our end-to-end development service. We handle everything from product strategy and MVP development to scaling infrastructure and monetization features.

Our SaaS expertise includes multi-tenant architecture, subscription billing, user onboarding flows, analytics dashboards, and everything needed to run a successful software-as-a-service business.

We've helped startups and enterprises alike launch profitable SaaS products that generate recurring revenue and delight customers.''',
                'icon_class': 'fa-cloud-arrow-up',
                'tags': ['SaaS', 'Multi-tenant', 'Stripe', 'Subscription', 'Microservices', 'Kubernetes', 'CI/CD', 'Analytics'],
                'features': [
                    {'title': 'Multi-tenant Architecture', 'description': 'Secure, isolated environments for each customer on shared infrastructure.', 'icon': 'fa-server'},
                    {'title': 'Subscription Billing', 'description': 'Integrated payment processing with Stripe, PayPal, or custom solutions.', 'icon': 'fa-credit-card'},
                    {'title': 'User Onboarding', 'description': 'Frictionless signup, trial management, and guided product tours.', 'icon': 'fa-user-plus'},
                    {'title': 'Analytics Dashboard', 'description': 'Real-time metrics, usage analytics, and customer insights.', 'icon': 'fa-chart-bar'},
                    {'title': 'Auto-scaling', 'description': 'Infrastructure that automatically scales with your user base.', 'icon': 'fa-arrows-up-down'},
                    {'title': 'Churn Reduction', 'description': 'Features and strategies to maximize customer retention.', 'icon': 'fa-heart-pulse'},
                ],
                'process_steps': [
                    {'title': 'Product Strategy', 'description': 'Market research, competitive analysis, and feature prioritization.'},
                    {'title': 'MVP Development', 'description': 'Build a minimum viable product to validate your concept quickly.'},
                    {'title': 'Scale & Iterate', 'description': 'Add features, optimize performance, and grow your user base.'},
                    {'title': 'Growth Optimization', 'description': 'A/B testing, conversion optimization, and retention strategies.'},
                ],
                'faqs': [
                    {'question': 'How much does it cost to build a SaaS product?', 'answer': 'MVP development typically starts at $10,000. Full-featured products range from $25,000 to $100,000+.'},
                    {'question': 'How long until launch?', 'answer': 'An MVP can be ready in 8-12 weeks. Full product launches typically take 4-6 months.'},
                    {'question': 'Do you handle hosting and infrastructure?', 'answer': 'Yes, we set up and manage cloud infrastructure on AWS, GCP, or Azure.'},
                ],
                'stats': [
                    {'value': '15+', 'label': 'SaaS Launched'},
                    {'value': '$2M+', 'label': 'Revenue Generated'},
                    {'value': '99.99%', 'label': 'Uptime'},
                    {'value': '10K+', 'label': 'Users Supported'},
                ],
                'timeline': '8-20 weeks',
                'starting_price': '$10,000',
                'support': 'Full Management',
                'is_featured': True,
            },
            {
                'title': 'Digital Marketing',
                'slug': 'digital-marketing',
                'short_description': 'Data-driven marketing strategies that amplify your brand and drive growth.',
                'description': '''Supercharge your digital presence with our comprehensive marketing services. From SEO and content marketing to paid advertising and social media management, we create strategies that deliver measurable results.

Our data-driven approach means every decision is backed by analytics. We track, measure, and optimize every campaign to maximize your return on investment and minimize wasted spend.

Whether you're a startup looking for your first customers or an established brand seeking growth, our marketing team has the expertise to take you to the next level.''',
                'icon_class': 'fa-bullhorn',
                'tags': ['SEO', 'Google Ads', 'Social Media', 'Content Marketing', 'Email Marketing', 'Analytics', 'CRO', 'PPC'],
                'features': [
                    {'title': 'SEO Optimization', 'description': 'Rank higher on Google with technical SEO, content strategy, and link building.', 'icon': 'fa-trophy'},
                    {'title': 'Paid Advertising', 'description': 'Targeted Google Ads, Facebook Ads, and LinkedIn campaigns.', 'icon': 'fa-ad'},
                    {'title': 'Content Strategy', 'description': 'Engaging content that attracts, educates, and converts your audience.', 'icon': 'fa-pen-nib'},
                    {'title': 'Social Media', 'description': 'Strategic social media management that builds community and drives engagement.', 'icon': 'fa-share-nodes'},
                    {'title': 'Email Marketing', 'description': 'Automated email sequences that nurture leads and drive conversions.', 'icon': 'fa-envelope'},
                    {'title': 'Conversion Optimization', 'description': 'A/B testing and UX improvements that turn visitors into customers.', 'icon': 'fa-percent'},
                ],
                'process_steps': [
                    {'title': 'Audit & Research', 'description': 'Comprehensive analysis of your current digital presence and competitors.'},
                    {'title': 'Strategy Development', 'description': 'Custom marketing plan aligned with your business goals and budget.'},
                    {'title': 'Campaign Execution', 'description': 'Launch and manage campaigns across selected channels.'},
                    {'title': 'Measure & Optimize', 'description': 'Continuous optimization based on performance data and ROI.'},
                ],
                'faqs': [
                    {'question': 'How quickly will I see results?', 'answer': 'PPC campaigns show results immediately. SEO typically takes 3-6 months for significant improvements.'},
                    {'question': 'What is your pricing model?', 'answer': 'We offer monthly retainers, project-based pricing, and performance-based options.'},
                    {'question': 'Do you provide reporting?', 'answer': 'Yes, detailed monthly reports with KPIs, insights, and recommendations.'},
                ],
                'stats': [
                    {'value': '300%', 'label': 'Avg ROI Increase'},
                    {'value': '50+', 'label': 'Active Campaigns'},
                    {'value': '2M+', 'label': 'Ad Spend Managed'},
                    {'value': '150%', 'label': 'Traffic Growth'},
                ],
                'timeline': 'Ongoing',
                'starting_price': '$1,500/mo',
                'support': 'Dedicated Team',
                'is_featured': False,
            },
        ]

        created_count = 0
        for data in services_data:
            service, created = Service.objects.update_or_create(
                slug=data['slug'],
                defaults=data
            )
            if created:
                self.stdout.write(f'  - Service: {service.title} [Created]')
            else:
                self.stdout.write(f'  - Service: {service.title} [Updated]')
            created_count += 1

            # Generate hero image if not exists
            if not service.hero_image:
                colors = [
                    ('#1A1F3B', '#28A197'),
                    ('#2D3555', '#3BC4B5'),
                    ('#1E837A', '#F7F9FA'),
                    ('#1A1F3B', '#64748B'),
                    ('#28A197', '#FFFFFF'),
                    ('#2D3555', '#28A197'),
                ]
                color_idx = created_count % len(colors)
                bg, text = colors[color_idx]
                
                img_data = generate_placeholder_image(
                    1200, 600, bg, text,
                    service.title,
                    service.short_description[:50] + '...'
                )
                service.hero_image.save(f'{service.slug}_hero.jpg', img_data, save=True)
                self.stdout.write(f'    Hero image generated')

            # Generate banner image if not exists
            if not service.banner_image:
                colors = [
                    ('#F7F9FA', '#1A1F3B'),
                    ('#28A197', '#FFFFFF'),
                    ('#1A1F3B', '#3BC4B5'),
                    ('#2D3555', '#28A197'),
                    ('#FFFFFF', '#1E837A'),
                    ('#1E837A', '#F7F9FA'),
                ]
                color_idx = created_count % len(colors)
                bg, text = colors[color_idx]
                
                img_data = generate_placeholder_image(
                    1200, 400, bg, text,
                    f'{service.title}',
                    'Transform Your Business'
                )
                service.banner_image.save(f'{service.slug}_banner.jpg', img_data, save=True)
                self.stdout.write(f'    Banner image generated')

            # Generate gallery images
            existing_gallery = service.gallery_images.count()
            if existing_gallery == 0:
                gallery_colors = [
                    ('#1A1F3B', '#28A197'),
                    ('#28A197', '#FFFFFF'),
                    ('#2D3555', '#3BC4B5'),
                    ('#FFFFFF', '#1A1F3B'),
                ]
                for i in range(4):
                    bg, text = gallery_colors[i % len(gallery_colors)]
                    img_data = generate_placeholder_image(
                        800, 600, bg, text,
                        f'{service.title}',
                        f'Project Showcase {i+1}'
                    )
                    ServiceImage.objects.create(
                        service=service,
                        title=f'{service.title} - Showcase {i+1}',
                        image=ContentFile(img_data.read(), name=f'{service.slug}_gallery_{i}.jpg'),
                        caption=f'Example of our {service.title.lower()} work',
                        order=i,
                        is_featured=(i == 0)
                    )
                self.stdout.write(f'    4 gallery images created')

            # Generate case studies
            existing_cases = service.case_studies.count()
            if existing_cases == 0:
                case_colors = [
                    ('#28A197', '#FFFFFF'),
                    ('#1A1F3B', '#3BC4B5'),
                    ('#2D3555', '#28A197'),
                ]
                case_titles = [
                    f'{service.title} - Success Story',
                    f'{service.title} - Client Transformation',
                    f'{service.title} - Enterprise Scale',
                ]
                case_results = [
                    '200% increase in efficiency',
                    'Reduced costs by 45%',
                    '3x faster time to market',
                ]
                for i in range(3):
                    bg, text = case_colors[i % len(case_colors)]
                    img_data = generate_placeholder_image(
                        800, 500, bg, text,
                        f'Case Study {i+1}',
                        case_results[i]
                    )
                    ServiceCaseStudy.objects.create(
                        service=service,
                        title=case_titles[i],
                        description=f'Detailed case study showing how we delivered exceptional results with {service.title.lower()} for a leading client in their industry.',
                        image=ContentFile(img_data.read(), name=f'{service.slug}_case_{i}.jpg'),
                        client=f'Client {i+1}',
                        result=case_results[i],
                        order=i,
                        is_active=True
                    )
                self.stdout.write(f'    3 case studies created')

        self.stdout.write(f'\nService details seeded successfully!')
        self.stdout.write(f'Services: {created_count}')
