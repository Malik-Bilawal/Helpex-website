from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Service, Testimonial, ProcessStep, PortfolioItem, PortfolioCategory, TeamMember, SiteSettings, HeroSection, ContactMessage


def index(request):
    hero = HeroSection.objects.filter(is_active=True).first()
    services = Service.objects.filter(is_active=True).order_by('order', 'title')[:6]
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order', 'name')[:3]
    portfolio_items = PortfolioItem.objects.filter(is_active=True).order_by('order', '-created_at')[:6]
    categories = PortfolioCategory.objects.all().order_by('order', 'name')
    process_steps = ProcessStep.objects.filter(is_active=True).order_by('order', 'step_number')
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/index.html', {
        'hero': hero,
        'services': services,
        'testimonials': testimonials,
        'portfolio_items': portfolio_items,
        'categories': categories,
        'process_steps': process_steps,
        'settings': settings,
    })


def service(request):
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    settings = SiteSettings.get_settings()
    
    return render(request, 'helpex_app/service.html', {
        'services': services,
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