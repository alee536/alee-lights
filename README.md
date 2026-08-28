# AleeLights

Premium outdoor light decoration rental service based in Bahria Town, Lahore. Built with Django and Tailwind CSS.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38bdf8?logo=tailwindcss)

## Features

- **Product Catalog** - Browse light decoration packages for weddings, birthdays, corporate events, Eid, and Christmas
- **Product Detail Pages** - Multi-image gallery with lightbox zoom
- **Pricing Tables** - Flexible rental durations: 3, 5, 7, and 10 days
- **Contact Form** - AJAX-powered inquiry form with HTML email notifications
- **WhatsApp Integration** - One-click chat buttons throughout the site
- **Dark Mode** - Toggle with localStorage persistence
- **Admin Panel** - Django admin for products, images, testimonials, gallery, and inquiries
- **Responsive Design** - Mobile-first layout with Tailwind CSS

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django, Python |
| Frontend | Django templates, Tailwind CSS CDN, Lucide Icons |
| Fonts | Playfair Display, Montserrat |
| Database | SQLite for development |
| Email | Gmail SMTP |
| Hosting | PythonAnywhere |

## Folder Structure

```text
aleelights/
├── backend/
│   ├── aleelights/          # Django project settings
│   ├── core/                # Django app: models, views, forms, admin
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── templates/           # Django templates
│   ├── static/              # CSS, JavaScript, fallback images
│   └── media/               # Seeded product, hero, gallery, and testimonial media
└── README.md
```

## Quick Start

```bash
# Clone
git clone https://github.com/alee536/alee-lights.git
cd alee-lights

# Install dependencies
cd backend
pip install -r requirements.txt

# Set Gmail app password for inquiry emails
set EMAIL_HOST_PASSWORD=your-gmail-app-password

# Run migrations and seed data
python manage.py migrate
python manage.py seed_data

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

For local development, you can also keep `EMAIL_HOST_PASSWORD=...` in a root `.env` file or in `backend/.env`.

## Admin Panel

Access `/admin/` to manage:

- Products and product images
- Hero slider slides
- Testimonials
- Gallery images
- Contact inquiries

## Contact

- **Phone/WhatsApp:** +92 302 5329536
- **Email:** aleelights786@gmail.com
- **Location:** Bahria Town, Lahore
