from django.conf.urls import url

from .views import Index
from .views import StateView
from .views import StateData
from .views import CountyView
from .views import CountyData

app_name = 'tigerleaflet'
urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<state>[a-z_]+)$',
        StateView.as_view(),
        name='state'),
    url(r'^(?P<state>[a-z_]+)/(?P<county>[a-z_]+)$',
        CountyView.as_view(),
        name='county'),

    # geojson urls
    url(r'^state.geojson$',
        StateData.as_view(),
        name='state_data'),
    url(r'^county.geojson$',
        CountyData.as_view(),
        name='county_data'),
]
