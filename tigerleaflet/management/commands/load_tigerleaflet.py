import datetime

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Installs the 2011-2016 TIGER/LINE files for states and counties'

    def add_arguments(self, parser):
        help_string = 'The directory where the TIGER/LINE data is stored.'
        parser.add_argument('--path', default='', dest='path',
                            help=help_string,
                            )

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        print("Begin: %s" % datetime.datetime.now())

        call_command('load_states', path=path)
        call_command('load_counties', path=path)

        print("All Finished: %s" % datetime.datetime.now())
