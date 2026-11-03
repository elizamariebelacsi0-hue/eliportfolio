document.addEventListener('DOMContentLoaded', function() {
    /* ---------------- Theme toggle ---------------- */
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        const updateThemeToggle = () => {
            const isDark = document.documentElement.dataset.theme === 'dark';
            themeToggle.setAttribute('aria-pressed', String(isDark));
            themeToggle.setAttribute('aria-label', `Switch to ${isDark ? 'light' : 'dark'} mode`);
        };

        updateThemeToggle();
        themeToggle.addEventListener('click', function() {
            const isDark = document.documentElement.dataset.theme !== 'dark';
            document.documentElement.dataset.theme = isDark ? 'dark' : 'light';
            try {
                localStorage.setItem('portfolio-theme', isDark ? 'dark' : 'light');
            } catch {}
            updateThemeToggle();
        });
    }

    /* ---------------- Smooth in-page links ---------------- */
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.length < 2) return;
            const target = document.getElementById(href.slice(1));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    /* ---------------- Gentle fade-in on scroll ---------------- */
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                el.classList.add('animate-in');
                observer.unobserve(el);
                setTimeout(() => el.style.setProperty('--reveal-delay', '0ms'), 1200);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('.reveal').forEach((el, i) => {
        el.style.setProperty('--reveal-delay', `${(i % 4) * 110}ms`);
        observer.observe(el);
    });

    /* ---------------- Projects: sliding cards ---------------- */
    const marquee = document.getElementById('projects-marquee');
    if (marquee) {
        const track = marquee.querySelector('.projects-track');
        const set = track.querySelector('.projects-set');
        const originals = [...set.children];

        // Copies stay clickable (they open the same case study) but are
        // hidden from screen readers and skipped by the Tab key.
        const makeDecorative = node => {
            node.setAttribute('aria-hidden', 'true');
            node.querySelectorAll('button, a').forEach(el => el.setAttribute('tabindex', '-1'));
            node.querySelectorAll('img').forEach(img => img.removeAttribute('loading'));
            return node;
        };

        // On wide screens, repeat cards until one set is wider than the viewport
        for (let i = 0; set.scrollWidth < marquee.clientWidth && i < 6; i++) {
            originals.forEach(card => set.appendChild(makeDecorative(card.cloneNode(true))));
        }
        track.appendChild(makeDecorative(set.cloneNode(true)));

        // ~6s per card: clearly moving, still slow enough to read
        const cards = set.querySelectorAll('.project-card').length;
        marquee.style.setProperty('--marquee-duration', `${Math.max(cards, 3) * 6}s`);
        marquee.classList.add('is-running');
    }

    /* ---------------- Projects: case-study dialog ---------------- */
    const caseDialog = document.getElementById('case-dialog');
    if (caseDialog) {
        const panels = [...caseDialog.querySelectorAll('[data-case-panel]')];
        const scroller = caseDialog.querySelector('.case-scroll');
        const label = document.getElementById('case-dialog-title');
        let current = 0;

        const show = index => {
            current = (index + panels.length) % panels.length;
            panels.forEach((panel, i) => { panel.hidden = i !== current; });
            const panel = panels[current];
            label.textContent = `Case study · ${panel.querySelector('.case-title').textContent}`;
            scroller.scrollTop = 0;
        };

        document.addEventListener('click', e => {
            const trigger = e.target.closest('[data-case]');
            if (!trigger) return;
            const index = panels.findIndex(p => p.dataset.casePanel === trigger.dataset.case);
            if (index < 0) return;
            show(index);
            marquee?.classList.add('is-paused');
            caseDialog.showModal();
        });

        caseDialog.querySelectorAll('.case-nav').forEach(btn => {
            btn.addEventListener('click', () => show(current + Number(btn.dataset.step)));
        });

        caseDialog.addEventListener('keydown', e => {
            if (e.key === 'ArrowRight') show(current + 1);
            if (e.key === 'ArrowLeft') show(current - 1);
        });

        // Click on the dimmed backdrop closes the dialog
        caseDialog.addEventListener('click', e => {
            if (e.target === caseDialog) caseDialog.close();
        });

        caseDialog.addEventListener('close', () => {
            marquee?.classList.remove('is-paused');
            if (location.hash.startsWith('#case-')) history.replaceState(null, '', location.pathname);
        });

        // Shareable links: /projects/#case-serenity opens that case study
        const openFromHash = () => {
            const index = panels.findIndex(p => `#${p.id}` === location.hash);
            if (index < 0) return;
            show(index);
            if (!caseDialog.open) caseDialog.showModal();
        };
        openFromHash();
        window.addEventListener('hashchange', openFromHash);
    }

    /* ---------------- Skills: tile ↔ orbit highlight ---------------- */
    const orbit = document.getElementById('skills-orbit');
    if (orbit) {
        document.querySelectorAll('.skill-tile[data-skill]').forEach(tile => {
            const targets = orbit.querySelectorAll(`.orbit-item[data-skill="${tile.dataset.skill}"]`);
            tile.addEventListener('mouseenter', () => {
                targets.forEach(item => item.classList.add('is-lit'));
                orbit.classList.add('is-paused');
            });
            tile.addEventListener('mouseleave', () => {
                targets.forEach(item => item.classList.remove('is-lit'));
                orbit.classList.remove('is-paused');
            });
        });
    }

    /* ---------------- Certificates: lightbox ---------------- */
    const lightbox = document.getElementById('certificate-lightbox');
    if (lightbox) {
        const image = document.getElementById('lightbox-image');
        const title = document.getElementById('lightbox-title');
        document.querySelectorAll('[data-lightbox]').forEach(trigger => {
            trigger.addEventListener('click', () => {
                image.src = trigger.dataset.src;
                image.alt = trigger.querySelector('img')?.alt || '';
                title.textContent = trigger.dataset.title || '';
                lightbox.showModal();
            });
        });
        lightbox.addEventListener('click', e => {
            if (e.target === lightbox) lightbox.close();
        });
    }

    /* ---------------- Contact: live local time in Biliran ---------------- */
    const clock = document.getElementById('local-time');
    if (clock) {
        const format = new Intl.DateTimeFormat('en-US', {
            timeZone: 'Asia/Manila',
            hour: 'numeric',
            minute: '2-digit',
        });
        const tick = () => { clock.textContent = format.format(new Date()); };
        tick();
        setInterval(tick, 15000);
    }
});
