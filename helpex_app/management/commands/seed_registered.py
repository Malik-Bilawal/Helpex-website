import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpex_project.settings')
django.setup()

from django.core.management.base import BaseCommand
from helpex_app.models import RegisteredCompany
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile


def generate_logo(width, height, bg_color, text_color, text):
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((width - tw) // 2, (height - th) // 2), text, fill=text_color, font=font)
    
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue())


class Command(BaseCommand):
    help = 'Seed registered companies data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding registered companies...')

        companies = [
            {'name': 'SECP Pakistan', 'description': 'Securities & Exchange Commission', 'color': '#1A5C3A'},
            {'name': 'FIA', 'description': 'Federal Investigation Agency', 'color': '#1E3A5F'},
            {'name': 'P@SHA', 'description': 'Pakistan Software Houses Association', 'color': '#2D5AA0'},
            {'name': 'NTN Registered', 'description': 'National Tax Number - FBR', 'color': '#0D4D3A'},
            {'name': 'Punjab IT Board', 'description': 'Punjab Information Technology Board', 'color': '#8B1A1A'},
            {'name': 'Ignite Pakistan', 'description': 'National Technology Fund', 'color': '#1A4D8B'},
            {'name': 'Ministry of IT', 'description': 'Ministry of IT & Telecom', 'color': '#2E4057'},
            {'name': 'PEC', 'description': 'Pakistan Engineering Council', 'color': '#4A3B8B'},
        ]

        for i, company in enumerate(companies):
            img_data = generate_logo(200, 100, (0, 0, 0, 0), company['color'], company['name'])
            RegisteredCompany.objects.update_or_create(
                name=company['name'],
                defaults={
                    'logo': ContentFile(img_data.read(), name=f'{company["name"].lower().replace(" ", "_")}.png'),
                    'description': company['description'],
                    'order': i,
                    'is_active': True,
                }
            )
            self.stdout.write(f'  - {company["name"]} [OK]')

        self.stdout.write('Done!')
