import ckan.plugins as p
import ckan.model as model
import ckan.logic as logic
from ckan.lib.base import h
from ckan.common import request, _
import ckan.lib.base as base
from ckanext.rating.model import init_tables

c = p.toolkit.c
flatten_to_string_key = logic.flatten_to_string_key
NotAuthorized = logic.NotAuthorized
abort = base.abort

def submit_package_rating(package, rating):
    context = {'model': model, 'user': c.user or c.author}
    data_dict = {'package': package, 'rating': rating}
    try:
        p.toolkit.check_access('check_access_user', context, data_dict)
        p.toolkit.get_action('rating_package_create')(context, data_dict)
        h.redirect_to(controller='package', action='read', id=package)
    except NotAuthorized:
        abort(403, _('Unauthenticated user not allowed to submit ratings.'))

def submit_showcase_rating(package, rating):
    context = {'model': model, 'user': c.user or c.author}
    data_dict = {'package': package, 'rating': rating}
    try:
        p.toolkit.check_access('check_access_user', context, data_dict)
        p.toolkit.get_action('rating_package_create')(context, data_dict)
        h.redirect_to(controller='ckanext.sixodp_showcase.controller:Sixodp_ShowcaseController', action='read', id=package)
    except NotAuthorized:
        abort(403, _('Unauthenticated user not allowed to submit ratings.'))

def init_db():
    init_tables(model.meta.engine)