# triplog/tables.py
import django_tables2 as tables
from django_tables2 import TemplateColumn
from django.utils.html import format_html
from triplog.models import SiteInformation, JourneyDetails

class JourneyDetailsTable(tables.Table):
        update = TemplateColumn(template_name='changejourneycolumn.html', orderable=False)
        travel_from = tables.Column(order_by=("travel_from", "start_date"))
        class Meta:
            attrs = {"id": "journey_details", "class": "table table-striped",         
                'thead' : {
                    'class': 'thead-dark'
                }}
            model = JourneyDetails
            template_name = "django_tables2/bootstrap4.html"
            fields = ("start_date", "end_date", "travel_from", "travel_to", "update")

class SiteInformationTable(tables.Table):
    stars = tables.Column(empty_values=(),
                           attrs = {
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
                           attrs = {
                               "td": {
                                   "style": "display:none;",
                                   "scope": "col",
                           }
                           })                 

    class Meta:
        attrs = {"id": "site_information", "class": "table table-striped",         
            'thead' : {
                'class': 'thead-dark'
            }}
        model = SiteInformation
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "address", "star_rating", "stars", "update")
        exclude = ("change",)


