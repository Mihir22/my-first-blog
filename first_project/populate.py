import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django

django.setup()
import random
from first_app.models import Topic,Webpage,AccessRecord
from faker import Faker

fake = Faker()
topics = ["Search","Social","Marketplace","News","Games"]

def add_topic():
    t  = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):
        t = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpg = Webpage.objects.get_or_create(topic = t,urls = fake_url,name = fake_name)[0]


        acrecords = AccessRecord.objects.get_or_create(t_name = webpg,date = fake_date)[0]


if __name__ == '__main__':
    print("Start Populating")
    populate(20)
    print("Populating completed")
