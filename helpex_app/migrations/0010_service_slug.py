from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Service = apps.get_model('helpex_app', 'Service')
    for service in Service.objects.all():
        if not service.slug:
            service.slug = slugify(service.title)
            service.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('helpex_app', '0009_whychooseusreason_whychooseussection_whychooseusstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=120, blank=True),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
    ]
