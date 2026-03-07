# ✨ AleeLights

Premium outdoor light decoration rental service based in Bahria Town, Lahore. Built with Django and Tailwind CSS.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38bdf8?logo=tailwindcss)

## Features

- **Product Catalog** — Browse light decoration packages for weddings, birthdays, corporate events, Eid & Christmas
- **Product Detail Pages** — Multi-image gallery with lightbox zoom
- **Pricing Tables** — Flexible rental durations (3, 5, 7, 10 days)
- **Contact Form** — AJAX-powered inquiry form with professional HTML email notifications
- **WhatsApp Integration** — One-click chat buttons throughout the site
- **Dark Mode** — Toggle with localStorage persistence
- **Admin Panel** — Full Django admin for managing products, images, testimonials, gallery & inquiries
- **Responsive Design** — Mobile-first with Tailwind CSS

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.2, Python 3.13 |
| Frontend | Tailwind CSS (CDN), Lucide Icons |
| Fonts | Playfair Display, Montserrat (Google Fonts) |
| Database | SQLite (dev) / MySQL (production) |
| Email | Gmail SMTP with HTML templates |
| Hosting | PythonAnywhere |

## Quick Start

```bash
# Clone
git clone https://github.com/alee536/alee-lights.git
cd alee-lights

# Install dependencies
pip install -r requirements.txt

# Set environment variable
set EMAIL_HOST_PASSWORD=your-gmail-app-password

# Run migrations & seed data
python manage.py migrate
python manage.py seed_data

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Project Structure

```
aleelights/
├── aleelights/          # Django project settings
├── core/                # Main app (models, views, forms, admin)
│   ├── management/      # Custom commands (seed_data)
│   ├── migrations/
│   ├── models.py        # Product, ProductImage, Testimonial, Gallery, HeroSlide, ContactInquiry
│   ├── views.py         # Home, product detail, contact form with email
│   └── admin.py         # Admin configuration with inlines
├── templates/           # Django templates
│   ├── base.html
│   ├── home.html
│   ├── product_detail.html
│   └── partials/        # Header, footer, floating actions
├── static/
│   ├── css/style.css    # Custom styles + dark mode
│   └── js/main.js       # Dark mode toggle, gallery, slider, AJAX
└── manage.py
```

## Admin Panel

Access at `/admin/` to manage:
- Products & product images
- Hero slider slides
- Testimonials
- Gallery images
- Contact inquiries

## Contact

- **Phone/WhatsApp:** +92 302 5329536
- **Email:** aleelights786@gmail.com
- **Location:** Bahria Town, Lahore
