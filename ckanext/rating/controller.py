import ckan.plugins as p
from ckan.controllers.package import PackageController
import ckanext.rating.utils as utils

class RatingController(p.toolkit.BaseController):

    def submit_package_rating(self, package, rating):
        return utils.submit_package_rating(package, rating)
        
    def submit_showcase_rating(self, package, rating):
        return utils.submit_showcase_rating(package, rating)
