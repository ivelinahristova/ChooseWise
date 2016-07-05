from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from datetime import datetime
from django.utils import timezone
from dateutil.parser import parse
from datetime import date, timedelta
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        users = User.objects.filter(last_login__lte = date.today() - timedelta(days = 3))
        for user in users:
            self.stdout.write(('Successfully "%s"' % user.email))
            send_mail('Hello', 'World', 'iv4etoxx@gmail.com', [user.email, 'iv4eto_xx@abv.bg'])
            