import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from helpex_app.models import WhyChooseUsSection, WhyChooseUsReason, WhyChooseUsStat

section, created = WhyChooseUsSection.objects.get_or_create(
    pk=1,
    defaults={
        'title': 'Why Choose Us',
        'subtitle': 'Discover what makes us the perfect partner for your digital success',
        'is_active': True
    }
)
print(f'Created section: {section.title}')

reasons_data = [
    {
        'title': 'Expert Team',
        'description': 'Our team of seasoned professionals brings years of industry experience and cutting-edge expertise to every project, ensuring top-tier results.',
        'icon_class': 'fa-users',
        'order': 1
    },
    {
        'title': 'Innovation First',
        'description': 'We stay ahead of the curve by leveraging the latest technologies and creative approaches to deliver solutions that set you apart from the competition.',
        'icon_class': 'fa-lightbulb',
        'order': 2
    },
    {
        'title': 'Proven Track Record',
        'description': 'With hundreds of successful projects and a 98% client satisfaction rate, our results speak for themselves.',
        'icon_class': 'fa-trophy',
        'order': 3
    },
    {
        'title': 'Transparent Communication',
        'description': 'We believe in complete transparency with regular updates, clear timelines, and open communication channels throughout your project.',
        'icon_class': 'fa-comments',
        'order': 4
    },
    {
        'title': 'Custom Solutions',
        'description': 'No cookie-cutter approaches here. Every solution is tailored to your unique business needs, goals, and target audience.',
        'icon_class': 'fa-puzzle-piece',
        'order': 5
    },
    {
        'title': 'Ongoing Support',
        'description': 'Our relationship doesn\'t end at launch. We provide comprehensive support and maintenance to ensure your continued success.',
        'icon_class': 'fa-headset',
        'order': 6
    }
]

created_count = 0
for reason_data in reasons_data:
    reason, created = WhyChooseUsReason.objects.get_or_create(
        title=reason_data['title'],
        defaults=reason_data
    )
    if created:
        created_count += 1
        print(f'Created reason: {reason.title}')

stats_data = [
    {
        'number': '180+',
        'label': 'Projects Completed',
        'icon_class': 'fa-briefcase',
        'order': 1
    },
    {
        'number': '98%',
        'label': 'Client Satisfaction',
        'icon_class': 'fa-smile',
        'order': 2
    },
    {
        'number': '50+',
        'label': 'Team Members',
        'icon_class': 'fa-users',
        'order': 3
    },
    {
        'number': '24/7',
        'label': 'Support Available',
        'icon_class': 'fa-clock',
        'order': 4
    }
]

for stat_data in stats_data:
    stat, created = WhyChooseUsStat.objects.get_or_create(
        label=stat_data['label'],
        defaults=stat_data
    )
    if created:
        print(f'Created stat: {stat.number} - {stat.label}')

print(f'\nSuccessfully seeded Why Choose Us data!')
