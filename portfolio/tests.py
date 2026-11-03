from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase
from django.utils.html import escape


class PortfolioPageTests(SimpleTestCase):
    def test_theme_toggle_is_in_shared_navigation(self):
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'class="theme-toggle"')
        self.assertContains(response, 'Switch to dark mode')

    def test_home_is_one_intro_section_with_lanyard_and_no_portfolio_screen(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="home"')
        self.assertContains(response, '<section', count=1)
        self.assertContains(response, 'Hi,')
        self.assertNotContains(response, 'portfolio-title')
        self.assertNotContains(response, 'home_pic.jpg')
        self.assertContains(response, '/media/lanyard_pic.jpg')
        self.assertNotContains(response, 'Enter Site')

    def test_about_contains_two_sections_and_bounce_cards(self):
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="about"')
        self.assertContains(response, 'id="more-about"')
        self.assertContains(response, '/media/more_about_me_fixed.png')
        self.assertContains(response, 'id="bounce-cards-root"')
        self.assertContains(response, 'data-photo', count=9)

        for index in range(1, 10):
            self.assertContains(response, f'/media/{index}few_shots.jpg')

    def test_named_media_images_exist(self):
        for filename in (
            'lanyard_pic.jpg',
            'home_pic.jpg',
            'more_about_me_fixed.png',
            'lungcheck.jpg',
            'payflow.png',
            *(f'{index}few_shots.jpg' for index in range(1, 10)),
        ):
            with self.subTest(filename=filename):
                image_path = Path(settings.MEDIA_ROOT, filename)
                self.assertTrue(image_path.is_file())
                self.assertGreater(image_path.stat().st_size, 0)

    def test_project_cards_use_pneumonia_and_payflow_images(self):
        response = self.client.get('/projects/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/media/fiscal.jpg')
        self.assertContains(response, '/media/lungcheck.jpg')
        self.assertContains(response, '/media/payflow.png')
        self.assertContains(response, '/media/serenity-tours.jpg')
        self.assertContains(response, 'Serenity Tours')
        self.assertContains(response, 'id="projects-marquee"')
        self.assertNotContains(response, 'project-toggle')

    def test_every_project_card_opens_a_case_study(self):
        from .projects_data import PROJECTS

        response = self.client.get('/projects/')

        self.assertContains(response, 'id="case-dialog"')
        self.assertContains(response, 'data-case-panel=', count=len(PROJECTS))
        for project in PROJECTS:
            with self.subTest(project=project['slug']):
                # one trigger on the sliding card, one in the project index
                self.assertContains(response, f'data-case="{project["slug"]}"', count=2)
                self.assertContains(response, f'id="case-{project["slug"]}"')
                for feature in project['features']:
                    self.assertContains(response, escape(feature))

    def test_skills_page_has_orbit_and_icon_tiles(self):
        from .skills_data import SKILL_COUNT, SKILL_GROUPS

        response = self.client.get('/skills/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="skills-orbit"')
        self.assertContains(response, 'class="orbit-item"', count=SKILL_COUNT)
        self.assertContains(response, 'class="skill-tile"', count=SKILL_COUNT)
        for group in SKILL_GROUPS:
            for skill in group['skills']:
                with self.subTest(skill=skill['name']):
                    self.assertContains(response, skill['name'])
                    icon = Path(settings.BASE_DIR, 'static', 'images', 'skills', f"{skill['icon']}.svg")
                    self.assertTrue(icon.is_file())

    def test_intelliguide_is_fifth_project_with_team(self):
        response = self.client.get('/projects/')

        self.assertContains(response, 'id="case-intelliguide"')
        self.assertContains(response, '<span class="kicker-no">05</span>')
        for name, role in (
            ('Eliza Marie Rosario', 'Team Leader'),
            ('Christine Elaine Oliverio', 'Assistant Team Leader'),
            ('Marjon Vera', 'Developer'),
            ('Carl Marco Vaporoso', 'Assistant Developer'),
        ):
            with self.subTest(member=name):
                self.assertContains(response, name)
                self.assertContains(response, f'<span class="case-team-role">{role}</span>')
        self.assertContains(response, '<dt>Context</dt><dd>School Project</dd>', count=4)
        self.assertContains(response, '<dt>Context</dt><dd>Thesis Project</dd>', count=1)
        self.assertContains(response, 'Assistive technology for visually impaired persons')
        self.assertContains(response, '<dt>Platform</dt><dd>Mobile App</dd>')
        for shot in ('intelliguide-camera.png', 'intelliguide-map.png', 'intelliguide-settings.png'):
            with self.subTest(shot=shot):
                self.assertContains(response, f'/media/{shot}')
                self.assertTrue(Path(settings.MEDIA_ROOT, shot).is_file())
        for tool in ('Flutter', 'Dart', 'TensorFlow Lite', 'YOLOv8 Nano', 'CNN + ViT', 'Hive'):
            with self.subTest(tool=tool):
                self.assertContains(response, f'<span class="project-tag">{tool}</span>')

    def test_certificates_include_cisco_networking_basics(self):
        response = self.client.get('/certificates/')

        self.assertContains(response, 'class="certificate-card', count=3)
        self.assertContains(response, 'Networking Basics')
        for image in ('cert-cisco-networking-basics.jpg', 'cert-cisco-networking-basics-award.jpg'):
            with self.subTest(image=image):
                self.assertContains(response, f'/media/{image}')
                self.assertTrue(Path(settings.MEDIA_ROOT, image).is_file())

        home = self.client.get('/')
        self.assertContains(home, '<dt>Certificates</dt><dd>03</dd>')

    def test_facebook_and_github_rows_become_links_when_urls_are_set(self):
        from django.template.loader import render_to_string
        from django.test import RequestFactory
        from django.urls import resolve

        request = RequestFactory().get('/contact/')
        request.resolver_match = resolve('/contact/')
        html = render_to_string('contact.html', {
            'facebook_url': 'https://www.facebook.com/sample.page',
            'github_url': 'https://github.com/sampleuser',
        }, request=request)

        self.assertIn('href="https://www.facebook.com/sample.page"', html)
        self.assertIn('href="https://github.com/sampleuser"', html)

    def test_contact_page_links_to_facebook_and_github(self):
        response = self.client.get('/contact/')

        self.assertContains(response, 'href="https://www.facebook.com/share/1dkXNeVm6a/"')
        self.assertContains(response, 'href="https://github.com/elizamariebelacsi0-hue"')

    def test_contact_page_shows_requested_contact_methods(self):
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 200)
        for contact in ('Email', 'Phone', 'WhatsApp', 'Facebook', 'Eli Belacsi', 'GitHub'):
            with self.subTest(contact=contact):
                self.assertContains(response, contact)

        # Each link must go where its visible text says it goes
        self.assertContains(response, 'href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=elxxbel@gmail.com"')
        self.assertContains(response, 'elxxbel@gmail.com</span>')
        # Phone number is shown as plain text, not a link
        self.assertContains(response, '09260726050</span>')
        self.assertNotContains(response, 'href="tel:')
        self.assertContains(response, 'href="https://wa.me/639260726050"')
        self.assertNotContains(response, 'elxx@gmail.com')
        self.assertNotContains(response, '09876543212')
