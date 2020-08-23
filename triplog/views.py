""" Views defined """
# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView
from .models import SiteInformation, JourneyDetails
from .forms import JourneyDetailsForm, JourneyDetails2Form


SITE_INFORMATION_FORM = "triplog/site_information_form.html"
JOURNEY_DETAILS_FORM = "triplog/journey_details_form.html"
SUCCESS_SITEINDEX = "/siteindex/"
SUCCESS_JOURNEYINDEX = "/journeyindex/"

class AddSiteInformationView(CreateView):
    """ Add site inforamtion view """
    model = SiteInformation
    template_name = SITE_INFORMATION_FORM
    success_url = SUCCESS_SITEINDEX
    fields = ("name", "location", "address",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'Add Site Details'
        context['site_infomation_title'] = site_title
        return context

class ChangeSiteInformationView(UpdateView):
    """ change site information view """
    model = SiteInformation
    template_name = SITE_INFORMATION_FORM
    success_url = SUCCESS_SITEINDEX
    fields = ("name", "location", "address",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'Change Site Details'
        context['site_information_title'] = site_title
        return context

class SiteInformationView(ListView):
    """ list site inforamtion view """
    model = SiteInformation
    template_name = "triplog/siteindex.html"
    ordering = ["-created_at", ]
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = 'List Sites'
        context['site_information_title'] = site_title
        return context

class JourneyDetailsView(ListView):
    """ List journey details view """
    model = JourneyDetails
    template_name = "triplog/journeyindex.html"
    success_url = SUCCESS_JOURNEYINDEX
    ordering = ["-start_date",]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'List Journeys'
        context['journey_details_title'] = journey_title
        return context

class AddJourneyDetailsView(CreateView):
    """ add journey details view """
    model = JourneyDetails
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetailsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Add new Journey Details'
        context['journey_details_title'] = journey_title
        return context

class AddJourneyDetails2View(CreateView):
    """ add journey details view """
    model = JourneyDetails
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetails2Form
    template_name = "triplog/journey_details2_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Add new Journey Details'
        context['journey_details_title'] = journey_title
        return context

    def get_initial(self, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['weather'] = 'Sunny'
        return initial

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(response)
        return response

class ChangeJourneyDetailsView(UpdateView):
    """ change journey details view """
    model = JourneyDetails
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JourneyDetailsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Change Journey Details'
        context['journey_details_title'] = journey_title
        return context
