import os
from django.core.management.base import BaseCommand
from core.models import Product, Testimonial, GalleryImage, HeroSlide


class Command(BaseCommand):
    help = 'Seed the database with initial data (products, gallery, testimonials, hero slides)'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # ==================== HERO SLIDES ====================
        if HeroSlide.objects.count() == 0:
            slides = [
                {
                    'title': 'Transform Your Special Moments with Luxurious Outdoor Lighting',
                    'subtitle': 'Premium light decoration rentals for unforgettable celebrations',
                    'image': 'hero/Garden_party_with_fairy_lights_c450bf55.png',
                    'order': 1,
                },
                {
                    'title': 'Elegant Lighting for Every Occasion',
                    'subtitle': 'Weddings, birthdays, corporate events, and more',
                    'image': 'hero/Wedding_venue_with_romantic_lighting_8e02b9ec.png',
                    'order': 2,
                },
                {
                    'title': 'Professional Installation & Premium Quality',
                    'subtitle': '500+ happy clients, 1000+ successful events',
                    'image': 'hero/Christmas_luxury_lighting_display_629dbbd6.png',
                    'order': 3,
                },
            ]
            for s in slides:
                HeroSlide.objects.create(**s)
            self.stdout.write(self.style.SUCCESS(f'  Created {len(slides)} hero slides'))
        else:
            self.stdout.write('  Hero slides already exist, skipping...')

        # ==================== PRODUCTS ====================
        if Product.objects.count() == 0:
            products = [
                {
                    'name': 'Elegant Wedding Package',
                    'category': 'Wedding',
                    'image': 'products/Premium_LED_string_lights_closeup_f9cc5a19.jfif',
                    'description': 'Premium warm white LED lights perfect for creating a romantic ambiance at your special celebration',
                    'price_3days': 25000,
                    'price_5days': 38000,
                    'price_7days': 48000,
                    'price_10days': 62000,
                    'spec_lights': '2000+ LEDs',
                    'spec_coverage': 'Up to 2000 sq ft',
                    'spec_style': 'Warm White Elegance',
                    'is_featured': True,
                    'order': 1,
                },
                {
                    'name': 'Garden Party Deluxe',
                    'category': 'Birthday',
                    'image': 'products/Garden_party_with_fairy_lights_c450bf55.png',
                    'description': 'Charming fairy lights and ambient lighting to transform your garden into a magical wonderland',
                    'price_3days': 18000,
                    'price_5days': 28000,
                    'price_7days': 36000,
                    'price_10days': 45000,
                    'spec_lights': '1500+ LEDs',
                    'spec_coverage': 'Up to 1500 sq ft',
                    'spec_style': 'Fairy Light Magic',
                    'is_featured': True,
                    'order': 2,
                },
                {
                    'name': 'Christmas Grand Display',
                    'category': 'Christmas',
                    'image': 'products/Christmas_luxury_lighting_display_629dbbd6.png',
                    'description': 'Spectacular holiday lighting package featuring icicle lights and architectural illumination',
                    'price_3days': 32000,
                    'price_5days': 48000,
                    'price_7days': 60000,
                    'price_10days': 75000,
                    'spec_lights': '3000+ LEDs',
                    'spec_coverage': 'Up to 3000 sq ft',
                    'spec_style': 'Holiday Splendor',
                    'is_featured': True,
                    'order': 3,
                },
                {
                    'name': 'Night Outdoor Setup',
                    'category': 'Corporate',
                    'image': 'products/open (1).jfif',
                    'description': 'Apne event ko den aik modern aur dreamy look is Starry Night Decoration ke sath. High-quality string lights aur behtareen seating arrangement jo aapke mehmano ko hairan kar dega.',
                    'price_3days': 15000,
                    'price_5days': 25000,
                    'price_7days': 35000,
                    'price_10days': 45000,
                    'spec_lights': 'Premium String Lights',
                    'spec_coverage': 'Outdoor Setup',
                    'spec_style': 'Starry Night Dreamy',
                    'is_featured': True,
                    'order': 4,
                },
            ]
            for p in products:
                Product.objects.create(**p)
            self.stdout.write(self.style.SUCCESS(f'  Created {len(products)} products'))
        else:
            self.stdout.write('  Products already exist, skipping...')

        # ==================== TESTIMONIALS ====================
        if Testimonial.objects.count() == 0:
            testimonials = [
                {
                    'name': 'Ahmed & Sara Khan',
                    'event_type': 'Wedding Celebration',
                    'rating': 5,
                    'testimonial': 'Absolutely stunning! The lighting transformed our venue into a magical space. The team was professional, punctual, and the quality exceeded our expectations. Highly recommended!',
                    'image': 'testimonials/Happy_customer_couple_portrait_78cb04c2.png',
                },
                {
                    'name': 'Ayesha Malik',
                    'event_type': 'Birthday Party',
                    'rating': 5,
                    'testimonial': "The garden party package was perfect for my daughter's birthday. The fairy lights created such a beautiful atmosphere. Installation was seamless and removal was handled professionally.",
                    'image': 'testimonials/Professional_woman_testimonial_portrait_62e76b6c.png',
                },
                {
                    'name': 'Rashid Abdullah',
                    'event_type': 'Corporate Event',
                    'rating': 5,
                    'testimonial': 'We used Lights for our annual corporate gala. The sophisticated lighting added tremendous value to our event. Guests were impressed and the setup was flawless.',
                    'image': 'testimonials/Business_professional_testimonial_portrait_ab18402e.png',
                },
            ]
            for t in testimonials:
                Testimonial.objects.create(**t)
            self.stdout.write(self.style.SUCCESS(f'  Created {len(testimonials)} testimonials'))
        else:
            self.stdout.write('  Testimonials already exist, skipping...')

        # ==================== GALLERY IMAGES ====================
        if GalleryImage.objects.count() == 0:
            gallery = [
                {'title': 'Elegant Wedding Setup', 'category': 'Wedding', 'image': 'gallery/Luxury_mansion_with_elegant_lighting_12b28620.png', 'order': 1},
                {'title': 'Wedding Setup 1', 'category': 'Wedding', 'image': 'gallery/wedding (1).png', 'order': 2},
                {'title': 'Wedding Setup 2', 'category': 'Wedding', 'image': 'gallery/wedding (2).png', 'order': 3},
                {'title': 'Wedding Setup 3', 'category': 'Wedding', 'image': 'gallery/wedding (3).png', 'order': 4},
                {'title': 'Wedding Setup 4', 'category': 'Wedding', 'image': 'gallery/wedding (4).png', 'order': 5},
                {'title': 'Wedding Setup 5', 'category': 'Wedding', 'image': 'gallery/wedding (5).png', 'order': 6},
                {'title': 'Wedding Setup 6', 'category': 'Wedding', 'image': 'gallery/wedding (6).png', 'order': 7},
                {'title': 'Wedding Setup 7', 'category': 'Wedding', 'image': 'gallery/wedding (7).png', 'order': 8},
                {'title': 'Wedding Setup 8', 'category': 'Wedding', 'image': 'gallery/wedding (8).png', 'order': 9},
                {'title': 'Garden Party Ambiance', 'category': 'Birthday', 'image': 'gallery/Garden_party_with_fairy_lights_c450bf55.png', 'order': 10},
                {'title': 'Holiday Luxury Display', 'category': 'Christmas', 'image': 'gallery/Christmas_luxury_lighting_display_629dbbd6.png', 'order': 11},
                {'title': 'Festive Celebration', 'category': 'Eid', 'image': 'gallery/Eid_celebration_luxury_lighting_d4858fdb.png', 'order': 12},
                {'title': 'Corporate Event Lighting', 'category': 'Corporate', 'image': 'gallery/Modern_home_with_architectural_lighting_a5a24633.png', 'order': 13},
                {'title': 'Corporate Outdoor Setup 1', 'category': 'Corporate', 'image': 'gallery/open (1).png', 'order': 14},
                {'title': 'Corporate Outdoor Setup 2', 'category': 'Corporate', 'image': 'gallery/open (2).png', 'order': 15},
            ]
            for g in gallery:
                GalleryImage.objects.create(**g)
            self.stdout.write(self.style.SUCCESS(f'  Created {len(gallery)} gallery images'))
        else:
            self.stdout.write('  Gallery images already exist, skipping...')

        self.stdout.write(self.style.SUCCESS('\nDatabase seeded successfully!'))
