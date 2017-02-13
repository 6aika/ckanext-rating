from .create import rating_create_auth


def get_rating_auth_dict():
    rating_auth = dict()
    rating_auth.update(rating_create_auth())
    return rating_auth
