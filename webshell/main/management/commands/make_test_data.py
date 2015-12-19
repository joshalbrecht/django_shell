from django.core.management.base import BaseCommand
from main.models import AWSTestModel

class Command(BaseCommand):

    def handle(self, *args, **options):
        model = AWSTestModel(random_text="hello world")
        model.save()
