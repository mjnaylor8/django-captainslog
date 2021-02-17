import django_tables2 as tables
from django_tables2 import TemplateColumn, FileColumn
from sitemaps.models import GeoJSONRoute

class GeoJSONRouteTable(tables.Table):
    """ Table listing Routes """
    options = TemplateColumn(template_name='optionsroutecolumn.html', orderable=False, attrs={
        "th": {},
        "tr": {},
        "td": {}})
    route_file = FileColumn()
    class Meta:
        """ update meta for formatting """
        attrs = {
            "id": "route-details",
            "class": "table table-striped",
            'thead' : {
                'id': 'route-details-header',
                'class': 'thead-dark'
            },
            'tbody' : {
                'id' : 'route-details-body'
            }
        }
        model = GeoJSONRoute
        template_name = "django_tables2/bootstrap4.html"
        fields = ("route_name", "route_description", "user", "route_file", "options")
        order_by = ("route_name")
        row_attrs = {
            'data-pk': lambda record: record.pk, 'data-url': " 'updateroute' "
        }