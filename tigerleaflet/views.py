from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import View

from tigerleaflet.models import County
from tigerleaflet.models import State


def get_geojson(data, fields):
    return serialize('geojson', data, geometry_field='mpoly', fields=fields)


class CountryData(View):
    fields = ('name', 'usps_code', 'fips_code')

    def post(self, request):
        map_data = State.objects.raw(
            'SELECT id, ST_simplify(mpoly, 0.1) AS mpoly,'
            ' name, usps_code, fips_code'
            ' FROM tigerleaflet_state')
        geojson = get_geojson(map_data, self.fields)

        return HttpResponse(geojson, content_type='application/json')


class StateData(View):
    fields = ('name', 'usps_code', 'fips_code')

    def post(self, request):
        usps_code = self.request.POST['state'].upper()
        map_data = County.objects.raw(
            'SELECT id, ST_simplify(mpoly, 0.01) AS mpoly,'
            ' name, fips_code, usps_code FROM tigerleaflet_county'
            ' WHERE usps_code=%s', [usps_code],
        )
        geojson = get_geojson(map_data, self.fields)

        return HttpResponse(geojson, content_type='application/json')


class CountyData(View):
    fields = ('name', 'fips_code', 'usps_code')

    def post(self, request):
        usps_code = self.request.POST['state'].upper()
        county_name = self.request.POST['county'].replace("_", " ").title()
        map_data = County.objects.raw(
            'SELECT id, mpoly,'
            ' name, usps_code FROM tigerleaflet_county'
            ' WHERE usps_code=%s AND name=%s',
            [usps_code, county_name],
        )
        geojson = get_geojson(map_data, self.fields)

        return HttpResponse(geojson, content_type='application/json')
