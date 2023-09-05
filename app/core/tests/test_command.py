'''
test custom Django management commands
'''

from unittest.mock import patch

from psycopg2 import OperationalError as Pyscopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    '''test commands.'''
    def test_wait_for_db_ready(self, patched_check):
        '''test waiting for database if database is ready'''

        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        '''Test waiting for database when Operation Error return'''
        # Call the function 6 times, can change accordingly to operation
        patched_check.side_effect = [Pyscopg2Error]*2 + \
            [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
