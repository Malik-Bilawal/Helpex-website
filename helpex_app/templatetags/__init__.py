from django import template

register = template.Library()


@register.simple_tag
def get_hero():
    """Get active hero section"""
    from helpex_app.models import HeroSection
    try:
        return HeroSection.objects.filter(is_active=True).first()
    except HeroSection.DoesNotExist:
        return None


@register.simple_tag
def get_services():
    """Get all active services"""
    from helpex_app.models import Service
    return Service.objects.filter(is_active=True).order_by('order', 'title')


@register.simple_tag
def get_testimonials():
    """Get all active testimonials"""
    from helpex_app.models import Testimonial
    return Testimonial.objects.filter(is_active=True).order_by('order', 'name')


@register.simple_tag
def get_process_steps():
    """Get all active process steps"""
    from helpex_app.models import ProcessStep
    return ProcessStep.objects.filter(is_active=True).order_by('order', 'step_number')


@register.simple_tag
def get_portfolio_items():
    """Get all active portfolio items"""
    from helpex_app.models import PortfolioItem
    return PortfolioItem.objects.filter(is_active=True).order_by('order', '-created_at')


@register.simple_tag
def get_portfolio_categories():
    """Get all portfolio categories"""
    from helpex_app.models import PortfolioCategory
    return PortfolioCategory.objects.all().order_by('order', 'name')


@register.simple_tag
def get_team_members():
    """Get all active team members"""
    from helpex_app.models import TeamMember
    return TeamMember.objects.filter(is_active=True).order_by('order', 'name')


@register.simple_tag
def get_site_settings():
    """Get site settings"""
    from helpex_app.models import SiteSettings
    return SiteSettings.get_settings()


@register.inclusion_tag('helpex_app/partials/navbar.html')
def render_navbar():
    """Render the navbar with dynamic content"""
    return {'settings': get_site_settings()}


@register.inclusion_tag('helpex_app/partials/footer.html')
def render_footer():
    """Render the footer with dynamic content"""
    return {'settings': get_site_settings()}