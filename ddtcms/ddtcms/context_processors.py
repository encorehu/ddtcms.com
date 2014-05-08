import random

from django.utils import timezone
from django import get_version as django_version
from django.core.cache import cache
from django.conf import settings

def site(request):
    """
    Adds site-related context variables to the context.
    """
    return {
        'DJANGO_VERSION': django_version(),
        'DDTCMS_VERSION': '0.6',
        'SITE_NAME':    'DDTCMS.com',
        'DEBUG':    settings.DEBUG,
        'system_version': '0.1',
    }
