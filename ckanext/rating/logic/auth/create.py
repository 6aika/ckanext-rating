import ckantoolkit as config
from ckan.plugins import toolkit
import ckan.logic as logic
c = toolkit.c


def rating_create_auth():
    return {
        'check_access_user': check_access_user,
    }


@logic.auth_allow_anonymous_access
def check_access_user(context, data_dict):
    if c.user:
        return {'success': True}
    else:
        allow_rating = toolkit.asbool(
            config.get('ckanext.rating.enabled_for_unauthenticated_users', True))
    return {'success': allow_rating}
