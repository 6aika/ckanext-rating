from flask import Blueprint

import ckanext.rating.utils as utils

rating = Blueprint('rating', __name__)

def submit_package_rating(package, rating):
    return utils.submit_package_rating(package, rating)
    
def submit_showcase_rating(package, rating):
    return utils.submit_showcase_rating(package, rating)


rating.add_url_rule('/rating/dataset/<package>/<rating>', view_func=submit_package_rating, endpoint='submit_package_rating')
rating.add_url_rule('/rating/showcase/<package>/<rating>', view_func=submit_showcase_rating, endpoint='submit_showcase_rating')