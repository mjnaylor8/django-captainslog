""" Views defined """
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView


from triplog.models import SiteInformation, JourneyDetail, TripDetail
from triplog.forms import JourneyDetailForm, SiteInformationForm, \
    TripDetailForm
from triplog.tables import SiteInformationTable, JourneyDetailTable, TripDetailTable

SITE_INFORMATION_FORM = "triplog/site_information_form.html"
JOURNEY_DETAILS_FORM = "triplog/journey_details_form.html"
SUCCESS_SITEINDEX = "/triplog/siteindex/"
SUCCESS_JOURNEYINDEX = "/triplog/journeyindex/"
TRIP_DETAILS_FORM = "triplog/trip_details_form.html"
SUCCESS_TRIPINDEX = "/triplog/trip2index/"

class AddSiteInformationView(LoginRequiredMixin, CreateView):
    """ Add site inforamtion view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = SiteInformation
    template_name = SITE_INFORMATION_FORM
    success_url = SUCCESS_SITEINDEX
    form_class = SiteInformationForm
#    fields = ("name", "location", "address",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'Add Site Details'
        context['site_information_title'] = site_title
        return context

    def get_initial(self, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['star_rating'] = 0
        return initial

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)


class ChangeSiteInformationView(LoginRequiredMixin, UpdateView):
    """ change site information view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = SiteInformation
    template_name = SITE_INFORMATION_FORM
    success_url = SUCCESS_SITEINDEX
    form_class = SiteInformationForm
#    fields = ("name", "location", "address",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'Change Site Details'
        context['site_information_title'] = site_title
        return context

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)


class SiteInformationView(LoginRequiredMixin, ListView):
    """ list site information view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = SiteInformation
    template_name = "triplog/siteindex.html"
    ordering = ["-created_date", ]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'List Sites'
        context['site_information_title'] = site_title
        return context

    #def form_valid(self, form):
    #    if form.instance.created_by is None:
    #    """ if form is valid return users """
    #        form.instance.created_by = self.request.user
    #    form.instance.edited_by = self.request.user
    #    return super().form_valid(form)

class Site2InformationView(LoginRequiredMixin, SingleTableView):
    """ list site information view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = SiteInformation
    table_class = SiteInformationTable
    template_name = "triplog/site2index.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'List Sites'
        context['site_information_title'] = site_title
        return context

class JourneyDetailView(LoginRequiredMixin, ListView):
    """ List journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetail
    template_name = "triplog/journeyindex.html"
    success_url = SUCCESS_JOURNEYINDEX
    ordering = ["-start_date",]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'List Journeys'
        context['journey_details_title'] = journey_title
        return context

class Journey2DetailsView(LoginRequiredMixin, SingleTableView):
    """ List journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetail
    table_class = JourneyDetailTable
    template_name = "triplog/journey2index.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'List Journeys'
        context['journey_details_title'] = journey_title
        return context

class AddJourneyDetailView(LoginRequiredMixin, CreateView):
    """ add journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetail
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Add a new Journey'
        context['journey_details_title'] = journey_title
        return context

    def get_initial(self, **kwargs):
        initial = super().get_initial(**kwargs)
       # initial['weather'] = 'Sunny'
        return initial

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(response)
        return response

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

class ChangeJourneyDetailView(LoginRequiredMixin, UpdateView):
    """ change journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetail
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Change Journey Details'
        context['journey_details_title'] = journey_title
        return context

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

@login_required(login_url='/accounts/login/')
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_sites = SiteInformation.objects.all().count()
    num_journeys = JourneyDetail.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    home_page_title = 'Home'

    context = {
        'num_sites': num_sites,
        'num_journeys': num_journeys,
        'num_visits': num_visits,
        'home_page_title': home_page_title,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'triplog/index.html', context=context)

class Trip2DetailView(LoginRequiredMixin, SingleTableView):
    """ List trip details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TripDetail
    table_class = TripDetailTable
    template_name = "triplog/trip2index.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip_title = 'List Trips'
        context['trip_details_title'] = trip_title
        #context['table'].order_by = 'name'
        return context

class ChangeTripDetailView(LoginRequiredMixin, UpdateView):
    """ change trip details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TripDetail
    template_name = TRIP_DETAILS_FORM
    success_url = SUCCESS_TRIPINDEX
    form_class = TripDetailForm
    currentjourneys = None

    def get_initial(self):
        self.currentjourneys = get_object_or_404(TripDetail, pk=self.kwargs.get('pk'))
        return {'currentjourneys': self.currentjourneys,}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip_title = 'Change Trip Details'
        context['trip_detail_title'] = trip_title
        context['currentjourneys'] = self.currentjourneys
        return context

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        selectedjourneys = form.cleaned_data['journeychoice']
        for journey in selectedjourneys:
            journey = JourneyDetail.objects.get(pk=journey.pk)
            journey.trip = form.instance
            journey.save()
        return super().form_valid(form)

class AddTripDetailView(LoginRequiredMixin, CreateView):
    """ add trip details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TripDetail

    template_name = TRIP_DETAILS_FORM
    success_url = SUCCESS_TRIPINDEX
    form_class = TripDetailForm

    def get_context_data(self, **kwargs):
        context = super(AddTripDetailView, self).get_context_data(**kwargs)
        trip_title = 'Add a new Trip'
        context['trip_detail_title'] = trip_title
        context['currentjourneys'] = ""
        return context

    def get_initial(self, **kwargs):
        initial = super().get_initial(**kwargs)
        return initial

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(response)
        return response

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        selectedjourneys = form.cleaned_data['journeychoice']
        for journey in selectedjourneys:
            journey = JourneyDetail.objects.get(pk=journey.pk)
            journey.trip = form.instance
            journey.save()
        return super().form_valid(form)
