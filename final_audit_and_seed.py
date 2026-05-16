import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from helpex_app.models import (
    HeroSection, Service, Testimonial, ProcessStep,
    PortfolioCategory, PortfolioItem, SiteSettings,
    ContactMessage, TeamMember, Client, BlogCategory, BlogPost,
    GalleryCategory, GalleryImage, PricingPlan, PricingFeature,
    WhyChooseUsSection, WhyChooseUsReason, WhyChooseUsStat
)

print("=" * 60)
print("FINAL PROJECT AUDIT & SEEDING")
print("=" * 60)

models = [
    (HeroSection, "Hero Section"),
    (Service, "Services"),
    (Testimonial, "Testimonials"),
    (ProcessStep, "Process Steps"),
    (PortfolioCategory, "Portfolio Categories"),
    (PortfolioItem, "Portfolio Items"),
    (SiteSettings, "Site Settings"),
    (TeamMember, "Team Members"),
    (Client, "Clients"),
    (BlogCategory, "Blog Categories"),
    (BlogPost, "Blog Posts"),
    (GalleryCategory, "Gallery Categories"),
    (GalleryImage, "Gallery Images"),
    (PricingPlan, "Pricing Plans"),
    (PricingFeature, "Pricing Features"),
    (WhyChooseUsSection, "Why Choose Us Section"),
    (WhyChooseUsReason, "Why Choose Us Reasons"),
    (WhyChooseUsStat, "Why Choose Us Stats"),
]

print("\n[DATA STATUS]")
print("-" * 60)
for model, name in models:
    count = model.objects.count()
    status = "[OK]" if count > 0 else "[MISSING]"
    print(f"{status} {name}: {count}")

print("\n\n[SEEDING MISSING DATA]")
print("-" * 60)

if not SiteSettings.objects.exists():
    SiteSettings.objects.create(
        company_name="HELPEX BRO",
        tagline="Adaptive Digital Studio",
        email="hello@helpex.com",
        phone="+1 234 567 8900",
        address="123 Innovation Drive, Tech City, TC 12345",
        primary_color="#28A197",
        secondary_color="#1A1F3B",
    )
    print("[OK] Site Settings created")
else:
    print("[OK] Site Settings exists")

if not HeroSection.objects.exists():
    HeroSection.objects.create(
        title_line_1="Innovating the Future",
        title_line_2="One Solution at a Time",
        typing_texts=["Web Development", "Mobile Apps", "UI/UX Design", "Digital Strategy"],
        description="HELPEX is an adaptive digital studio crafting exceptional digital experiences.",
        cta_button_text="Start Your Project",
        cta_button_url="/contact/",
        stats_label_1="Projects",
        stats_number_1="180+",
        stats_label_2="Satisfaction",
        stats_number_2="98%",
        stats_label_3="Team",
        stats_number_3="50+",
        badge_text="ADAPTIVE DIGITAL STUDIO",
        show_badge=True,
        is_active=True,
    )
    print("[OK] Hero Section created")
else:
    print("[OK] Hero Section exists")

if Service.objects.count() == 0:
    services_data = [
        {"title": "Web Development", "description": "Custom web applications built with modern technologies.", "icon_class": "fa-code", "order": 1},
        {"title": "Mobile Apps", "description": "Native and cross-platform mobile applications.", "icon_class": "fa-mobile-screen", "order": 2},
        {"title": "UI/UX Design", "description": "User-centered design that combines aesthetics with functionality.", "icon_class": "fa-palette", "order": 3},
        {"title": "Digital Marketing", "description": "Strategic campaigns that boost your online presence.", "icon_class": "fa-bullhorn", "order": 4},
        {"title": "Cloud Solutions", "description": "Scalable cloud infrastructure and migration services.", "icon_class": "fa-cloud", "order": 5},
        {"title": "Consulting", "description": "Expert guidance to align technology with business goals.", "icon_class": "fa-lightbulb", "order": 6},
    ]
    for data in services_data:
        Service.objects.create(**data, is_active=True)
    print("[OK] 6 Services created")
else:
    print(f"[OK] {Service.objects.count()} Services exist")

if Testimonial.objects.count() == 0:
    testimonials_data = [
        {"name": "Sarah Johnson", "role": "CEO", "company": "TechStart Inc", "quote": "HELPEX transformed our digital presence completely. Their team delivered beyond our expectations.", "rating": 5, "order": 1},
        {"name": "Michael Chen", "role": "Marketing Director", "company": "GrowthLabs", "quote": "The results speak for themselves. Our conversion rates increased by 150% after working with HELPEX.", "rating": 5, "order": 2},
        {"name": "Emily Rodriguez", "role": "Founder", "company": "CreativeHub", "quote": "Professional, innovative, and incredibly responsive. HELPEX is our go-to partner.", "rating": 5, "order": 3},
    ]
    for data in testimonials_data:
        Testimonial.objects.create(**data, is_active=True)
    print("[OK] 3 Testimonials created")
else:
    print(f"[OK] {Testimonial.objects.count()} Testimonials exist")

if ProcessStep.objects.count() == 0:
    process_data = [
        {"step_number": 1, "title": "Discovery", "description": "We dive deep into understanding your business and goals.", "icon_class": "fa-magnifying-glass", "order": 1},
        {"step_number": 2, "title": "Strategy", "description": "Crafting a comprehensive plan that aligns with your objectives.", "icon_class": "fa-chess", "order": 2},
        {"step_number": 3, "title": "Design", "description": "Creating stunning visuals and intuitive user experiences.", "icon_class": "fa-pen-ruler", "order": 3},
        {"step_number": 4, "title": "Development", "description": "Building robust solutions with cutting-edge technology.", "icon_class": "fa-code", "order": 4},
        {"step_number": 5, "title": "Launch", "description": "Deploying your project with thorough testing and optimization.", "icon_class": "fa-rocket", "order": 5},
    ]
    for data in process_data:
        ProcessStep.objects.create(**data, is_active=True)
    print("[OK] 5 Process Steps created")
else:
    print(f"[OK] {ProcessStep.objects.count()} Process Steps exist")

if TeamMember.objects.count() == 0:
    team_data = [
        {"name": "Alex Thompson", "role": "Founder & CEO", "bio": "Visionary leader with 15+ years in digital innovation.", "order": 1},
        {"name": "Maria Garcia", "role": "Creative Director", "bio": "Award-winning designer passionate about user experience.", "order": 2},
        {"name": "James Wilson", "role": "Lead Developer", "bio": "Full-stack expert specializing in scalable architectures.", "order": 3},
        {"name": "Sophia Lee", "role": "Marketing Head", "bio": "Strategic marketer driving growth through data-driven campaigns.", "order": 4},
    ]
    for data in team_data:
        TeamMember.objects.create(**data, is_active=True)
    print("[OK] 4 Team Members created")
else:
    print(f"[OK] {TeamMember.objects.count()} Team Members exist")

if Client.objects.count() == 0:
    clients_data = [
        {"name": "TechStart Inc", "industry": "Technology", "order": 1, "is_featured": True},
        {"name": "GrowthLabs", "industry": "Marketing", "order": 2, "is_featured": True},
        {"name": "CreativeHub", "industry": "Design", "order": 3, "is_featured": True},
        {"name": "DataFlow Systems", "industry": "Analytics", "order": 4, "is_featured": False},
        {"name": "EcoVentures", "industry": "Sustainability", "order": 5, "is_featured": False},
        {"name": "FinTech Pro", "industry": "Finance", "order": 6, "is_featured": True},
    ]
    for data in clients_data:
        Client.objects.create(**data, is_active=True)
    print("[OK] 6 Clients created")
else:
    print(f"[OK] {Client.objects.count()} Clients exist")

if BlogCategory.objects.count() == 0:
    categories_data = [
        {"name": "Technology", "description": "Latest tech trends and innovations", "order": 1},
        {"name": "Design", "description": "UI/UX insights and creative inspiration", "order": 2},
        {"name": "Marketing", "description": "Digital marketing strategies and tips", "order": 3},
        {"name": "Business", "description": "Business growth and entrepreneurship", "order": 4},
    ]
    for data in categories_data:
        BlogCategory.objects.create(**data)
    print("[OK] 4 Blog Categories created")
else:
    print(f"[OK] {BlogCategory.objects.count()} Blog Categories exist")

if BlogPost.objects.count() == 0:
    category = BlogCategory.objects.first()
    posts_data = [
        {"title": "The Future of Web Development in 2026", "excerpt": "Explore the cutting-edge technologies shaping the future.", "content": "Full article content here...", "author": "Alex Thompson", "is_published": True, "is_featured": True, "order": 1},
        {"title": "10 UI/UX Trends to Watch", "excerpt": "Stay ahead with these emerging design trends.", "content": "Full article content here...", "author": "Maria Garcia", "is_published": True, "is_featured": True, "order": 2},
        {"title": "How to Scale Your Startup", "excerpt": "Practical strategies for growing your business.", "content": "Full article content here...", "author": "James Wilson", "is_published": True, "is_featured": False, "order": 3},
    ]
    for data in posts_data:
        BlogPost.objects.create(**data, category=category)
    print("[OK] 3 Blog Posts created")
else:
    print(f"[OK] {BlogPost.objects.count()} Blog Posts exist")

if GalleryCategory.objects.count() == 0:
    gallery_cats = [
        {"name": "Projects", "description": "Our latest work", "icon": "fa-laptop-code", "color": "#28A197", "order": 1},
        {"name": "Office", "description": "Behind the scenes", "icon": "fa-building", "color": "#1A1F3B", "order": 2},
        {"name": "Events", "description": "Team events and conferences", "icon": "fa-calendar", "color": "#3BC4B5", "order": 3},
    ]
    for data in gallery_cats:
        GalleryCategory.objects.create(**data, is_active=True)
    print("[OK] 3 Gallery Categories created")
else:
    print(f"[OK] {GalleryCategory.objects.count()} Gallery Categories exist")

if PricingPlan.objects.count() == 0:
    plans_data = [
        {
            'name': 'Starter', 'description': 'Perfect for small projects',
            'plan_type': 'monthly', 'price': '299.00', 'currency': '$',
            'billing_period': '/month', 'popular_badge': 'none',
            'cta_text': 'Get Started', 'icon_class': 'fa-rocket', 'color_accent': '#28A197',
            'features': ['5 Pages Website', 'Responsive Design', 'Basic SEO', 'Contact Form', '1 Month Support']
        },
        {
            'name': 'Professional', 'description': 'Ideal for growing businesses',
            'plan_type': 'monthly', 'price': '599.00', 'currency': '$',
            'billing_period': '/month', 'popular_badge': 'popular',
            'cta_text': 'Start Now', 'icon_class': 'fa-star', 'color_accent': '#28A197',
            'features': ['15 Pages Website', 'Custom Design', 'Advanced SEO', 'CMS Integration', 'E-commerce Ready', '3 Months Support', 'Analytics Setup']
        },
        {
            'name': 'Enterprise', 'description': 'For large-scale solutions',
            'plan_type': 'monthly', 'price': '999.00', 'currency': '$',
            'billing_period': '/month', 'popular_badge': 'best_value',
            'cta_text': 'Contact Us', 'icon_class': 'fa-crown', 'color_accent': '#1A1F3B',
            'features': ['Unlimited Pages', 'Premium Design', 'Full SEO Suite', 'Custom Features', 'API Integration', 'Priority Support', 'Performance Optimization', 'Security Audit']
        }
    ]
    for plan_data in plans_data:
        features = plan_data.pop('features')
        plan = PricingPlan.objects.create(**plan_data, is_active=True)
        for i, feat in enumerate(features):
            PricingFeature.objects.create(plan=plan, text=feat, included=True, order=i)
    print("[OK] 3 Pricing Plans created")
else:
    print(f"[OK] {PricingPlan.objects.count()} Pricing Plans exist")

if not WhyChooseUsSection.objects.exists():
    WhyChooseUsSection.objects.create(
        title='Why Choose Us',
        subtitle='Discover what makes us the perfect partner',
        is_active=True
    )
    print("[OK] Why Choose Us Section created")
else:
    print("[OK] Why Choose Us Section exists")

if WhyChooseUsReason.objects.count() == 0:
    reasons_data = [
        {'title': 'Expert Team', 'description': 'Our team brings years of industry experience and cutting-edge expertise to every project.', 'icon_class': 'fa-users', 'order': 1},
        {'title': 'Innovation First', 'description': 'We leverage the latest technologies and creative approaches to deliver exceptional results.', 'icon_class': 'fa-lightbulb', 'order': 2},
        {'title': 'Proven Track Record', 'description': 'With hundreds of successful projects and a 98% client satisfaction rate.', 'icon_class': 'fa-trophy', 'order': 3},
        {'title': 'Transparent Communication', 'description': 'Complete transparency with regular updates and open communication channels.', 'icon_class': 'fa-comments', 'order': 4},
        {'title': 'Custom Solutions', 'description': 'Every solution is tailored to your unique business needs and goals.', 'icon_class': 'fa-puzzle-piece', 'order': 5},
        {'title': 'Ongoing Support', 'description': 'Comprehensive support and maintenance for continued success.', 'icon_class': 'fa-headset', 'order': 6},
    ]
    for data in reasons_data:
        WhyChooseUsReason.objects.create(**data, is_active=True)
    print("[OK] 6 Why Choose Us Reasons created")
else:
    print(f"[OK] {WhyChooseUsReason.objects.count()} Why Choose Us Reasons exist")

if WhyChooseUsStat.objects.count() == 0:
    stats_data = [
        {'number': '180+', 'label': 'Projects Completed', 'icon_class': 'fa-briefcase', 'order': 1},
        {'number': '98%', 'label': 'Client Satisfaction', 'icon_class': 'fa-smile', 'order': 2},
        {'number': '50+', 'label': 'Team Members', 'icon_class': 'fa-users', 'order': 3},
        {'number': '24/7', 'label': 'Support Available', 'icon_class': 'fa-clock', 'order': 4},
    ]
    for data in stats_data:
        WhyChooseUsStat.objects.create(**data, is_active=True)
    print("[OK] 4 Why Choose Us Stats created")
else:
    print(f"[OK] {WhyChooseUsStat.objects.count()} Why Choose Us Stats exist")

print("\n" + "=" * 60)
print("[AUDIT COMPLETE]")
print("=" * 60)

print("\n[FINAL DATA COUNT]")
print("-" * 60)
for model, name in models:
    count = model.objects.count()
    print(f"  {name}: {count}")

print("\n[PAGES AVAILABLE]")
print("  / - Home")
print("  /service/ - Services")
print("  /gallery/ - Gallery")
print("  /clients/ - Clients")
print("  /blog/ - Blog")
print("  /pricing/ - Pricing")
print("  /why-choose-us/ - Why Choose Us")
print("  /about/ - About Us")
print("  /contact/ - Contact")
print("  /admin/ - Admin Panel")
print("\n[ALL CONTENT IS FULLY DYNAMIC & MANAGEABLE VIA ADMIN]")
