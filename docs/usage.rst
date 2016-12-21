=====
Usage
=====

To use geodjango-tigerleaflet in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tigerleaflet.apps.TigerleafletConfig',
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
