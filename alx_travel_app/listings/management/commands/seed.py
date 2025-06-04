import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Clean up old data if necessary
        Listing.objects.all().delete()

        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found to assign as hosts. Please create users first.'))
            return

        sample_titles = [
            'Cozy Cottage',
            'Downtown Apartment',
            'Beach House',
            'Mountain Cabin',
            'City Loft'
        ]

        for i in range(10):
            listing = Listing.objects.create(
                title=random.choice(sample_titles),
                description='A lovely place to stay.',
                address=f'{i} Main Street, City',
                price_per_night=random.uniform(50, 300),
                host=random.choice(users)
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
