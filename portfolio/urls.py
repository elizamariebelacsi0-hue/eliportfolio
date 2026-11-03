"""
URL configuration for portfolio project.
"""
from django.conf import settings
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from .projects_data import PROJECTS
from .skills_data import SKILL_COUNT, SKILL_GROUPS

CERTIFICATE_COUNT = 3

# Paste your profile links between the quotes. When a link is filled in,
# that row on the Contact page becomes clickable and opens in a new tab.
CONTACT_LINKS = {
    'facebook_url': 'https://www.facebook.com/share/1dkXNeVm6a/',
    'github_url': 'https://github.com/elizamariebelacsi0-hue',
}

site_stats = {
    'project_count': len(PROJECTS),
    'skill_count': SKILL_COUNT,
    'certificate_count': CERTIFICATE_COUNT,
}

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html', extra_context=site_stats), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html', extra_context=site_stats), name='about'),
    path('projects/', TemplateView.as_view(
        template_name='projects.html',
        extra_context={'projects': PROJECTS},
    ), name='projects'),
    path('certificates/', TemplateView.as_view(template_name='certificates.html'), name='certificates'),
    path('skills/', TemplateView.as_view(
        template_name='skills.html',
        extra_context={'skill_groups': SKILL_GROUPS, 'skill_count': SKILL_COUNT},
    ), name='skills'),
    path('contact/', TemplateView.as_view(template_name='contact.html', extra_context=CONTACT_LINKS), name='contact'),
]

# Photos and screenshots in media/ are part of the site itself (nobody uploads
# files here), so serve them on Vercel too, not only while DEBUG is on.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
