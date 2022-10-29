from django.core.management.base import BaseCommand
from utils.coins import CoinApi


class Command(BaseCommand):
    help = 'Web scraping of CoinsApi '

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS(
                'Start scraping of CoreApi webpage'))
            if CoinApi().execute():
                self.stdout.write(self.style.SUCCESS(
                    'Successful scraping of CoreApi webpage'))
            else:
                self.stdout.write(self.style.ERROR(
                    'Fail scraping of CoreApi webpage'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                'Error scraping of CoreApi webpage' + str(e)))

