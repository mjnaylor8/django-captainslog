""" Views defined """
# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from braces import views
from triplog.models import SiteInformation, JourneyDetails
from triplog.forms import JourneyDetailsForm, SiteInformationForm
from triplog.tables import SiteInformationTable, JourneyDetailsTable

SITE_INFORMATION_FORM = "triplog/site_information_form.html"
JOURNEY_DETAILS_FORM = "triplog/journey_details_form.html"
SUCCESS_SITEINDEX = "/triplog/siteindex/"
SUCCESS_JOURNEYINDEX = "/triplog/journeyindex/"

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
    
    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

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
    
    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)


class JourneyDetailsView(LoginRequiredMixin, ListView):
    """ List journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetails
    template_name = "triplog/journeyindex.html"
    success_url = SUCCESS_JOURNEYINDEX
    ordering = ["-start_date",]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'List Journeys'
        context['journey_details_title'] = journey_title
        return context

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

class Journey2DetailsView(LoginRequiredMixin, SingleTableView):
    """ List journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetails
    table_class = JourneyDetailsTable
    template_name = "triplog/journey2index.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'List Journeys'
        context['journey_details_title'] = journey_title
        return context

    def form_valid(self, form):
        if form.instance.created_by is None:
            form.instance.created_by = self.request.user
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

class AddJourneyDetailsView(LoginRequiredMixin, CreateView):
    """ add journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetails
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetailsForm

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

class ChangeJourneyDetailsView(LoginRequiredMixin, UpdateView):
    """ change journey details view """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = JourneyDetails
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetailsForm

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
    num_journeys = JourneyDetails.objects.all().count()

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
    
