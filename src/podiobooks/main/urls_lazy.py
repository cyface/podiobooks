"""URL Definitions for the Main Podiobooks Module"""

# pylint: disable=W0401,W0614,C0103

from django.conf.urls.defaults import * #@UnusedWildImport
from podiobooks.main.models import * #@UnusedWildImport

urlpatterns = patterns('',
    url(r'^featured/','main.views.lazy.homepage_featured',name="lazy_load_featured_title"),
)
