""" Views defined """
# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView
from django.shortcuts import HttpResponse, render, redirect
from .models import SITEINFORMATION, JOURNEYDETAILS
from .forms import JOURNEYDETAILSForm, JOURNEYDETAILS2Form


SITE_INFORMATION_FORM = "triplog/site_information_form.html"
JOURNEY_DETAILS_FORM = "triplog/journey_details_form.html"
SUCCESS_SITEINDEX = "/siteindex/"
SUCCESS_JOURNEYINDEX = "/journeyindex/"

class AddSITEINFORMATIONView(CreateView):
    """ Add site inforamtion view """
    model = SITEINFORMATION
    template_name = SITE_INFORMATION_FORM
    success_url = SUCCESS_SITEINDEX
    fields = ("name", "location", "address",)

class ChangeSITEINFORMATIONView(UpdateView):
    """ change site information view """
    model = SITEINFORMATION
    template_name = SITE_INFORMATION_FORM
    success_url = SUCCESS_SITEINDEX
    fields = ("name", "location", "address",)

class SITEINFORMATIONView(ListView):
    """ list site inforamtion view """
    model = SITEINFORMATION
    template_name = "triplog/siteindex.html"
    ordering = ["-created_at", ]

class JOURNEYDETAILSView(ListView):
    """ List journey details view """
    model = JOURNEYDETAILS
    template_name = "triplog/journeyindex.html"
    success_url = SUCCESS_JOURNEYINDEX
    ordering = ["-start_date",]

class AddJOURNEYDETAILSView(CreateView):
    """ add journey details view """
    model = JOURNEYDETAILS
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JOURNEYDETAILSForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Add new Journey Details'
        context['journey_details_title'] = journey_title
        return context

class AddJOURNEYDETAILS2View(CreateView):
    """ add journey details view """
    model = JOURNEYDETAILS
    template_name = "triplog/journey_details2_form.html"
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JOURNEYDETAILS2Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Add new Journey Details'
        context['journey_details_title'] = journey_title
        return context

def home(request):

    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = JOURNEYDETAILS2Form(request.POST)

        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if details.is_valid():

            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database
            post = details.save(commit=False)

            # Finally write the changes into database
            post.save()

            # redirect it to some another page indicating data
            # was inserted successfully
            return HttpResponseRedirect(SUCCESS_JOURNEYINDEX)

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "triplog/journey_details2_form.html", {'form':details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = JOURNEYDETAILS2Form(None)
        return render(request, 'triplog/journey_details2_form.html', {'form':form})


class ChangeJOURNEYDETAILSView(UpdateView):
    """ change journey details view """
    model = JOURNEYDETAILS
    template_name = JOURNEY_DETAILS_FORM
    success_url = SUCCESS_JOURNEYINDEX
    form_class = JOURNEYDETAILSForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        journey_title = 'Change Journey Details'
        context['journey_details_title'] = journey_title
        return context
        