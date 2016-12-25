=============================
geodjango-tigerleaflet
=============================

Leaflet setup for US Tiger State and County data

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

Todo
--------

* Push models back into geodjango-tigerline once it's upgraded to use Django 1.10
* Make the current templates more generic through the use of template tags, needs to be coupled with the provided javascript
* Better documentation on pypi
* Offer direct download and import of census data (like django-brasil-municipios)

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  `geodjango-tigerline`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _`geodjango-tigerline`_: https://github.com/adamfast/geodjango-tigerline
