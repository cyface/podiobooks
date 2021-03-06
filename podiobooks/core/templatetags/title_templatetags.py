""" Tags used for working with Titles """
import feedparser

from django import template
from django.conf import settings
from django.contrib.sites.models import Site

from podiobooks.core.util import get_cover_url_at_width


register = template.Library()


@register.inclusion_tag('core/title/tags/show_awardshow.html')
def show_awardshow(title):
    """ Show a slideshow of all the awards for a title, used on title detail page """
    return {'award_list': title.awards.order_by('-date_updated').all()}


@register.inclusion_tag('core/title/tags/show_contributors.html')
def show_contributors(title, detail=False):
    """ standardize formatting for contributor list for a given title """
    return {"title": title, "detail": detail, "SITE": Site.objects.get_current()}


@register.inclusion_tag('core/title/tags/show_titlecover.html')
def show_titlecover(title, width):
    """Returns  Image Tag for Cover at Specified Width"""
    return {"title": title, "url": get_cover_url_at_width(title, width)}


@register.simple_tag()
def get_cover_url(title, width):
    """Returns the url to the cover image """
    return get_cover_url_at_width(title, width)


@register.inclusion_tag('core/title/tags/show_titlelist.html', takes_context=True)
def show_titlelist(context, title_list, page_name):
    """ Formats a list of titles, used on search, category, author list pages """
    return {'title_list': title_list, 'page_name': page_name, 'debug': settings.DEBUG}


@register.inclusion_tag('core/title/tags/show_episodelist.html')
def show_episodelist(title):
    """ Show a list of all the episodes for a title, used on title detail page """
    return {'episode_list': title.episodes.order_by('sequence').all()}


@register.inclusion_tag('core/title/tags/show_rating_icon.html')
def show_rating_icon(title):
    """ Show an icon indicating the rating of this title"""
    return {'title': title}


@register.inclusion_tag('core/title/tags/show_tipjar_button.html')
def show_tipjar_button(title):
    """ Show button to enable people to tip the author of this title """
    return {'title': title, 'TIPJAR_BUSINESS_NAME': settings.TIPJAR_BUSINESS_NAME}


@register.inclusion_tag('core/title/tags/show_comments.html')
def show_comments(podiobooker_url):
    """Pulls in a template to show a list of comments"""

    feed_url = podiobooker_url.rstrip('/') + '/feed/'

    feed = feedparser.parse(feed_url)
    if feed.entries:
        entries = feed.entries
    else:
        entries = []

    return {'comments': entries, 'podiobooker_url': podiobooker_url}


@register.filter
def count_titles(something):
    """
    Count how many undeleted titles exist for a given something

    Handles both 1-M relations and M-M relations
    """
    some_titles = []
    try:
        some_titles += [title for title in something.title_set.all() if not title.deleted]
    except AttributeError:
        some_titles += [title for title in something.titles.all() if not title.deleted]
    return len(some_titles)
