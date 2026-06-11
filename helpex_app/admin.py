from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from .models import (
    HeroSection, HeroCarouselItem, Service, ServiceImage, ServiceCaseStudy, Testimonial, ProcessStep,
    PortfolioCategory, PortfolioItem, SiteSettings,
    ContactMessage, TeamMember, Client, BlogCategory, BlogPost,
    GalleryCategory, GalleryImage, PricingPlan, PricingFeature,
    WhyChooseUsSection, WhyChooseUsReason, WhyChooseUsStat, RegisteredCompany,
    ProductCategory, Product, ProductFeature, ProductScreenshot
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        # Ensure settings exist
        if not SiteSettings.objects.exists():
            settings = SiteSettings.objects.create(pk=1)
        # Redirect to the existing settings
        if object_id is None:
            return HttpResponseRedirect('/admin/helpex_app/sitesettings/1/change/')
        return super().changeform_view(request, object_id, form_url, extra_context)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title_line_1', 'title_line_2', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title_line_1', 'title_line_2']
    ordering = ['-created_at']


@admin.register(HeroCarouselItem)
class HeroCarouselItemAdmin(admin.ModelAdmin):
    list_display = ['media_type', 'order', 'is_active', 'created_at']
    list_filter = ['media_type', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'id']
    fieldsets = (
        ('Media', {
            'fields': ('media_type', 'image', 'video'),
            'description': 'Upload either an image OR a video file.'
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'order', 'is_active', 'is_featured']
    list_filter = ['is_active', 'is_featured']
    search_fields = ['title', 'description', 'short_description']
    list_editable = ['order', 'is_active', 'is_featured']
    ordering = ['order', 'title']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'short_description', 'icon_class', 'order', 'is_active', 'is_featured')
        }),
        ('Images', {
            'fields': ('hero_image', 'banner_image'),
            'classes': ('collapse',)
        }),
        ('Content', {
            'fields': ('description', 'tags', 'features', 'process_steps', 'faqs', 'stats'),
            'description': 'Use JSON format for arrays. Example for features: [{"title": "Fast", "description": "Quick delivery", "icon": "fa-bolt"}]'
        }),
        ('Details', {
            'fields': ('timeline', 'starting_price', 'support'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'order', 'is_featured']
    list_filter = ['service', 'is_featured']
    list_editable = ['order', 'is_featured']
    ordering = ['service', 'order']


@admin.register(ServiceCaseStudy)
class ServiceCaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'client', 'order', 'is_active']
    list_filter = ['service', 'is_active']
    search_fields = ['title', 'description', 'client']
    list_editable = ['order', 'is_active']
    ordering = ['service', 'order']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'client_link', 'project_link', 'rating', 'order', 'is_active']
    list_filter = ['is_active', 'rating', 'client', 'project']
    search_fields = ['name', 'company', 'quote']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    fieldsets = (
        ('Reviewer Info', {
            'fields': ('name', 'role', 'company', 'avatar')
        }),
        ('Review', {
            'fields': ('quote', 'rating')
        }),
        ('Links', {
            'fields': ('client', 'project'),
            'description': 'Link this review to a specific client and/or project for tracking.'
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def client_link(self, obj):
        if obj.client:
            return obj.client.name
        return '—'
    client_link.short_description = 'Client'

    def project_link(self, obj):
        if obj.project:
            return obj.project.title
        return '—'
    project_link.short_description = 'Project'


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ['step_number', 'title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'step_number']


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    ordering = ['-created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    
    mark_as_read.short_description = "Mark as read"
    mark_as_unread.short_description = "Mark as unread"
    
    actions = ['mark_as_read', 'mark_as_unread']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'role']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry', 'is_featured', 'order', 'is_active']
    list_filter = ['is_active', 'is_featured', 'industry']
    search_fields = ['name', 'industry']
    list_editable = ['order', 'is_active', 'is_featured']
    ordering = ['order', 'name']


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_published', 'is_featured', 'view_count', 'created_at']
    list_filter = ['is_published', 'is_featured', 'category']
    search_fields = ['title', 'content']
    list_editable = ['is_published', 'is_featured']
    ordering = ['-created_at']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_display', 'color_preview', 'order', 'image_count', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Appearance', {
            'fields': ('icon', 'color')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def icon_display(self, obj):
        return format_html('<i class="fas {}"></i> {}', obj.icon, obj.name)
    icon_display.short_description = 'Category'

    def color_preview(self, obj):
        return format_html(
            '<span style="display: inline-block; width: 24px; height: 24px; background: {}; border-radius: 4px; border: 1px solid #ddd;"></span>',
            obj.color
        )
    color_preview.short_description = 'Color'

    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_preview', 'title', 'category', 'aspect_ratio', 'is_featured', 'is_active', 'order', 'view_count', 'created_at']
    list_filter = ['is_active', 'is_featured', 'category', 'aspect_ratio']
    search_fields = ['title', 'description', 'tags', 'photographer', 'location']
    list_editable = ['order', 'is_active', 'is_featured']
    ordering = ['order', '-is_featured', '-created_at']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'description')
        }),
        ('Image', {
            'fields': ('image', 'thumbnail')
        }),
        ('SEO & Metadata', {
            'fields': ('alt_text', 'tags'),
            'classes': ('collapse',)
        }),
        ('Details', {
            'fields': ('photographer', 'location', 'captured_date', 'aspect_ratio')
        }),
        ('Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        from django.utils.safestring import mark_safe
        return mark_safe('<span style="color: #999;">No image</span>')
    thumbnail_preview.short_description = 'Preview'

    def created(self, obj):
        return obj.created_at.strftime('%b %d, %Y')
    created.short_description = 'Added'

    readonly_fields = ['view_count', 'created_at', 'updated_at']

    actions = ['make_active', 'make_inactive', 'make_featured', 'remove_featured']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected as inactive"
    
    actions = ['make_active', 'make_inactive']


@admin.register(RegisteredCompany)
class RegisteredCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width:50px;height:50px;object-fit:contain;border-radius:8px;" />', obj.logo.url)
        return '—'
    logo_preview.short_description = 'Logo'


@admin.register(WhyChooseUsSection)
class WhyChooseUsSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        return not WhyChooseUsSection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(WhyChooseUsReason)
class WhyChooseUsReasonAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected as active"
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected as inactive"
    
    actions = ['make_active', 'make_inactive']


@admin.register(WhyChooseUsStat)
class WhyChooseUsStatAdmin(admin.ModelAdmin):
    list_display = ['number', 'label', 'icon_class', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['label', 'number']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'label']
    
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected as active"
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected as inactive"
    
    actions = ['make_active', 'make_inactive']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon_display', 'color_preview', 'order', 'product_count', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Appearance', {
            'fields': ('icon_class', 'color')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def icon_display(self, obj):
        return format_html('<i class="fas {}"></i> {}', obj.icon_class, obj.name)
    icon_display.short_description = 'Category'

    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:24px;height:24px;background:{};border-radius:4px;border:1px solid #ddd;"></span>',
            obj.color
        )
    color_preview.short_description = 'Color'

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'pricing_type', 'version', 'order', 'is_active', 'is_featured']
    list_filter = ['is_active', 'is_featured', 'pricing_type', 'category']
    search_fields = ['name', 'tagline', 'description', 'short_description']
    list_editable = ['order', 'is_active', 'is_featured']
    ordering = ['order', 'name']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'category', 'tagline', 'short_description', 'icon_class', 'order', 'is_active', 'is_featured')
        }),
        ('Images', {
            'fields': ('hero_image', 'logo'),
            'classes': ('collapse',)
        }),
        ('Version & Release', {
            'fields': ('version', 'release_date'),
            'classes': ('collapse',)
        }),
        ('Pricing', {
            'fields': ('pricing_type', 'price', 'currency', 'billing_period'),
        }),
        ('Links', {
            'fields': ('website_url', 'demo_url', 'docs_url', 'github_url'),
            'classes': ('collapse',)
        }),
        ('Content (JSON)', {
            'fields': ('description', 'features', 'specifications', 'screenshots', 'faqs', 'tech_stack', 'system_requirements'),
            'description': 'Use JSON format. Example: [{"title": "Fast", "description": "Quick delivery"}]'
        }),
    )

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected as inactive"

    actions = ['make_active', 'make_inactive']


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'icon_class', 'order', 'is_active']
    list_filter = ['product', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['product', 'order']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected as inactive"

    actions = ['make_active', 'make_inactive']


@admin.register(ProductScreenshot)
class ProductScreenshotAdmin(admin.ModelAdmin):
    list_display = ['product', 'caption', 'order', 'is_active', 'image_preview']
    list_filter = ['product', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['product', 'order']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;" />', obj.image.url)
        return '�'
    image_preview.short_description = 'Preview'
