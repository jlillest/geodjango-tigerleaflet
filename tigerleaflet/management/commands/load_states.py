import datetime
import os
import sys

from django.conf import settings
from django.core.management.base import BaseCommand

try:
    from django.contrib.gis.utils import LayerMapping
except ImportError:
    print("gdal is required")
    sys.exit(1)

from tigerleaflet.models import State


def state_import(state_shp, year):
    state_mapping = {
        'fips_code': 'STATEFP',
        'usps_code': 'STUSPS',
        'name': 'NAME',
        'area_description_code': 'LSAD',
        'feature_class_code': 'MTFCC',
        'functional_status': 'FUNCSTAT',
        'mpoly': 'POLYGON',
    }
    lm = LayerMapping(State, state_shp, state_mapping)
    lm.save(verbose=True)


class Command(BaseCommand):
    help = 'Installs the 2011-2016 tigerline files for states'

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
            help='The directory where the state data is stored.'
        )

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        # figure out which path we want to use.
        years = ["2016", "2015", "2014", "2013", "2012", "2011"]
        directories = [('tl_%s_us_state' % year, year) for year in years]

        tiger_file = ""
        for (directory, year) in directories:
            if os.path.exists(os.path.join(path, directory)):
                print('Found %s files.' % year)
                tiger_file = os.path.join(path, directory + "/" + directory + ".shp")
                file_found = True
                break

        if not tiger_file:
            print('Could not find files.')
            exit()

        print("Start States: %s" % datetime.datetime.now())
        state_import(tiger_file, year)
        print("End States: %s" % datetime.datetime.now())
