from ckanext.rating.model import Rating
from ckan.plugins import toolkit
import ckan.model as model

c = toolkit.c

def get_user_rating(package_id):
    context = {'model': model, 'user': c.user}

    from ckan.model import User
    if not isinstance(context.get('user'), User):
        user = toolkit.request.environ.get('REMOTE_ADDR')

    user_rating = Rating.get_user_package_rating(user, package_id).first()
    return user_rating.rating if user_rating is not None else None
