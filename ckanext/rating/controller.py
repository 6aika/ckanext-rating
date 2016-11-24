import ckan.plugins as p
import ckan.model as model
import ckan.logic as logic
from ckan.lib.base import h

c = p.toolkit.c
flatten_to_string_key = logic.flatten_to_string_key

class RatingController(p.toolkit.BaseController):

    def submit_package_rating(self, package, rating): 
        p.toolkit.get_action('rating_package_create')(
            context = {'model': model,
                   'user': c.user or c.author},
            data_dict={'package': package,
                       'rating': rating}
        )
        h.redirect_to(str('/dataset/' + package))
        return p.toolkit.render('package/read.html')

    def submit_showcase_rating(self, package, rating): 
        p.toolkit.get_action('rating_package_create')(
            context = {'model': model,
                   'user': c.user or c.author},
            data_dict={'package': package,
                       'rating': rating}
        )
        h.redirect_to(str('/showcase/' + package))
        return p.toolkit.render('showcase/showcase_info.html')

    def submit_ajax_package_rating(self, package, rating):
        try:
            p.toolkit.get_action('rating_package_create')(
                context = {'model': model,
                    'user': c.user or c.author},
                data_dict={'package': package,
                        'rating': rating}
            )
        except Exception, ex:
            errors = ex
        else:
            data['success'] = True

        data = flatten_to_string_key({ 'data': data, 'errors': errors }),
        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)