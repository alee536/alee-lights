from django.db import models


class ContactInquiry(models.Model):
    EVENT_TYPE_CHOICES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('engagement', 'Engagement'),
        ('eid', 'Eid Celebration'),
        ('christmas', 'Christmas'),
        ('corporate', 'Corporate Event'),
        ('other', 'Other'),
    ]

    RENTAL_DURATION_CHOICES = [
        ('1day', '1 Day'),
        ('2days', '2 Days'),
        ('3days', '3 Days'),
        ('5days', '5 Days'),
        ('7days', '7 Days'),
        ('10days', '10 Days'),
        ('custom', 'Custom Duration'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    event_date = models.DateField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    rental_duration = models.CharField(max_length=20, choices=RENTAL_DURATION_CHOICES)
    message = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'

    def __str__(self):
        return f"{self.full_name} - {self.get_event_type_display()} - {self.event_date}"


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Wedding', 'Wedding'),
        ('Birthday', 'Birthday'),
        ('Christmas', 'Christmas'),
        ('Eid', 'Eid'),
        ('Corporate', 'Corporate'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price_3days = models.PositiveIntegerField(verbose_name='Price (3 Days)')
    price_5days = models.PositiveIntegerField(verbose_name='Price (5 Days)')
    price_7days = models.PositiveIntegerField(verbose_name='Price (7 Days)')
    price_10days = models.PositiveIntegerField(verbose_name='Price (10 Days)')
    spec_lights = models.CharField(max_length=100, verbose_name='Lights')
    spec_coverage = models.CharField(max_length=100, verbose_name='Coverage')
    spec_style = models.CharField(max_length=100, verbose_name='Style')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name} - Image {self.order}"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=5)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)

    def __str__(self):
        return f"{self.name} - {self.event_type}"


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('Wedding', 'Wedding'),
        ('Birthday', 'Birthday'),
        ('Christmas', 'Christmas'),
        ('Eid', 'Eid'),
        ('Corporate', 'Corporate'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.category})"


class HeroSlide(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='hero/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
