'''
Django command to wait for database to be available
'''

from django.core.management.base import BaseCommand

class Command(BaseCommand):
  '''Django to wait for database'''
  def handle(self,*args,**options):
    pass