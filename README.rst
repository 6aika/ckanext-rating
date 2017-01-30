=============
CKAN Rating extension
=============

This is a simple rating extension for CKAN datasets (packages) and showcases. The extension adds a list of clickable stars to the side navigation
in the dataset and showcacse templates similar to ckanext-qa. In showcase the stars are also displayed in the showcase listing, but are not clickable.

The stars can also be added to any desired view by adding the following code to the desired template::

    {% snippet "rating/snippets/stars.html", package=<YOUR_PACKAGE> %}

The amount of ratings submitted can also be displayed with::

    {{h.package_rating(None, {'package_id' : <YOUR_PACKAGE>.id} ).ratings_count}}

Rating is identified with client IP if the user is not authenticated. User ID is saved with the rating when authenticated.


------------
Requirements
------------

This extension works with CKAN version 2.5 or later.


------------
Installation
------------

To install ckanext-rating:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-rating Python package into your virtual environment::
     pip install -e git+https://github.com/6aika/ckanext-rating.git#egg=ckanext-rating

3. Add ``rating`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

5. Initialize database tables used by Rating::

    paster --plugin=ckanext-rating rating init --config=production.ini

6. If you want to use this extension for ckanext-showcase, install it into your environment by following the instructions at https://github.com/ckan/ckanext-showcase


---------------
Config Settings
---------------

Rating is enabled or disabled for unauthenticated users::

  rating.enabled_for_unauthenticated_users = true or false

Optional::

    # List of dataset types for which the rating will be shown (defaults to ['dataset'])
    ckanext.rating.enabled_dataset_types


------------------------
Development Installation
------------------------

To install ckanext-rating for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/6aika/ckanext-rating.git
    cd ckanext-rating
    python setup.py develop
    pip install -r dev-requirements.txt
