from helpex_app.models import Service, RegisteredCompany, Product


def global_context(request):
    return {
        'nav_services': Service.objects.filter(is_active=True).order_by('order', 'title'),
        'registered_companies': RegisteredCompany.objects.filter(is_active=True).order_by('order', 'name'),
        'nav_products': Product.objects.filter(is_active=True).order_by('order', 'name'),
    }
