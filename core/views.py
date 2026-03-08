from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Product, ProductImage, Testimonial, GalleryImage, HeroSlide
from .forms import ContactInquiryForm


def home(request):
    hero_slides = HeroSlide.objects.filter(is_active=True)
    featured_products = Product.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.all()
    gallery_images = GalleryImage.objects.all()
    categories = gallery_images.values_list('category', flat=True).distinct()
    form = ContactInquiryForm()

    context = {
        'hero_slides': hero_slides,
        'featured_products': featured_products,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
        'gallery_categories': categories,
        'form': form,
    }
    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    extra_images = product.images.all()
    related_products = Product.objects.filter(is_featured=True).exclude(pk=pk)[:3]
    form = ContactInquiryForm()
    context = {
        'product': product,
        'extra_images': extra_images,
        'related_products': related_products,
        'form': form,
    }
    return render(request, 'product_detail.html', context)


@require_POST
def submit_inquiry(request):
    form = ContactInquiryForm(request.POST)
    if form.is_valid():
        inquiry = form.save()
        # Forward to email
        try:
            subject = f'New Inquiry: {inquiry.get_event_type_display()} - {inquiry.full_name}'
            phone_clean = inquiry.phone.replace(' ', '').replace('-', '')
            if not phone_clean.startswith('+') and not phone_clean.startswith('92'):
                phone_wa = '92' + phone_clean.lstrip('0')
            else:
                phone_wa = phone_clean.lstrip('+')
            html_body = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="margin:0;padding:0;background:#f0f0f0;font-family:Arial,Helvetica,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f0f0;padding:32px 0;">
<tr><td align="center">
<table width="680" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">

    <!-- HEADER -->
    <tr><td style="background:linear-gradient(135deg,#0f2027 0%,#203a43 50%,#2c5364 100%);padding:20px 40px;text-align:center;">
        <table width="100%" cellpadding="0" cellspacing="0"><tr><td align="center">
            <h1 style="color:#ffffff;margin:0;font-size:22px;font-weight:700;letter-spacing:3px;font-family:Georgia,serif;">&#10024; AleeLights</h1>
            <p style="color:rgba(255,255,255,0.7);margin:6px 0 0;font-size:12px;font-weight:400;letter-spacing:1.5px;">NEW INQUIRY RECEIVED</p>
        </td></tr></table>
    </td></tr>

    <!-- CUSTOMER INFO CARD -->
    <tr><td style="padding:36px 40px 0;">
        <table width="100%" cellpadding="0" cellspacing="0" style="background:#fafafa;border-radius:12px;border:1px solid #eee;overflow:hidden;">
            <!-- Name Row -->
            <tr>
                <td style="padding:16px 20px;width:44px;vertical-align:middle;border-bottom:1px solid #eee;">
                    <div style="width:40px;height:40px;border-radius:50%;background:#f3e8d0;text-align:center;line-height:40px;font-size:18px;">&#128100;</div>
                </td>
                <td style="padding:16px 0;border-bottom:1px solid #eee;vertical-align:middle;">
                    <div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#999;font-weight:600;">Full Name</div>
                    <div style="font-size:16px;color:#1a1a1a;font-weight:700;margin-top:2px;">{inquiry.full_name}</div>
                </td>
            </tr>
            <!-- Email Row -->
            <tr>
                <td style="padding:16px 20px;width:44px;vertical-align:middle;border-bottom:1px solid #eee;">
                    <div style="width:40px;height:40px;border-radius:50%;background:#dbeafe;text-align:center;line-height:40px;font-size:18px;">&#9993;</div>
                </td>
                <td style="padding:16px 0;border-bottom:1px solid #eee;vertical-align:middle;">
                    <div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#999;font-weight:600;">Email</div>
                    <a href="mailto:{inquiry.email}" style="font-size:15px;color:#2c5364;text-decoration:none;font-weight:600;margin-top:2px;display:block;">{inquiry.email}</a>
                </td>
            </tr>
            <!-- Phone Row -->
            <tr>
                <td style="padding:16px 20px;width:44px;vertical-align:middle;border-bottom:1px solid #eee;">
                    <div style="width:40px;height:40px;border-radius:50%;background:#d1fae5;text-align:center;line-height:40px;font-size:18px;">&#128222;</div>
                </td>
                <td style="padding:16px 0;border-bottom:1px solid #eee;vertical-align:middle;">
                    <div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#999;font-weight:600;">Phone</div>
                    <a href="tel:{inquiry.phone}" style="font-size:15px;color:#2c5364;text-decoration:none;font-weight:600;margin-top:2px;display:block;">{inquiry.phone}</a>
                </td>
            </tr>
        </table>
    </td></tr>

    <!-- EVENT DETAILS CARDS -->
    <tr><td style="padding:24px 40px 0;">
        <table width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <!-- Event Date -->
            <td width="33%" style="padding-right:8px;">
                <div style="background:#fff7ed;border:1px solid #fed7aa;border-radius:12px;padding:20px 16px;text-align:center;">
                    <div style="font-size:28px;line-height:1;">&#128197;</div>
                    <div style="font-size:10px;text-transform:uppercase;letter-spacing:1px;color:#9a7b4f;font-weight:700;margin-top:8px;">Event Date</div>
                    <div style="font-size:14px;color:#1a1a1a;font-weight:700;margin-top:4px;">{inquiry.event_date}</div>
                </div>
            </td>
            <!-- Event Type -->
            <td width="33%" style="padding:0 4px;">
                <div style="background:#fef3c7;border:1px solid #fcd34d;border-radius:12px;padding:20px 16px;text-align:center;">
                    <div style="font-size:28px;line-height:1;">&#127881;</div>
                    <div style="font-size:10px;text-transform:uppercase;letter-spacing:1px;color:#92400e;font-weight:700;margin-top:8px;">Event Type</div>
                    <div style="font-size:14px;color:#92400e;font-weight:700;margin-top:4px;">{inquiry.get_event_type_display()}</div>
                </div>
            </td>
            <!-- Duration -->
            <td width="33%" style="padding-left:8px;">
                <div style="background:#ecfdf5;border:1px solid #6ee7b7;border-radius:12px;padding:20px 16px;text-align:center;">
                    <div style="font-size:28px;line-height:1;">&#9200;</div>
                    <div style="font-size:10px;text-transform:uppercase;letter-spacing:1px;color:#065f46;font-weight:700;margin-top:8px;">Duration</div>
                    <div style="font-size:14px;color:#065f46;font-weight:700;margin-top:4px;">{inquiry.get_rental_duration_display()}</div>
                </div>
            </td>
        </tr>
        </table>
    </td></tr>

    <!-- MESSAGE BOX -->
    <tr><td style="padding:24px 40px 0;">
        <div style="background:#fafafa;border-radius:12px;border:1px solid #eee;padding:20px 24px;">
            <div style="font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#999;font-weight:700;margin-bottom:8px;">&#128172; Customer Message</div>
            <div style="font-size:15px;color:#333;line-height:1.7;white-space:pre-wrap;">{inquiry.message or "No additional message"}</div>
        </div>
    </td></tr>

    <!-- ACTION BUTTON -->
    <tr><td style="padding:28px 50px;" align="center">
        <a href="https://wa.me/{phone_wa}" style="display:block;background:linear-gradient(135deg,#25d366,#128c48);color:#ffffff;padding:16px 0;border-radius:12px;text-decoration:none;font-weight:700;font-size:16px;text-align:center;letter-spacing:0.5px;"><img src="https://cdn-icons-png.flaticon.com/128/3670/3670051.png" width="28" height="28" alt="WA" style="vertical-align:middle;margin-right:10px;"/>Chat on WhatsApp</a>
    </td></tr>

    <!-- FOOTER -->
    <tr><td style="background:linear-gradient(135deg,#0f2027 0%,#203a43 50%,#2c5364 100%);padding:28px 40px;text-align:center;">
        <p style="margin:0;color:#ffffff;font-size:20px;font-weight:700;font-family:Georgia,serif;letter-spacing:2px;">&#10024; AleeLights</p>
        <p style="margin:8px 0 0;color:rgba(255,255,255,0.65);font-size:13px;line-height:1.6;">Premium Light Decoration Rentals</p>
        <div style="width:40px;height:1px;background:rgba(255,255,255,0.2);margin:12px auto;"></div>
        <p style="margin:0;color:rgba(255,255,255,0.55);font-size:12px;">&#128205; Bahria Town, Lahore &nbsp;&bull;&nbsp; &#128222; +92 302 5329536</p>
        <p style="margin:6px 0 0;color:rgba(255,255,255,0.4);font-size:11px;">Auto-generated from aleelights&#8203;.com contact form</p>
    </td></tr>

</table>
</td></tr>
</table>
</body></html>'''
            email = EmailMessage(
                subject=subject,
                body=html_body,
                from_email=f'{inquiry.full_name} via AleeLights <{settings.EMAIL_HOST_USER}>',
                to=[settings.NOTIFY_EMAIL],
                reply_to=[inquiry.email],
                headers={'X-Customer-Name': inquiry.full_name, 'X-Customer-Email': inquiry.email},
            )
            email.content_subtype = 'html'
            email.send(fail_silently=True)
        except Exception:
            pass  # Email failure should not block the response
        return JsonResponse({
            'success': True,
            'message': 'Your inquiry has been received. We\'ll contact you within 24 hours.'
        })
    return JsonResponse({
        'success': False,
        'errors': form.errors
    }, status=400)
