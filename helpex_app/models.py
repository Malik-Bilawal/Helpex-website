from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class HeroCarouselItem(models.Model):
    """Minimal carousel items for homepage hero - images/videos only"""
    MEDIA_CHOICES = [('image', 'Image'), ('video', 'Video')]
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default='image')
    image = models.ImageField(upload_to='hero/carousel/', blank=True, null=True)
    video = models.FileField(upload_to='hero/carousel/', blank=True, null=True, help_text="MP4/WebM video file")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Hero Carousel Item"
        verbose_name_plural = "Hero Carousel Items"

    def __str__(self):
        return f"{'Video' if self.media_type == 'video' else 'Image'} #{self.order}"

    def save(self, *args, **kwargs):
        if self.video and not self.image:
            self.media_type = 'video'
        elif self.image and not self.video:
            self.media_type = 'image'
        super().save(*args, **kwargs)


class HeroSection(models.Model):
    """Hero section for the homepage"""
    title_line_1 = models.CharField(max_length=100, default="Innovating the Future")
    title_line_2 = models.CharField(max_length=100, default="One Solution at a Time")
    typing_texts = models.JSONField(default=list, blank=True, help_text="Array of animated texts")
    description = models.TextField(default="HELPEX is an adaptive digital studio crafting exceptional digital experiences. We combine creative design, cutting-edge technology, and strategic thinking to deliver transformative solutions that drive business growth and success.")
    cta_button_text = models.CharField(max_length=50, default="Start Your Project")
    cta_button_url = models.CharField(max_length=100, default="/contact/")
    secondary_cta_text = models.CharField(max_length=50, default="Watch Showreel", blank=True)
    secondary_cta_url = models.CharField(max_length=100, default="#portfolio", blank=True)
    
    # Stats
    stats_label_1 = models.CharField(max_length=30, default="Projects")
    stats_number_1 = models.CharField(max_length=10, default="180+")
    stats_label_2 = models.CharField(max_length=30, default="Satisfaction")
    stats_number_2 = models.CharField(max_length=10, default="98%")
    stats_label_3 = models.CharField(max_length=30, default="Team")
    stats_number_3 = models.CharField(max_length=10, default="50+")
    
    # Badges
    badge_text = models.CharField(max_length=50, default="ADAPTIVE DIGITAL STUDIO")
    show_badge = models.BooleanField(default=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return f"Hero - {self.title_line_1} {self.title_line_2}"


class Service(models.Model):
    """Services offered by the company"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200, blank=True)
    icon_class = models.CharField(max_length=100, default="fa-code", help_text="FontAwesome icon class")
    hero_image = models.ImageField(upload_to='services/hero/', blank=True, null=True, help_text="Main hero banner image")
    banner_image = models.ImageField(upload_to='services/banner/', blank=True, null=True, help_text="Secondary banner image")
    tags = models.JSONField(default=list, blank=True, help_text="Array of technology tags")
    features = models.JSONField(default=list, blank=True, help_text='[{"title": "...", "description": "...", "icon": "fa-icon"}]')
    process_steps = models.JSONField(default=list, blank=True, help_text='[{"title": "...", "description": "..."}]')
    faqs = models.JSONField(default=list, blank=True, help_text='[{"question": "...", "answer": "..."}]')
    stats = models.JSONField(default=list, blank=True, help_text='[{"value": "100+", "label": "..."}]')
    timeline = models.CharField(max_length=100, blank=True, help_text="e.g., 4-8 weeks")
    starting_price = models.CharField(max_length=100, blank=True, help_text="e.g., $2,000")
    support = models.CharField(max_length=100, blank=True, help_text="e.g., 24/7 Support")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ServiceImage(models.Model):
    """Additional images for a service detail page"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='gallery_images')
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='services/gallery/')
    caption = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.service.title} - {self.title or f'Image {self.id}'}"


class ServiceCaseStudy(models.Model):
    """Case studies / portfolio items linked to a service"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='case_studies')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/case-studies/')
    client = models.CharField(max_length=100, blank=True)
    result = models.CharField(max_length=200, blank=True, help_text="e.g., 200% increase in traffic")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    """Client testimonials"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    quote = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.company}"


class ProcessStep(models.Model):
    """Process steps for about page"""
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, default="fa-lightbulb", help_text="FontAwesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Process Step"
        verbose_name_plural = "Process Steps"
        ordering = ['order', 'step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class PortfolioCategory(models.Model):
    """Portfolio categories"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PortfolioItem(models.Model):
    """Portfolio/project items"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    client_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Portfolio Item"
        verbose_name_plural = "Portfolio Items"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """Singleton settings for the entire site"""
    company_name = models.CharField(max_length=100, default="HELPEX BRO")
    tagline = models.CharField(max_length=200, default="Adaptive Digital Studio")
    description = models.TextField(default="", blank=True)
    
    # Contact Info
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    office_hours = models.CharField(max_length=100, default="Mon-Fri: 9AM - 6PM")
    
    # Social Links
    social_twitter = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    social_dribbble = models.URLField(blank=True)
    social_github = models.URLField(blank=True)
    
    # Branding
    primary_color = models.CharField(max_length=7, default="#28A197")
    secondary_color = models.CharField(max_length=7, default="#1A1F3B")
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    
    # Section Titles (Dynamic)
    hero_tagline = models.CharField(max_length=100, default="Innovating the Future")
    hero_subtagline = models.CharField(max_length=100, default="One Solution at a Time")
    section_services_title = models.CharField(max_length=100, default="Our Services")
    section_testimonials_title = models.CharField(max_length=100, default="What Our Clients Say")
    section_process_title = models.CharField(max_length=100, default="Our Working Process")
    section_portfolio_title = models.CharField(max_length=100, default="Our Portfolio")
    section_team_title = models.CharField(max_length=100, default="Our Team")
    section_clients_title = models.CharField(max_length=100, default="Our Clients")
    section_blog_title = models.CharField(max_length=100, default="Latest Insights")
    section_gallery_title = models.CharField(max_length=100, default="Our Gallery")
    section_contact_title = models.CharField(max_length=100, default="Get In Touch")
    section_about_title = models.CharField(max_length=100, default="About Us")
    
    # Copyright
    copyright_text = models.CharField(max_length=200, default="HELPEX BRO. All rights reserved.")
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError("Only one set of site settings is allowed")
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        """Get or create site settings"""
        settings, created = cls.objects.get_or_create(pk=1)
        return settings


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

    def get_absolute_url(self):
        return reverse('admin:helpex_app_contactmessage_change', args=[self.pk])


class TeamMember(models.Model):
    """Team members for about page"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.role}"


class Client(models.Model):
    """Client logos and information"""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/', blank=True, null=True)
    website = models.URLField(blank=True, help_text="Client website URL")
    industry = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    """Blog categories"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    """Blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    excerpt = models.TextField(max_length=300, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100, default="HELPEX Team")
    author_image = models.ImageField(upload_to='blog/authors/', blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class GalleryCategory(models.Model):
    """Gallery categories for organizing images"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default="fa-images", help_text="FontAwesome icon class")
    color = models.CharField(max_length=7, default="#28A197", help_text="Category accent color (hex)")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class WhyChooseUsSection(models.Model):
    """Why Choose Us page section settings"""
    title = models.CharField(max_length=200, default="Why Choose Us")
    subtitle = models.TextField(default="Discover what makes us the perfect partner for your digital success", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Why Choose Us Section"
        verbose_name_plural = "Why Choose Us Section"

    def __str__(self):
        return self.title


class WhyChooseUsReason(models.Model):
    """Reasons why clients choose us"""
    title = models.CharField(max_length=150)
    description = models.TextField()
    short_description = models.CharField(max_length=200, blank=True)
    icon_class = models.CharField(max_length=100, default='fa-check-circle', help_text="FontAwesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Why Choose Us Reason"
        verbose_name_plural = "Why Choose Us Reasons"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class WhyChooseUsStat(models.Model):
    """Statistics/achievements for Why Choose Us page"""
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, default='fa-trophy', help_text="FontAwesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Why Choose Us Stat"
        verbose_name_plural = "Why Choose Us Stats"
        ordering = ['order', 'label']

    def __str__(self):
        return f"{self.number} - {self.label}"


class PricingPlan(models.Model):
    """Pricing plans for the pricing page"""
    PLAN_TYPE_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('one_time', 'One Time'),
    ]
    
    POPULAR_CHOICES = [
        ('none', 'None'),
        ('popular', 'Popular'),
        ('best_value', 'Best Value'),
        ('recommended', 'Recommended'),
    ]
    
    name = models.CharField(max_length=100, help_text="Plan name (e.g., Basic, Pro, Enterprise)")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Short description of the plan")
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPE_CHOICES, default='monthly')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Plan price")
    currency = models.CharField(max_length=10, default='$', help_text="Currency symbol")
    billing_period = models.CharField(max_length=50, default='/month', help_text="Billing period text")
    popular_badge = models.CharField(max_length=20, choices=POPULAR_CHOICES, default='none', help_text="Highlight this plan")
    cta_text = models.CharField(max_length=50, default='Get Started', help_text="Call to action button text")
    cta_url = models.CharField(max_length=200, default='/contact/', blank=True, help_text="CTA button URL")
    icon_class = models.CharField(max_length=100, default='fa-star', help_text="FontAwesome icon class")
    color_accent = models.CharField(max_length=7, default='#28A197', help_text="Accent color for this plan (hex)")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pricing Plan"
        verbose_name_plural = "Pricing Plans"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.currency}{self.price}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PricingFeature(models.Model):
    """Features included in pricing plans"""
    plan = models.ForeignKey(PricingPlan, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=200, help_text="Feature description")
    included = models.BooleanField(default=True, help_text="Is this feature included in the plan?")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Pricing Feature"
        verbose_name_plural = "Pricing Features"
        ordering = ['plan', 'order']

    def __str__(self):
        return f"{self.plan.name} - {self.text}"


class GalleryImage(models.Model):
    """Gallery images with metadata"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    thumbnail = models.ImageField(upload_to='gallery/thumbs/', blank=True, null=True, help_text="Optional thumbnail for optimized loading")
    description = models.TextField(blank=True)
    
    alt_text = models.CharField(max_length=200, blank=True, help_text="SEO alt text for the image")
    photographer = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    captured_date = models.DateField(null=True, blank=True)
    
    tags = models.JSONField(default=list, blank=True, help_text="Array of tags for filtering")
    
    aspect_ratio = models.CharField(max_length=20, default="landscape", choices=[
        ('portrait', 'Portrait'),
        ('landscape', 'Landscape'),
        ('square', 'Square'),
    ])
    
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, help_text="Show in featured slider")
    is_active = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ['order', '-is_featured', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.thumbnail.url if self.thumbnail else self.image.url


class RegisteredCompany(models.Model):
    """Companies/organizations the business is registered or approved with"""
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='registered/', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, help_text="e.g., Registered with SECP")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Registered Company"
        verbose_name_plural = "Registered Companies"

    def __str__(self):
        return self.name