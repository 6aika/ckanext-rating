import sys

from ckan.plugins.toolkit import CkanCommand
import ckanext.rating.utils as utils

class RatingCommand(CkanCommand):
    '''
    Send notification emails of datasets which have a reminder date set

    Usage:

        paster rating init
            - Initializes database tables used by rating
    '''

    summary = __doc__.split('\n')[0]
    usage = __doc__
    min_args = 0
    max_args = 1

    def command(self):
        """
        Parse command line arguments and call appropriate method.
        """
        if not self.args or self.args[0] in ['--help', '-h', 'help']:
            self.parser.print_usage()
            sys.exit(1)

        cmd = self.args[0]
        self._load_config()

        if cmd == 'init':
            self.init_db()
        else:
            self.log.error('Command "%s" not recognized' % (cmd,))

    def init_db(self):
        utils.init_db()
