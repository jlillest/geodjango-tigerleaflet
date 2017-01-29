=============================
geodjango-tigerleaflet
=============================

Make use of Geodjango, Leaflet.js, US Census TIGER data to allow navigation through
 data related to US States and Counties

Quickstart
----------

Install geodjango-tigerleaflet::

    pip install geodjango-tigerleaflet

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tigerleaflet',
        ...
    )

Add geodjango-tigerleaflet's URL patterns:

.. code-block:: python

    from tigerleaflet import urls as tigerleaflet_urls


    urlpatterns = [
        ...
        url(r'^', include(tigerleaflet_urls)),
        ...
    ]

Features
--------

* GeoJson urls for easy map creation
* example Leaflet pages for displaying and navigating through state/county data
* template tags for users to use in their own templates

Todo
--------

* Push models back into geodjango-tigerline once it's upgraded to use Django 1.10
* Better documentation on pypi
* Better examples, even with some adding data on top of states/counties showcasing use of leaflet library
* Offer direct download and import of census data (like django-brasil-municipios)

Credits
-------

Tools/packages used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  `geodjango-tigerline`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _`geodjango-tigerline`_: https://github.com/adamfast/geodjango-tigerline

