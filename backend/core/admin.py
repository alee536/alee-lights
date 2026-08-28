from django.contrib import admin
from .models import ContactInquiry, Product, ProductImage, Testimonial, GalleryImage, HeroSlide


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'event_type', 'event_date', 'rental_duration', 'created_at']
    list_filter = ['event_type', 'rental_duration', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_3days', 'price_10days', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured', 'order']
    search_fields = ['name']
    inlines = [ProductImageInline]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_type', 'rating']
    list_filter = ['rating']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
