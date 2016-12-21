from django.contrib.gis import admin

from tigerleaflet.models import County
from tigerleaflet.models import State


class StateAdmin(admin.OSMGeoAdmin):
    list_display = ('name',
                    'usps_code',
                    'fips_code',
                    'area_description_code',
                    'feature_class_code',
                    'functional_status'
                   )


class CountyAdmin(admin.OSMGeoAdmin):
    list_display = ('name',
                    'county_identifier',
                    'legal_statistical_description',
                    'fips_55_class_code',
                    'feature_class_code',
                    'functional_status'
                   )
    search_fields = ('name', 'state_fips_code')


admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
