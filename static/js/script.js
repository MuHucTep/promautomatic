document.addEventListener("DOMContentLoaded", () => {
    const animatedElements = document.querySelectorAll('.fade-in-bottom');
    if (!animatedElements.length) return;

    animatedElements.forEach(el => {
        if (el.getBoundingClientRect().top < window.innerHeight) {
            el.classList.add('visible');
        }
    });

    let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;

    const observer = new IntersectionObserver((entries) => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const isScrollingDown = scrollTop <= 0 || scrollTop > lastScrollTop;

        entries.forEach(entry => {
            if (entry.isIntersecting && isScrollingDown) {
                entry.target.classList.add('visible');
            } else if (!isScrollingDown && entry.boundingClientRect.top > 0) {
                entry.target.classList.remove('visible');
            }
        });

        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    }, { threshold: 0.1 });

    animatedElements.forEach(el => observer.observe(el));
});