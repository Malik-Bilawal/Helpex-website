from django.core.management.base import BaseCommand
from helpex_app.models import GalleryCategory, GalleryImage
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import random


def create_placeholder_image(title, index, aspect='landscape'):
    colors = ['#28A197', '#1A1F3B', '#2D3555', '#3BC4B5', '#FF6B6B', '#4ECDC4', '#45B7D1', '#9B59B6']
    color = colors[index % len(colors)]

    if aspect == 'portrait':
        size = (600, 800)
    elif aspect == 'square':
        size = (600, 600)
    else:
        size = (800, 600)

    img = Image.new('RGB', size, color)
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    buffer.seek(0)
    return buffer


class Command(BaseCommand):
    help = 'Seed gallery with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding gallery data...')

        # Create Categories
        categories_data = [
            {'name': 'Web Design', 'slug': 'web-design', 'icon': 'fa-code', 'color': '#28A197', 'order': 1},
            {'name': 'Branding', 'slug': 'branding', 'icon': 'fa-palette', 'color': '#FF6B6B', 'order': 2},
            {'name': 'Mobile Apps', 'slug': 'mobile-apps', 'icon': 'fa-mobile-alt', 'color': '#4ECDC4', 'order': 3},
            {'name': 'Print Design', 'slug': 'print-design', 'icon': 'fa-print', 'color': '#45B7D1', 'order': 4},
            {'name': '3D Work', 'slug': '3d-work', 'icon': 'fa-cube', 'color': '#9B59B6', 'order': 5},
        ]

        category_map = {}
        for cat_data in categories_data:
            cat, created = GalleryCategory.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            category_map[cat_data['slug']] = cat
            status = 'Created' if created else 'Exists'
            self.stdout.write(f'  - Category: {cat.name} [{status}]')

        # Sample projects
        projects = [
            {'title': 'E-Commerce Platform', 'cat': 'web-design', 'desc': 'Modern online store with seamless checkout'},
            {'title': 'Banking Dashboard', 'cat': 'web-design', 'desc': 'Financial analytics and management'},
            {'title': 'Restaurant Website', 'cat': 'web-design', 'desc': 'Elegant restaurant landing page'},
            {'title': 'Tech Startup Landing', 'cat': 'web-design', 'desc': 'SaaS product landing page with dark theme'},
            {'title': 'Fitness App Interface', 'cat': 'mobile-apps', 'desc': 'Health tracking mobile application'},
            {'title': 'Social Media App', 'cat': 'mobile-apps', 'desc': 'Next-gen social networking platform'},
            {'title': 'Coffee Shop Branding', 'cat': 'branding', 'desc': 'Complete brand identity for artisan coffee'},
            {'title': 'Fashion Brand Identity', 'cat': 'branding', 'desc': 'Luxury fashion brand visual system'},
            {'title': 'Tech Conference Poster', 'cat': 'print-design', 'desc': 'Annual developer conference materials'},
            {'title': 'Magazine Layout', 'cat': 'print-design', 'desc': 'Editorial design for lifestyle magazine'},
            {'title': 'Product Visualization', 'cat': '3d-work', 'desc': '3D rendered product showcase'},
            {'title': 'Architectural Render', 'cat': '3d-work', 'desc': 'Modern building 3D visualization'},
            {'title': 'Dashboard UI', 'cat': 'web-design', 'desc': 'Admin panel with analytics widgets'},
            {'title': 'Portfolio Website', 'cat': 'web-design', 'desc': 'Creative agency portfolio site'},
            {'title': 'Delivery App', 'cat': 'mobile-apps', 'desc': 'Food delivery mobile application'},
            {'title': 'Music Streaming', 'cat': 'mobile-apps', 'desc': 'Audio streaming platform design'},
            {'title': 'Logo Design', 'cat': 'branding', 'desc': 'Modern minimalist logo design'},
            {'title': 'Business Cards', 'cat': 'print-design', 'desc': 'Premium business card design'},
            {'title': 'Product Mockup', 'cat': '3d-work', 'desc': '3D product packaging mockup'},
            {'title': 'Agency Website', 'cat': 'web-design', 'desc': 'Full service agency website'},
        ]

        aspect_ratios = ['landscape', 'portrait', 'square']

        for i, proj in enumerate(projects):
            aspect = aspect_ratios[i % len(aspect_ratios)]
            cat = category_map.get(proj['cat'])

            if not cat:
                continue

            # Check if exists
            if GalleryImage.objects.filter(title=proj['title']).exists():
                self.stdout.write(f'  - Image exists: {proj["title"]}')
                continue

            img_buffer = create_placeholder_image(proj['title'], i, aspect)

            image = GalleryImage(
                title=proj['title'],
                slug=proj['title'].lower().replace(' ', '-').replace('/', '-'),
                category=cat,
                description=proj['desc'],
                aspect_ratio=aspect,
                order=i + 1,
                is_active=True,
                is_featured=i < 5,
                view_count=random.randint(10, 500),
            )

            image.image.save(f'gallery_{i}.jpg', ContentFile(img_buffer.read()), save=True)

            self.stdout.write(f'  - Created: {image.title}')

        self.stdout.write(self.style.SUCCESS('\nGallery seeded successfully!'))
        self.stdout.write(f'Categories: {GalleryCategory.objects.count()}')
        self.stdout.write(f'Images: {GalleryImage.objects.count()}')