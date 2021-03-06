"""
    Libsyn URL Pattern List.
"""
from django.conf.urls import url
from .views import ImportFromLibsynFormView, ImportFromLibsynResultsView

urlpatterns = (
    # Import Title
    url(r'^import/$', ImportFromLibsynFormView.as_view(), name="libsyn_import_view"),
    url(r'^import/results/$', ImportFromLibsynResultsView.as_view(), name="libsyn_import_results_view"),
    url(r'^import/slug/(?P<libsyn_slug>[\w-]+)/$', ImportFromLibsynResultsView.as_view(), name="libsyn_import_view_direct"),
)
