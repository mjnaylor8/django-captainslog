from django.test import TestCase, LiveServerTestCase, Client
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
            'address',
            'location',
            'email',
            'phone_number',
            'created_at',
        )
       
    name = 'test site name'
    address ='address'
    location = FuzzyPoint()
    email  = 'fred.com'
    address = 'address'
    phone_number = '1274-234'
    created_at = timezone.now()

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
        self.assertEquals(only_site.address, 'address')
        self.assertEquals(only_site.phone_number, '1274-234')
        self.assertEquals(only_site.phone_number, '1274-234')
        self.assertEquals(only_site.created_at.hour, only_site.created_at.hour)
        self.assertEquals(only_site.created_at.minute, only_site.created_at.minute)
        self.assertEquals(only_site.created_at.second, only_site.created_at.second)
        self.assertEquals(only_site.created_at.day, only_site.created_at.day)
        self.assertEquals(only_site.created_at.month, only_site.created_at.month)
        self.assertEquals(only_site.created_at.year, only_site.created_at.year)

class Journey_DetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        # Create Journey Information
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
            'notes',
            'destination',
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
        site = Site_InformationFactory()
        # Create the journey_details
        journey_details = Journey_DetailsFactory(destination = site)

        #In test will have now been added to the database and now need to test we 
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
        self.assertEquals(only_journey.destination, site) 
        self.assertEquals(only_journey.destination.name, 'test site name')




class Site_FacilitiesFactory(factory.django.DjangoModelFactory):
    class Meta:
    # Create Site Facilities
        model = Site_Facilities
        django_get_or_create = (
            'name',
            'greeting',
            'pitch_type',
            'pitch_level',
            'hook_up',
            'waste',
            'toilets',
            'ambience',
            'security',
            'wi_fi',
            'tv_signal',
            'phone_signal_3G_4G',
            'pets',
            'children',
            'laundry',
            'cost_charges',
            'cost_extras',
            'cost_currency',
        )
    greeting = "Good"
    pitch_type = "Grass"
    pitch_level = "Level"
    hook_up = "10A"
    waste = "On Pitch"
    toilets = "Clean"
    ambience = "Peaceful"
    security = "Good"
    wi_fi = "True"
    tv_signal = "Good"
    phone_signal_3G_4G = "Good"
    pets = "True"
    children = "True"
    laundry = "True"
    cost_charges = 10.02
    cost_extras = 0.20
    cost_currency = "£"
    created_date = timezone.now()
    edited_date = timezone.now()


class Site_FacilitiesTest(TestCase):
    
    def test_create_site_facilities(self):
        site = Site_InformationFactory()
        # Create the journey_details
        site_facilities = Site_FacilitiesFactory(name = site)

        #In test will have nnow been added to the database and now need to test we 
        #can save OK and retrieve it

        all_facilities = Site_Facilities.objects.all()
        self.assertEquals(len(all_facilities),1)
        only_facility = all_facilities[0]
        self.assertEquals(only_facility, site_facilities)

        # Check attributes 
        self.assertEquals(only_facility.greeting, 'Good')
        self.assertEquals(only_facility.pitch_type, 'Grass')
        self.assertEquals(only_facility.pitch_level, 'Level')
        self.assertEquals(only_facility.hook_up, '10A')
        self.assertEquals(only_facility.waste, 'On Pitch')
        self.assertEquals(only_facility.toilets, 'Clean')
        self.assertEquals(only_facility.ambience, 'Good')
        self.assertEquals(only_facility.wi_fi, 'True')
        self.assertEquals(only_facility.phone_signal_3G_4G, 'Good')
        self.assertEquals(only_facility.tv_signal, 'Good')
        self.assertEquals(only_facility.pets, 'True')
        self.assertEquals(only_facility.children, 'True')
        self.assertEquals(only_facility.laundry, 'True')
        self.assertEquals(only_facility.cost_charges, 10.02)
        self.assertEquals(only_facility.cost_extras, 0.20)
        self.assertEquals(only_facility.cost_currency,  '£')
        self.assertEquals(only_facility.name, site) 
        self.assertEquals(only_facility.name.name, 'test site name')
        self.assertEquals(only_facility.created_date.day, site_facilities.created_date.day)
        self.assertEquals(only_facility.created_date.month, site_facilities.created_date.month)
        self.assertEquals(only_facility.created_date.year, site_facilities.created_date.year)
        self.assertEquals(only_facility.created_date.hour, site_facilities.created_date.hour)
        self.assertEquals(only_facility.created_date.minute, site_facilities.created_date.minute)
        self.assertEquals(only_facility.created_date.second, site_facilities.created_date.second)       
        self.assertEquals(only_facility.edited_date.day, site_facilities.edited_date.day)
        self.assertEquals(only_facility.edited_date.month, site_facilities.edited_date.month)
        self.assertEquals(only_facility.edited_date.year, site_facilities.edited_date.year)
        self.assertEquals(only_facility.edited_date.hour, site_facilities.edited_date.hour)
        self.assertEquals(only_facility.edited_date.minute, site_facilities.edited_date.minute)
        self.assertEquals(only_facility.edited_date.second, site_facilities.edited_date.second)