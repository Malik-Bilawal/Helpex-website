from datetime import date

from django.db.models import Avg, Min

from helpex_app.models import (
    Client, PortfolioItem, Product, RegisteredCompany, Service, ServiceCaseStudy, TeamMember, Testimonial,
)


def global_context(request):
    total_projects = ServiceCaseStudy.objects.filter(is_active=True).count()
    if not total_projects:
        total_projects = PortfolioItem.objects.filter(is_active=True).count()
    total_clients = Client.objects.filter(is_active=True).count()
    team_size = TeamMember.objects.filter(is_active=True).count()

    avg_rating = Testimonial.objects.filter(is_active=True).aggregate(avg=Avg('rating'))['avg']
    avg_satisfaction = int(avg_rating * 20) if avg_rating else 98

    earliest_project = PortfolioItem.objects.filter(is_active=True).aggregate(earliest=Min('created_at'))['earliest']
    if earliest_project:
        total_experience = date.today().year - earliest_project.year
        total_experience = max(total_experience, 1)
    else:
        total_experience = 3

    return {
        'nav_services': Service.objects.filter(is_active=True).order_by('order', 'title'),
        'registered_companies': RegisteredCompany.objects.filter(is_active=True).order_by('order', 'name'),
        'nav_products': Product.objects.filter(is_active=True).order_by('order', 'name'),
        'total_projects': total_projects or 0,
        'total_clients': total_clients or 0,
        'team_size': team_size or 0,
        'avg_satisfaction': avg_satisfaction,
        'total_experience': total_experience,
    }
