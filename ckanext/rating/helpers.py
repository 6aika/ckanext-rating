from ckanext.rating.model import Rating
from ckan.plugins import toolkit
from pylons import config

c = toolkit.c


def get_user_rating(package_id):
    if not c.userobj:
        user = toolkit.request.environ.get('REMOTE_ADDR')
    else:
        user = c.userobj
    user_rating = Rating.get_user_package_rating(user, package_id).first()
    return user_rating.rating if user_rating is not None else None


def show_rating_in_type(type):
    return type in config.get('ckanext.rating.enabled_dataset_types',
                              ['dataset'])
