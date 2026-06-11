from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Service, Testimonial, ProcessStep, PortfolioItem, PortfolioCategory, TeamMember, SiteSettings, HeroSection, HeroCarouselItem, ContactMessage, Client, BlogPost, BlogCategory, GalleryImage, GalleryCategory, PricingPlan, WhyChooseUsSection, WhyChooseUsReason, WhyChooseUsStat, ProductCategory, Product, ProductFeature, ProductScreenshot


def index(request):
    hero = HeroSection.objects.filter(is_active=True).first()
    carousel_items = HeroCarouselItem.objects.filter(is_active=True).order_by('order', 'id')
    services = Service.objects.filter(is_active=True).order_by('order', 'title')[:6]
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order', 'name')[:3]
    portfolio_items = PortfolioItem.objects.filter(is_active=True).order_by('order', '-created_at')[:6]
    categories = PortfolioCategory.objects.all().order_by('order', 'name')
    process_steps = ProcessStep.objects.filter(is_active=True).order_by('order', 'step_number')
    clients = Client.objects.filter(is_active=True).order_by('order', 'name')[:8]
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/index.html', {
        'hero': hero,
        'carousel_items': carousel_items,
        'services': services,
        'testimonials': testimonials,
        'portfolio_items': portfolio_items,
        'categories': categories,
        'process_steps': process_steps,
        'clients': clients,
        'settings': settings,
    })


def service(request):
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/service.html', {
        'services': services,
        'settings': settings,
    })


def service_detail(request, slug):
    service = Service.objects.filter(slug=slug, is_active=True).first()
    if not service:
        from django.http import Http404
        raise Http404("Service not found")
    
    related_services = Service.objects.filter(is_active=True).exclude(slug=slug).order_by('order', 'title')[:3]
    case_studies = service.case_studies.filter(is_active=True).order_by('order', 'id')
    gallery_images = service.gallery_images.order_by('order', 'id')
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/service_detail.html', {
        'service': service,
        'related_services': related_services,
        'case_studies': case_studies,
        'gallery_images': gallery_images,
        'settings': settings,
    })


def about(request):
    # Get stats from hero section or use defaults
    hero = HeroSection.objects.filter(is_active=True).first()
    process_steps = ProcessStep.objects.filter(is_active=True).order_by('order', 'step_number')
    team_members = TeamMember.objects.filter(is_active=True).order_by('order', 'name')
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/about.html', {
        'hero': hero,
        'process_steps': process_steps,
        'team_members': team_members,
        'settings': settings,
    })


def contact(request):
    settings = SiteSettings.get_settings()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_type = request.POST.get('service', 'General Inquiry')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=service_type,
                message=message
            )
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    return render(request, 'helpex_app/contact.html', {
        'settings': settings,
    })


def clients(request):
    client_list = Client.objects.filter(is_active=True).order_by('order', 'name')
    featured_clients = Client.objects.filter(is_active=True, is_featured=True).order_by('order', 'name')
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order', 'name')[:3]
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/clients.html', {
        'clients': client_list,
        'featured_clients': featured_clients,
        'testimonials': testimonials,
        'settings': settings,
    })


def blog(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    featured_posts = BlogPost.objects.filter(is_published=True, is_featured=True).order_by('-created_at')[:3]
    categories = BlogCategory.objects.all().order_by('order', 'name')
    settings = SiteSettings.get_settings()
    
    response = render(request, 'helpex_app/blog.html', {
        'posts': posts,
        'featured_posts': featured_posts,
        'categories': categories,
        'settings': settings,
    })
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def gallery(request):
    images = GalleryImage.objects.filter(is_active=True).order_by('order', '-is_featured', '-created_at')
    categories = GalleryCategory.objects.filter(is_active=True).order_by('order', 'name')
    featured_images = GalleryImage.objects.filter(is_active=True, is_featured=True).order_by('order')[:5]
    total_count = images.count()
    settings = SiteSettings.get_settings()

    category_filter = request.GET.get('category')
    if category_filter and category_filter != 'all':
        images = images.filter(category__slug=category_filter)

    return render(request, 'helpex_app/gallery.html', {
        'images': images,
        'categories': categories,
        'featured_images': featured_images,
        'total_count': total_count,
        'settings': settings,
        'active_category': category_filter or 'all',
    })


def gallery_image_detail(request, slug):
    image = GalleryImage.objects.get(slug=slug, is_active=True)
    image.view_count += 1
    image.save(update_fields=['view_count'])

    related_images = GalleryImage.objects.filter(
        category=image.category,
        is_active=True
    ).exclude(id=image.id)[:4]

    settings = SiteSettings.get_settings()

    return render(request, 'helpex_app/gallery_detail.html', {
        'image': image,
        'related_images': related_images,
        'settings': settings,
    })


def profile(request):
    """User profile page"""
    settings = SiteSettings.get_settings()
    return render(request, 'helpex_app/profile.html', {
        'settings': settings,
    })


def pricing(request):
    """Pricing page with all plans"""
    plans = PricingPlan.objects.filter(is_active=True).order_by('order', 'name')
    monthly_plans = plans.filter(plan_type='monthly')
    yearly_plans = plans.filter(plan_type='yearly')
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/pricing.html', {
        'plans': plans,
        'monthly_plans': monthly_plans,
        'yearly_plans': yearly_plans,
        'settings': settings,
    })


def why_choose_us(request):
    """Why Choose Us page"""
    section = WhyChooseUsSection.objects.filter(is_active=True).first()
    reasons = WhyChooseUsReason.objects.filter(is_active=True).order_by('order', 'title')
    stats = WhyChooseUsStat.objects.filter(is_active=True).order_by('order')
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order', 'name')[:3]
    settings = SiteSettings.get_settings()
    process_steps = ProcessStep.objects.filter(is_active=True).order_by('order', 'step_number')
    
    return render(request, 'helpex_app/why_choose_us.html', {
        'section': section,
        'reasons': reasons,
        'stats': stats,
        'testimonials': testimonials,
        'settings': settings,
        'process_steps': process_steps,
    })


def reviews(request):
    """Client Reviews page - all reviews linked to clients and projects"""
    review_list = Testimonial.objects.filter(is_active=True).select_related('client', 'project').order_by('order', '-created_at')
    settings = SiteSettings.get_settings()

    client_filter = request.GET.get('client')
    project_filter = request.GET.get('project')

    if client_filter:
        review_list = review_list.filter(client__slug=client_filter)
    if project_filter:
        review_list = review_list.filter(project__slug=project_filter)

    clients = Client.objects.filter(is_active=True, reviews__is_active=True).distinct().order_by('name')
    projects = PortfolioItem.objects.filter(is_active=True, reviews__is_active=True).distinct().order_by('title')

    return render(request, 'helpex_app/reviews.html', {
        'reviews': review_list,
        'clients': clients,
        'projects': projects,
        'active_client': client_filter or '',
        'active_project': project_filter or '',
        'settings': settings,
    })


def products(request):
    """Products listing page"""
    products = Product.objects.filter(is_active=True).order_by('order', 'name')
    categories = ProductCategory.objects.filter(is_active=True).order_by('order', 'name')
    featured_products = Product.objects.filter(is_active=True, is_featured=True).order_by('order', 'name')
    settings = SiteSettings.get_settings()

    category_filter = request.GET.get('category')
    if category_filter and category_filter != 'all':
        products = products.filter(category__slug=category_filter)

    return render(request, 'helpex_app/products.html', {
        'products': products,
        'categories': categories,
        'featured_products': featured_products,
        'settings': settings,
        'active_category': category_filter or 'all',
    })


def product_detail(request, slug):
    """Product detail page"""
    from django.http import Http404
    product = Product.objects.filter(slug=slug, is_active=True).first()
    if not product:
        raise Http404("Product not found")

    related_products = Product.objects.filter(is_active=True).exclude(slug=slug).order_by('order', 'name')[:4]
    features = product.detailed_features.filter(is_active=True).order_by('order', 'title')
    screenshots = product.screenshot_images.filter(is_active=True).order_by('order', 'id')
    settings = SiteSettings.get_settings()

    return render(request, 'helpex_app/product_detail.html', {
        'product': product,
        'related_products': related_products,
        'features': features,
        'screenshots': screenshots,
        'settings': settings,
    })