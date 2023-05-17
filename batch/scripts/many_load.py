import csv  # https://docs.python.org/3/library/csv.html
import os

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

#from many.models import Person, Course, Membership
from unesco.models import Site, Category, State, Iso, Region 

def run():
    fhand = open(os.path.abspath('unesco/whc-sites-2018-clean.csv'))
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    # Person.objects.all().delete()
    # Course.objects.all().delete()
    # Membership.objects.all().delete()

    # Format <In Sample>
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    # Format <In WHC Sites>
    # 0    1           2             3
    # name,description,justification,year,
    #
    # 4         5        6       
    # longitude,latitude,area_hectares,
    #
    # 7        8     9      10
    # category,state,region,iso

    for row in reader:
        #print(row)

        #p, created = Person.objects.get_or_create(email=row[0])
        #c, created = Course.objects.get_or_create(title=row[2])

        _category, created = Category.objects.get_or_create(name=row[7])
        _iso, created = Iso.objects.get_or_create(name=row[10])
        _region, created = Region.objects.get_or_create(name=row[9])
        _state, created = State.objects.get_or_create(name=row[8])

        # r = Membership.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()

        site_name = row[0]
        try:
            site_year = int(row[3])
        except:
            site_year = None
        try:
            site_latitude = float(row[5])
        except:
            site_latitude = None
        try:
            site_longitude = float(row[4])
        except:
            site_longitude = None

        site_description = row[1]
        site_justification = row[2]

        try:
            site_area_hectares = float(row[6])
        except:
            site_area_hectares = None

        site = Site(name=site_name,year=site_year,latitude=site_latitude,longitude=site_longitude,description=site_description,justification=site_justification,area_hectares=site_area_hectares,category=_category,region=_region,iso=_iso,state=_state)

        site.save()
