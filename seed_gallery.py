from helpex_app.models import GalleryCategory, GalleryImage

# Create Categories
categories_data = [
    {'name': 'Web Design', 'slug': 'web-design', 'icon': 'fa-code', 'color': '#28A197', 'order': 1},
    {'name': 'Branding', 'slug': 'branding', 'icon': 'fa-palette', 'color': '#FF6B6B', 'order': 2},
    {'name': 'Mobile Apps', 'slug': 'mobile-apps', 'icon': 'fa-mobile-alt', 'color': '#4ECDC4', 'order': 3},
    {'name': 'Print Design', 'slug': 'print-design', 'icon': 'fa-print', 'color': '#45B7D1', 'order': 4},
    {'name': '3D Work', 'slug': '3d-work', 'icon': 'fa-cube', 'color': '#9B59B6', 'order': 5},
]

for cat_data in categories_data:
    cat, created = GalleryCategory.objects.get_or_create(slug=cat_data['slug'], defaults=cat_data)
    print(f'Category: {cat.name} - {"Created" if created else "Exists"}')

print(f'Total categories: {GalleryCategory.objects.count()}')

# Sample project titles and descriptions
projects = [
    {'title': 'E-Commerce Platform', 'cat': 'web-design', 'desc': 'Modern online store with seamless checkout experience'},
    {'title': 'Banking Dashboard', 'cat': 'web-design', 'desc': 'Financial analytics and management dashboard'},
    {'title': 'Restaurant Website', 'cat': 'web-design', 'desc': 'Elegant restaurant landing page with menu'},
    {'title': 'Tech Startup Landing', 'cat': 'web-design', 'desc': 'SaaS product landing page with dark theme'},
    {'title': 'Fitness App Interface', 'cat': 'mobile-apps', 'desc': 'Health tracking mobile application'},
    {'title': 'Social Media App', 'cat': 'mobile-apps', 'desc': 'Next-gen social networking platform'},
    {'title': 'Coffee Shop Branding', 'cat': 'branding', 'desc': 'Complete brand identity for artisan coffee'},
    {'title': 'Fashion Brand Identity', 'cat': 'branding', 'desc': 'Luxury fashion brand visual system'},
    {'title': 'Tech Conference Poster', 'cat': 'print', 'desc': 'Annual developer conference promotional materials'},
    {'title': 'Magazine Layout', 'cat': 'print', 'desc': 'Editorial design for lifestyle magazine'},
    {'title': 'Product Visualization', 'cat': '3d-work', 'desc': '3D rendered product showcase'},
    {'title': 'Architectural Render', 'cat': '3d-work', 'desc': 'Modern building 3D visualization'},
    {'title': 'Dashboard UI', 'cat': 'web-design', 'desc': 'Admin panel with analytics widgets'},
    {'title': 'Portfolio Website', 'cat': 'web-design', 'desc': 'Creative agency portfolio site'},
    {'title': 'Delivery App', 'cat': 'mobile-apps', 'desc': 'Food delivery mobile application'},
    {'title': 'Music Streaming', 'cat': 'mobile-apps', 'desc': 'Audio streaming platform design'},
]

aspect_ratios = ['landscape', 'portrait', 'square']
from django.utils import timezone
import random

# Get categories
web = GalleryCategory.objects.get(slug='web-design')
branding = GalleryCategory.objects.get(slug='branding')
mobile = GalleryCategory.objects.get(slug='mobile-apps')
printd = GalleryCategory.objects.get(slug='print-design')
d3 = GalleryCategory.objects.get(slug='3d-work')

category_map = {
    'web-design': web,
    'branding': branding,
    'mobile-apps': mobile,
    'print': printd,
    '3d-work': d3,
}

# Generate sample images (will use placeholder URLs)
from urllib.request import urlopen
from io import BytesIO
from PIL import Image
import os

def create_placeholder_image(title, index, aspect='landscape'):
    # Create a simple colored placeholder image
    colors = ['#28A197', '#1A1F3B', '#2D3555', '#3BC4B5', '#FF6B6B', '#4ECDC4', '#45B7D1', '#9B59B6']
    color = colors[index % len(colors)]

    # Create image based on aspect ratio
    if aspect == 'portrait':
        size = (600, 800)
    elif aspect == 'square':
        size = (600, 600)
    else:
        size = (800, 600)

    # Create PIL image
    img = Image.new('RGB', size, color)

    # Add text
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)

    # Save to BytesIO
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    buffer.seek(0)

    return buffer

created_count = 0
for i, proj in enumerate(projects):
    aspect = aspect_ratios[i % len(aspect_ratios)]
    cat = category_map.get(proj['cat'], web)

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
        view_count=random.randint(10, 500) if 'random' in dir() else 100,
    )

    # Save the image
    image.image.save(f'gallery_{i}.jpg', ContentFile(img_buffer.read()), save=True)

    created_count += 1
    print(f'Created image: {image.title}')

print(f'Total images created: {created_count}')
print('Done! Visit /gallery/ to see the results.')