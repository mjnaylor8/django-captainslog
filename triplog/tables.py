# triplog/tables.py
import django_tables2 as tables
from django_tables2 import TemplateColumn
from django.utils.html import format_html
from triplog.models import SiteInformation, JourneyDetail, TripDetail
from django.db.models.functions import Length

class JourneyDetailTable(tables.Table):
    update = TemplateColumn(template_name='changejourneycolumn.html', orderable=False)
    #travel_from = tables.Column(order_by=("travel_from", "start_date"))
    class Meta:
        attrs = {
            "id": "journey_details",
            "class": "table table-striped",
            'thead' : {
                'class': 'thead-dark'
            }}
        model = JourneyDetail
        template_name = "django_tables2/bootstrap4.html"
        fields = ("start_date", "end_date", "travel_from", "travel_to", "update")
        order_by = ("start_date")

class SiteInformationTable(tables.Table):
    stars = tables.Column(
        empty_values=(),
        attrs={
            "th": {"style": "display:none;",},
            "td": {
                "class": "col-2 stars",
                "scope": "col",
            }
        })
    def render_stars (self, value):
        return format_html('<div style="display:inline" class="score-star-success" id="star-rating"> </div>', value)

    update = TemplateColumn(template_name='changesitecolumn.html', orderable=False)

    star_rating = tables.Column(
        attrs={
            "td": {
                "style": "display:none;",
                "scope": "col",
            }
        })

    class Meta:
        attrs = {
            "id": "site_information",
            "class": "table table-striped",
            "thead" : {
                "class": "thead-dark"
                }
        }
        model = SiteInformation
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "address", "star_rating", "stars", "update")
        exclude = ("change",)

class TripDetailsTable(tables.Table):
    name = tables.Column(
        attrs={
            "td": {
                "class": "col-3",
            }
        }
    )

    #journey_trip = tables.ManyToManyColumn(
    #    verbose_name="Journeys (Date, From, To)",
    #    linkify_item=True, 
    #    accessor=('journey_trip'), 
    #    separator=format_html("<br/> ")
    #)

    date = tables.ManyToManyColumn(
        filter=lambda qs: qs.filter().order_by('start_date'),
        verbose_name="Date",
        linkify_item=True,
        separator=format_html("<br/> "),
        accessor=('journey_trip'),
        order_by=("date",),
        transform=lambda obj: obj.start_date
    )

    start = tables.ManyToManyColumn(
        filter=lambda qs: qs.filter().order_by('start_date'),
        verbose_name="Start",
        separator=format_html("<br/> "),
        accessor=('journey_trip'),
        transform=lambda obj: format_html('<a href="{}">{}</a>'.\
            format(obj.travel_from.get_absolute_url(), str(obj.travel_from)))
    )

    destination = tables.ManyToManyColumn(
        filter=lambda qs: qs.filter().order_by('start_date'),
        verbose_name="Destination",
        separator=format_html("<br/> "),
        accessor=('journey_trip'), 
        transform=lambda obj: format_html('<a href="{}">{}</a>'.\
            format(obj.travel_to.get_absolute_url(), str(obj.travel_to)))
    )


    class Meta:
        attrs = {
            "id": "trip_details",
            "class": "table table-striped",
            "thead": {
                "class": "thead-dark"
            }
        }
        model = TripDetail
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "date", "start", "destination")
        order_by = ("name", "date")
        