""" Tests """
import random
import datetime
from django.test import TestCase
from django.utils import timezone
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.gis.geos import Point

from factory.fuzzy import BaseFuzzyAttribute
import factory.django


from triplog.models import JourneyDetails
from triplog.models import SiteInformation
from triplog.views import JourneyDetailsView

# Create your tests here.

class FuzzyPoint(BaseFuzzyAttribute):
    """ Fuzzy Point for testing maps """
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0),
                     random.uniform(-90.0, 90.0))

class SiteInformationFactory(factory.django.DjangoModelFactory):
    """ Create SiteInformation """
    class Meta:
        # Create Site information
        model = SiteInformation
        django_get_or_create = (
            'name',
            'address',
            'location',
            'star_rating',
            'would_return',
            'email',
            'phone_number',
            'greeting',
            'pitch_type',
            'pitch_level',
            'hook_up',
            'waste',
            'toilets',
            'ambience',
            'security',
            'wifi',
            'tv_signal',
            'phone_signal_3G_4G',
            'pets',
            'children',
            'laundry',
            'cost_charges',
            'cost_extras',
            'cost_currency',
            'created_date',
        )

    name = 'test site name'
    address = 'address'
    location = FuzzyPoint()
    star_rating = 'Three'
    would_return = True
    email = 'fred.com'
    address = 'address'
    phone_number = '1274-234'
    greeting = "Good"
    pitch_type = "Grass"
    pitch_level = "Level"
    hook_up = "10A"
    waste = "On Pitch"
    toilets = "Clean"
    ambience = "Peaceful"
    security = "Good"
    wifi = True
    tv_signal = "Good"
    phone_signal_3G_4G = "Good"
    pets = True
    children = True
    laundry = True
    cost_charges = 10.02
    cost_extras = 0.20
    cost_currency = "£"
    created_date = timezone.now()

class SiteInformationTest(TestCase):
    """ Test SiteInformation """
    def test_create_site_information(self):
        """ Test SiteInformation """
        #create the site
        site_information = SiteInformationFactory()

        # checks
        all_sites = SiteInformation.objects.all()
        self.assertEqual(len(all_sites), 1)
        only_site = all_sites[0]
        self.assertEqual(only_site, site_information)

        # Check attributes
        self.assertEqual(only_site.name, 'test site name')
        self.assertEqual(only_site.address, 'address')
        self.assertEqual(only_site.phone_number, '1274-234')
        self.assertEqual(only_site.star_rating, 'Three')
        self.assertEqual(only_site.would_return, True)
        self.assertEqual(only_site.greeting, 'Good')
        self.assertEqual(only_site.pitch_type, 'Grass')
        self.assertEqual(only_site.pitch_level, 'Level')
        self.assertEqual(only_site.hook_up, '10A')
        self.assertEqual(only_site.waste, 'On Pitch')
        self.assertEqual(only_site.toilets, 'Clean')
        self.assertEqual(only_site.ambience, 'Peaceful')
        self.assertEqual(only_site.wifi, True)
        self.assertEqual(only_site.phone_signal_3G_4G, 'Good')
        self.assertEqual(only_site.tv_signal, 'Good')
        self.assertEqual(only_site.pets, True)
        self.assertEqual(only_site.children, True)
        self.assertEqual(only_site.laundry, True)
        self.assertEqual(only_site.cost_charges, 10.02)
        self.assertEqual(only_site.cost_extras, 0.20)
        self.assertEqual(only_site.cost_currency, '£')
        self.assertEqual(only_site.created_date.hour, only_site.created_date.hour)
        self.assertEqual(only_site.created_date.minute, only_site.created_date.minute)
        self.assertEqual(only_site.created_date.second, only_site.created_date.second)
        self.assertEqual(only_site.created_date.day, only_site.created_date.day)
        self.assertEqual(only_site.created_date.month, only_site.created_date.month)
        self.assertEqual(only_site.created_date.year, only_site.created_date.year)

class JourneyDetailsFactory(factory.django.DjangoModelFactory):
    """ Create JourneyDetails """
    class Meta:
        # Create Journey Information
        model = JourneyDetails
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
    notes = 'Nice Site'


class JourneyDetailsTest(TestCase):
    """ Test JourneyDetails """
    def test_create_journey_details(self):
        """ Test JourneyDetails """
        site = SiteInformationFactory()
        # Create the journey_details
        journey_details = JourneyDetailsFactory(destination=site)

        #In test will have now been added to the database and now need to test we
        #can save OK and retrieve it

        all_journeys = JourneyDetails.objects.all()
        self.assertEqual(len(all_journeys), 1)
        only_journey = all_journeys[0]
        self.assertEqual(only_journey, journey_details)

        # Check attributes
        self.assertEqual(only_journey.start_date.day, journey_details.start_date.day)
        self.assertEqual(only_journey.start_date.month, journey_details.start_date.month)
        self.assertEqual(only_journey.start_date.year, journey_details.start_date.year)
        self.assertEqual(only_journey.end_date.day, journey_details.end_date.day)
        self.assertEqual(only_journey.end_date.month, journey_details.end_date.month)
        self.assertEqual(only_journey.end_date.year, journey_details.end_date.year)
        self.assertEqual(only_journey.weather, 'Sunny')
        self.assertEqual(only_journey.travel_from, 'London')
        self.assertEqual(only_journey.travel_to, 'Rowledge')
        self.assertEqual(only_journey.start_time.hour, journey_details.start_time.hour)
        self.assertEqual(only_journey.start_time.minute, journey_details.start_time.minute)
        self.assertEqual(only_journey.start_time.second, journey_details.start_time.second)
        self.assertEqual(only_journey.end_time.hour, journey_details.end_time.hour)
        self.assertEqual(only_journey.end_time.minute, journey_details.end_time.minute)
        self.assertEqual(only_journey.end_time.second, journey_details.end_time.second)
        self.assertEqual(only_journey.mileage_start, 2312.0)
        self.assertEqual(only_journey.mileage_end, 2420.0)
        self.assertEqual(only_journey.distance, 108.0)
        self.assertEqual(only_journey.toll_charges, 32.12)
        self.assertEqual(only_journey.toll_currency, '£')
        self.assertEqual(only_journey.created_date.day, journey_details.created_date.day)
        self.assertEqual(only_journey.created_date.month, journey_details.created_date.month)
        self.assertEqual(only_journey.created_date.year, journey_details.created_date.year)
        self.assertEqual(only_journey.created_date.hour, journey_details.created_date.hour)
        self.assertEqual(only_journey.created_date.minute, journey_details.created_date.minute)
        self.assertEqual(only_journey.created_date.second, journey_details.created_date.second)
        self.assertEqual(only_journey.edited_date.day, journey_details.edited_date.day)
        self.assertEqual(only_journey.edited_date.month, journey_details.edited_date.month)
        self.assertEqual(only_journey.edited_date.year, journey_details.edited_date.year)
        self.assertEqual(only_journey.edited_date.hour, journey_details.edited_date.hour)
        self.assertEqual(only_journey.edited_date.minute, journey_details.edited_date.minute)
        self.assertEqual(only_journey.edited_date.second, journey_details.edited_date.second)
        self.assertEqual(only_journey.notes, 'Nice Site')
        self.assertEqual(only_journey.destination, site)
        self.assertEqual(only_journey.destination.name, 'test site name')

class JourneyDetailsViewTest(TestCase):
    """ Test Journey_DetailView """
    def setUp(self):
        """ Test Journey_DetailView """
        self.factory = RequestFactory()

    def test_get(self):
        """ Test Journey_DetailView """
        request = self.factory.get(reverse('journeyindex'))
        response = JourneyDetailsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('triplog/journey_index.html')
