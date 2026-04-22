from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class HeroSection(models.Model):
    """Hero section for the homepage"""
    title_line_1 = models.CharField(max_length=100, default="We craft")
    title_line_2 = models.CharField(max_length=100, default="experiences")
    typing_texts = models.JSONField(default=list, blank=True, help_text="Array of animated texts")
    description = models.TextField(default="HELPEX delivers premium web applications, custom software solutions, and iconic visual identities that transform businesses worldwide.")
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
    description = models.TextField()
    short_description = models.CharField(max_length=200, blank=True)
    icon_class = models.CharField(max_length=100, default="fa-code", help_text="FontAwesome icon class")
    tags = models.JSONField(default=list, blank=True, help_text="Array of technology tags")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


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
    
    # Social Links
    social_twitter = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    social_dribbble = models.URLField(blank=True)
    
    # Branding
    primary_color = models.CharField(max_length=7, default="#28A197")
    secondary_color = models.CharField(max_length=7, default="#1A1F3B")
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    
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