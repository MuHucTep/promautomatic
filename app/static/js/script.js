document.addEventListener("DOMContentLoaded", () => {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navList = document.querySelector('.nav-list');

    if (menuToggle && navList) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            navList.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const navLinks = navList.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navList.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!menuToggle.contains(e.target) && !navList.contains(e.target)) {
                menuToggle.classList.remove('active');
                navList.classList.remove('active');
            }
        });
    }

    // Fade-in animations
    const animatedElements = document.querySelectorAll('.fade-in-bottom');
    if (animatedElements.length === 0) return;

    // 1. Сразу показываем элементы, которые находятся в верхней части страницы (первый экран)
    animatedElements.forEach(element => {
        const rect = element.getBoundingClientRect();
        // Если верх элемента находится в пределах экрана при загрузке
        if (rect.top < window.innerHeight) {
            element.classList.add('visible');
        }
    });

    let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;

    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Если скролл у самого верха, принудительно считаем направление как "вниз",
        // чтобы верхние блоки не исчезали из-за погрешности расчетов
        const isScrollingDown = scrollTop <= 0 ? true : scrollTop > lastScrollTop;

        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Появляются только при скролле вниз
                if (isScrollingDown) {
                    entry.target.classList.add('visible');
                }
            } else {
                // Сбрасываем анимацию ТОЛЬКО если скроллим вверх
                // И элемент ушел именно за НИЖНЮЮ границу экрана
                if (!isScrollingDown && entry.boundingClientRect.top > 0) {
                    entry.target.classList.remove('visible');
                }
            }
        });

        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    }, options);

    animatedElements.forEach(element => {
        observer.observe(element);
    });
});