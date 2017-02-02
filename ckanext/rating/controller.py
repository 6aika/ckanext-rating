import ckan.plugins as p
import ckan.model as model
import ckan.logic as logic
from ckan.lib.base import h
from ckan.controllers.package import PackageController
from ckan.common import request

c = p.toolkit.c
flatten_to_string_key = logic.flatten_to_string_key


class RatingController(p.toolkit.BaseController):

    def submit_package_rating(self, package, rating):
        context = {'model': model, 'user': c.user or c.author}
        data_dict = {'package': package, 'rating': rating}
        if p.toolkit.check_access('check_access_user', context, data_dict):
            p.toolkit.get_action('rating_package_create')(context, data_dict)
            h.redirect_to(str('/dataset/' + package))
            return p.toolkit.render('package/read.html')

    def submit_showcase_rating(self, package, rating):
        context = {'model': model, 'user': c.user or c.author}
        data_dict = {'package': package, 'rating': rating}
        if p.toolkit.check_access('check_access_user', context, data_dict):
            p.toolkit.get_action('rating_package_create')(context, data_dict)
            h.redirect_to(str('/showcase/' + package))
            return p.toolkit.render('showcase/showcase_info.html')

    def submit_ajax_package_rating(self, package, rating):
        context = {'model': model, 'user': c.user or c.author}
        data_dict = {'package': package, 'rating': rating}
        if p.toolkit.check_access('check_access_user', context, data_dict):
            try:
                p.toolkit.get_action('rating_package_create')(
                    context, data_dict)
            except Exception, ex:
                errors = ex
            else:
                data['success'] = True

            data = flatten_to_string_key({'data': data, 'errors': errors}),
            response.headers['Content-Type'] = 'application/json;charset=utf-8'
            return h.json.dumps(data)


class RatingPackageController(PackageController):

    def search(self):
        cur_page = request.params.get('page')
        if cur_page is not None:
            c.current_page = self._get_page_number(request.params)
        else:
            c.current_page = 1
        c.pkg_type = 'dataset'
        result = super(RatingPackageController, self).search()
        return result
