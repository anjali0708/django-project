import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro_two.settings')

import django
django.setup()

from app_two.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for i in range(N):
        fake_fname= fake.first_name()
        fake_lname= fake.last_name()
        fake_email= fake.email()

        f = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]
        f.save()

if __name__ == '__main__':
    populate(20)
    print("done!")
