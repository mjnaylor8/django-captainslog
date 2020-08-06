from django.test import TestCase
from django.utils import timezone
import datetime
from django.contrib.gis.geos import Point
from factory.fuzzy import BaseFuzzyAttribute
import factory.django
import random
from triplog.models import Journey_Details
from triplog.models import Site_Information
from triplog.models import Site_Facilities
from django.test import RequestFactory
from django.urls import reverse

# Create your tests here.

class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0),
                     random.uniform(-90.0,90.0))

class Site_InformationFactory(factory.django.DjangoModelFactory):
    class Meta:
        # Create Site information
        model = Site_Information
        django_get_or_create = (
            'name',
            'address_line1',
            'address_line2',
            'address_line3',
            'address_code',
            'location',
            'email',
            'phone_number'
        )
       
    name = 'test site name'
    address_line1 ='address line 1'
    address_line2 ='address line 2'
    address_line3 ='address line 3'
    location = FuzzyPoint()
    email  = 'fred.com'
    address_code = 'address code'
    phone_number = '1274-234'

class Site_InformationTest(TestCase):
    def test_create_site_information(self):
        #create the site
        site_information = Site_InformationFactory()

        # checks
        all_sites = Site_Information.objects.all()
        self.assertEquals(len(all_sites),1)
        only_site = all_sites[0]
        self.assertEquals(only_site, site_information)

        # Check attributes
        self.assertEquals(only_site.name, 'test site name')
        self.assertEquals(only_site.address_line1, 'address line 1')
        self.assertEquals(only_site.address_line2, 'address line 2')
        self.assertEquals(only_site.address_line3, 'address line 3')
        self.assertEquals(only_site.address_code, 'address code')
        self.assertEquals(only_site.phone_number, '1274-234')


class Journey_DetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        # Create Site information
        model = Journey_Details
        django_get_or_create = (
            'start_date',
            'end_date',
            'weather',
            'travel_from',
            'travel_to',
            'start_time',
            'end_time',
            'duration',
            'mileage_start',
            'mileage_end',
            'distance',
            'toll_charges',
            'toll_currency',
            'created_date',
            'edited_date',
            'star_rating',
            'would_return',
            'notes'
        )
    start_date = datetime.date(2020, 7, 2)
    end_date = datetime.date(2020, 7, 3)
    weather = 'Sunny'
    travel_from = 'London'
    travel_to = 'Rowledge'
    start_time = datetime.time(9, 2)
    end_time = datetime.time(13, 20)
    duration = datetime.time(4, 14)
    mileage_start = 2312.0
    mileage_end = 2420.0
    distance = 108.0
    toll_charges = 32.12
    toll_currency = '£'
    created_date = timezone.now()
    edited_date = timezone.now()
    star_rating = 'Three'
    would_return = True
    notes = 'Nice Site'

class Journey_DetailsTest(TestCase):
    def test_create_journey_details(self):
        # Create the journey_details
        journey_details = Journey_DetailsFactory()
        #In test will have nnow been added to the database and now need to test we 
        #can save OK and retrieve it

        all_journeys = Journey_Details.objects.all()
        self.assertEquals(len(all_journeys),1)
        only_journey = all_journeys[0]
        self.assertEquals(only_journey, journey_details)

        # Check attributes
        self.assertEquals(only_journey.start_date.day, journey_details.start_date.day)
        self.assertEquals(only_journey.start_date.month, journey_details.start_date.month)
        self.assertEquals(only_journey.start_date.year, journey_details.start_date.year)
        self.assertEquals(only_journey.end_date.day, journey_details.end_date.day)
        self.assertEquals(only_journey.end_date.month, journey_details.end_date.month)
        self.assertEquals(only_journey.end_date.year, journey_details.end_date.year)    
        self.assertEquals(only_journey.weather, 'Sunny')
        self.assertEquals(only_journey.travel_from, 'London')
        self.assertEquals(only_journey.travel_to, 'Rowledge')
        self.assertEquals(only_journey.start_time.hour, journey_details.start_time.hour)
        self.assertEquals(only_journey.start_time.minute, journey_details.start_time.minute)
        self.assertEquals(only_journey.start_time.second, journey_details.start_time.second)
        self.assertEquals(only_journey.end_time.hour, journey_details.end_time.hour)
        self.assertEquals(only_journey.end_time.minute, journey_details.end_time.minute)
        self.assertEquals(only_journey.end_time.second, journey_details.end_time.second)
        self.assertEquals(only_journey.mileage_start,2312.0)
        self.assertEquals(only_journey.mileage_end,2420.0)
        self.assertEquals(only_journey.distance,108.0)
        self.assertEquals(only_journey.toll_charges, 32.12)
        self.assertEquals(only_journey.toll_currency, '£')
        self.assertEquals(only_journey.created_date.day, journey_details.created_date.day)
        self.assertEquals(only_journey.created_date.month, journey_details.created_date.month)
        self.assertEquals(only_journey.created_date.year, journey_details.created_date.year)
        self.assertEquals(only_journey.created_date.hour, journey_details.created_date.hour)
        self.assertEquals(only_journey.created_date.minute, journey_details.created_date.minute)
        self.assertEquals(only_journey.created_date.second, journey_details.created_date.second)       
        self.assertEquals(only_journey.edited_date.day, journey_details.edited_date.day)
        self.assertEquals(only_journey.edited_date.month, journey_details.edited_date.month)
        self.assertEquals(only_journey.edited_date.year, journey_details.edited_date.year)
        self.assertEquals(only_journey.edited_date.hour, journey_details.edited_date.hour)
        self.assertEquals(only_journey.edited_date.minute, journey_details.edited_date.minute)
        self.assertEquals(only_journey.edited_date.second, journey_details.edited_date.second)
        self.assertEquals(only_journey.star_rating, 'Three')
        self.assertEquals(only_journey.would_return, True)
        self.assertEquals(only_journey.notes, 'Nice Site')   