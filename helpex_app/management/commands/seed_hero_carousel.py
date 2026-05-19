import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from django.core.management.base import BaseCommand
from helpex_app.models import HeroCarouselItem
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile


def generate_placeholder(width, height, bg_color, text_color, text):
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 64)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((width - tw) // 2, (height - th) // 2), text, fill=text_color, font=font)
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=90)
    return ContentFile(buffer.getvalue())


class Command(BaseCommand):
    help = 'Seed hero carousel items'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding hero carousel...')

        colors = [
            ('#1A1F3B', '#28A197'),
            ('#28A197', '#FFFFFF'),
            ('#2D3555', '#3BC4B5'),
            ('#1E837A', '#F7F9FA'),
            ('#1A1F3B', '#3BC4B5'),
            ('#2D3555', '#28A197'),
        ]

        for i in range(6):
            bg, text = colors[i % len(colors)]
            img_data = generate_placeholder(1920, 1080, bg, text, f'Slide {i + 1}')
            HeroCarouselItem.objects.update_or_create(
                order=i,
                defaults={
                    'media_type': 'image',
                    'image': ContentFile(img_data.read(), name=f'hero_slide_{i}.jpg'),
                    'is_active': True,
                }
            )
            self.stdout.write(f'  Slide {i + 1} [OK]')

        self.stdout.write('Done!')
