from django.conf.urls import url

from .views import CountryData
from .views import StateData
from .views import CountyData

app_name = 'tigerleaflet'
urlpatterns = [
    # geojson urls
    url(r'^country.geojson$',
        CountryData.as_view(),
        name='country_data'),
    url(r'^state.geojson$',
        StateData.as_view(),
        name='state_data'),
    url(r'^county.geojson$',
        CountyData.as_view(),
        name='county_data'),
]
