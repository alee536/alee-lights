// ==================== DARK MODE TOGGLE ====================
function toggleDarkMode() {
    var html = document.documentElement;
    if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    } else {
        html.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }
    updateDarkIcons();
}

function updateDarkIcons() {
    var isDark = document.documentElement.classList.contains('dark');
    document.querySelectorAll('.dark-icon-moon').forEach(function(el) {
        el.style.display = isDark ? 'none' : 'block';
    });
    document.querySelectorAll('.dark-icon-sun').forEach(function(el) {
        el.style.display = isDark ? 'block' : 'none';
    });
    document.querySelectorAll('.dark-label-text').forEach(function(el) {
        el.textContent = isDark ? 'Light Mode' : 'Dark Mode';
    });
}

document.addEventListener('DOMContentLoaded', function () {

    // Initialize dark mode icons
    updateDarkIcons();

    // ==================== HEADER SCROLL EFFECT ====================
    const header = document.getElementById('header');
    const isHome = document.getElementById('slide-indicators') !== null;
    function updateHeader() {
        if (!isHome || window.scrollY > 50) {
            header.classList.add('header-scrolled');
        } else {
            header.classList.remove('header-scrolled');
        }
    }
    updateHeader();
    window.addEventListener('scroll', updateHeader);

    // ==================== MOBILE MENU ====================
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIconOpen = document.getElementById('menu-icon-open');
    const menuIconClose = document.getElementById('menu-icon-close');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
            menuIconOpen.classList.toggle('hidden');
            menuIconClose.classList.toggle('hidden');
        });
    }

    mobileNavLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            mobileMenu.classList.add('hidden');
            menuIconOpen.classList.remove('hidden');
            menuIconClose.classList.add('hidden');
        });
    });

    // ==================== HERO SLIDER ====================
    const slides = document.querySelectorAll('.hero-slide');
    const indicatorsContainer = document.getElementById('slide-indicators');
    let currentSlide = 0;
    let slideInterval;

    const heroTitles = [
        'Transform Your Special Moments with Luxurious Outdoor Lighting',
        'Elegant Lighting for Every Occasion',
        'Professional Installation & Premium Quality'
    ];
    const heroSubtitles = [
        'Premium light decoration rentals for unforgettable celebrations',
        'Weddings, birthdays, corporate events, and more',
        '500+ happy clients, 1000+ successful events'
    ];

    // Create slide indicators
    if (slides.length > 0 && indicatorsContainer) {
        for (let i = 0; i < slides.length; i++) {
            const dot = document.createElement('button');
            dot.classList.add('slide-dot');
            if (i === 0) dot.classList.add('active');
            dot.setAttribute('aria-label', 'Go to slide ' + (i + 1));
            dot.addEventListener('click', function () {
                goToSlide(i);
            });
            indicatorsContainer.appendChild(dot);
        }
    }

    function goToSlide(index) {
        slides.forEach(function (slide) { slide.style.opacity = '0'; });
        slides[index].style.opacity = '1';
        currentSlide = index;

        // Update text
        const heroTitle = document.getElementById('hero-title');
        const heroSubtitle = document.getElementById('hero-subtitle');
        if (heroTitle && heroTitles[index]) heroTitle.textContent = heroTitles[index];
        if (heroSubtitle && heroSubtitles[index]) heroSubtitle.textContent = heroSubtitles[index];

        // Update indicators
        const dots = document.querySelectorAll('.slide-dot');
        dots.forEach(function (dot, i) {
            dot.classList.toggle('active', i === index);
        });

        resetTimer();
    }

    function nextSlide() {
        goToSlide((currentSlide + 1) % slides.length);
    }

    function prevSlide() {
        goToSlide((currentSlide - 1 + slides.length) % slides.length);
    }

    function resetTimer() {
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide, 5000);
    }

    // Navigation buttons
    const nextBtn = document.getElementById('next-slide');
    const prevBtn = document.getElementById('prev-slide');
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);

    // Start auto-play
    if (slides.length > 1) {
        slideInterval = setInterval(nextSlide, 5000);
    }

    // ==================== GALLERY FILTER + SHOW MORE ====================
    const GALLERY_LIMIT = 6;
    const filterBtns = document.querySelectorAll('.gallery-filter');
    const galleryItems = document.querySelectorAll('.gallery-item');
    const showMoreBtn = document.getElementById('gallery-show-more');
    const showMoreWrap = document.getElementById('gallery-show-more-wrap');
    let currentCategory = 'All';
    let galleryExpanded = false;

    function applyGalleryView() {
        let visibleCount = 0;
        let totalForCategory = 0;
        galleryItems.forEach(function (item) {
            const cat = item.getAttribute('data-category');
            const matchesCategory = (currentCategory === 'All' || cat === currentCategory);
            if (!matchesCategory) {
                item.style.display = 'none';
                return;
            }
            totalForCategory++;
            if (galleryExpanded || visibleCount < GALLERY_LIMIT) {
                item.style.display = '';
                visibleCount++;
            } else {
                item.style.display = 'none';
            }
        });
        // Show/hide the button
        if (showMoreWrap) {
            if (galleryExpanded) {
                showMoreBtn.innerHTML = '<i data-lucide="chevron-up" class="w-5 h-5 inline-block mr-1 align-middle"></i> Show Less';
                showMoreWrap.style.display = totalForCategory > GALLERY_LIMIT ? '' : 'none';
            } else {
                showMoreBtn.innerHTML = '<i data-lucide="chevron-down" class="w-5 h-5 inline-block mr-1 align-middle"></i> Show More';
                showMoreWrap.style.display = totalForCategory > GALLERY_LIMIT ? '' : 'none';
            }
            if (typeof lucide !== 'undefined') lucide.createIcons();
        }
    }

    // Initial view
    applyGalleryView();

    filterBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            currentCategory = this.getAttribute('data-category');
            galleryExpanded = false;

            // Update active button
            filterBtns.forEach(function (b) {
                b.classList.remove('bg-amber-500', 'text-white');
                b.classList.add('bg-gray-200', 'text-gray-800');
            });
            this.classList.remove('bg-gray-200', 'text-gray-800');
            this.classList.add('bg-amber-500', 'text-white');

            applyGalleryView();
        });
    });

    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', function () {
            galleryExpanded = !galleryExpanded;
            applyGalleryView();
        });
    }

    // ==================== LIGHTBOX ====================
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxClose = document.getElementById('lightbox-close');

    galleryItems.forEach(function (item) {
        item.addEventListener('click', function () {
            const img = this.querySelector('img');
            if (img && lightbox && lightboxImg) {
                lightboxImg.src = img.src;
                lightboxImg.alt = img.alt;
                lightbox.classList.add('active');
            }
        });
    });

    if (lightboxClose) {
        lightboxClose.addEventListener('click', function () {
            lightbox.classList.remove('active');
        });
    }

    if (lightbox) {
        lightbox.addEventListener('click', function (e) {
            if (e.target === lightbox) {
                lightbox.classList.remove('active');
            }
        });
    }

    // ==================== SCROLL TO TOP ====================
    const scrollTopBtn = document.getElementById('scroll-to-top');
    window.addEventListener('scroll', function () {
        if (scrollTopBtn) {
            if (window.scrollY > 400) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        }
    });

    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ==================== CONTACT FORM AJAX ====================
    const contactForm = document.getElementById('contact-form');
    const formContainer = document.getElementById('form-container');
    const formSuccess = document.getElementById('form-success');
    const submitBtn = document.getElementById('submit-btn');

    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(contactForm);
            submitBtn.textContent = 'Submitting...';
            submitBtn.disabled = true;

            fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                },
                body: formData,
            })
            .then(function (response) { return response.json(); })
            .then(function (data) {
                if (data.success) {
                    formContainer.classList.add('hidden');
                    formSuccess.classList.remove('hidden');

                    setTimeout(function () {
                        formContainer.classList.remove('hidden');
                        formSuccess.classList.add('hidden');
                        contactForm.reset();
                        submitBtn.textContent = 'Submit Inquiry';
                        submitBtn.disabled = false;
                    }, 5000);
                } else {
                    alert('Please check all fields and try again.');
                    submitBtn.textContent = 'Submit Inquiry';
                    submitBtn.disabled = false;
                }
            })
            .catch(function () {
                alert('An error occurred. Please try again or contact us at aleelights786@gmail.com');
                submitBtn.textContent = 'Submit Inquiry';
                submitBtn.disabled = false;
            });
        });
    }
});
