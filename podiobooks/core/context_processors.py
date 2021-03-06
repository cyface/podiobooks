"""
Special Context Processors (adds variables to template contexts) for Podiobooks
"""

# pylint: disable=W0613

from django.conf import settings
from django.contrib.sites.models import Site


def js_api_keys(request):
    """
    Adds JavaScript API Keys variables to the context.
    """
    return {
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID
    }


def current_site(request):
    """Adds current site object to context"""
    return {'SITE': Site.objects.get_current()}


def feed_settings(request):
    """Adds settings to use for feeds to context."""
    return {
        'FEED_URL': settings.FEED_URL,
    }
