=====
Usage
=====

To use geodjango-tigerleaflet in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tigerleaflet',
        ...
    )

Add geodjango-tigerleaflet's URL patterns, and views to show the desired maps:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'tigerleaflet/$', CountryView.as_view(), name='country'), 
        url(r'tigerleaflet/(?P<state>[a-z_]+)$', StateView.as_view(), name='state'),
        url(r'tigerleaflet/(?P<state>[a-z_]+)/(?P<county>[a-z_]+)$', CountyView.as_view(), name='county'),
        url(r'^tigerleaflet/', include('tigerleaflet.urls')),
        ...
    ]

Add views to your projects views to provide relevant data:

.. code-block:: python

    class CountryView(TemplateView):
        template_name = "country.html"

        def get_context_data(self, **kwargs):
            return { 'title': "Map of US States shown here"}

    class StateView(TemplateView):
        template_name = "state.html"

        def get_context_data(self, **kwargs):
            state_code = self.kwargs['state']
            state_name = State.objects.get(usps_code=state_code.upper()).name
            context = { 'title': state_name,
                        'state': state_code
                        }
            return context

    class CountyView(TemplateView):
        template_name = "county.html"

        def get_context_data(self, **kwargs):
            state_code = self.kwargs['state']
            county = self.kwargs['county']
            state_name = State.objects.get(usps_code=state_code.upper()).name
            county_name = county.replace('_', ' ').title()
            context = { 'title' : county_name + ", " + state_name,
                        'state' : state_code,
                        'county': county,
                        }
            return context

Then add the desired templates (country.html example shown here):

.. code-block:: python

    {% load tigerleaflet_tags %}

    <html>
      <head>
        <title>{{ title }}</title>
        {% init_tigerleaflet_map %}
      </head>
      <body>
        {% show_tigerleaflet_country 'map' "/tigerleaflet/" 37.22 -90.41 3 %}
      </body>
    </html>

