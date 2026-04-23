from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import (
    HeroSection, Service, Testimonial, ProcessStep, 
    PortfolioCategory, PortfolioItem, SiteSettings, 
    ContactMessage, TeamMember, Client, BlogCategory, BlogPost
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def get_urls(self):
        urls = super().get_urls()
        return [path('', lambda r: HttpResponseRedirect('/admin/helpex_app/sitesettings/1/change/'))] + urls
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if not SiteSettings.objects.exists() and object_id is None:
            return HttpResponseRedirect('/admin/helpex_app/sitesettings/add/')
        return super().changeform_view(request, object_id, form_url, extra_context)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title_line_1', 'title_line_2', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title_line_1', 'title_line_2']
    ordering = ['-created_at']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'rating', 'order', 'is_active']
    list_filter = ['is_active', 'rating']
    search_fields = ['name', 'company', 'quote']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']


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