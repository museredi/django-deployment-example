import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ninthproject.settings')

import django
django.setup()

import random
from ninth_app.models import Usersss
from faker import Faker

fakegen = Faker()
#topic = ['search', 'social', 'market', 'news', 'games']

#def add_topic():
#    t = Topic.objects.get_or_create(top_name = random.choice(topic))[0]
#    t.save()
#    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        #top = add_topic()

        #create the fake data for that entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        #create the new Webpage entry
        usrs = Usersss.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]

        #createa a fake access record
        #acc_rec = Accessrecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print('populating...')
    populate(30)
    print('Done.')
