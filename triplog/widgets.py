import datetime
from django.forms import DateTimeInput, CheckboxInput, DurationField
from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration
from django.utils.duration import _get_duration_components

class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context

class CheckBoxBootstrapSwitch(CheckboxInput):
    """Django widget for bootstrap switch HTML widget: http://www.bootstrap-switch.org/
    Options can be provided through 'switch' argument:
        switch = forms.BooleanField(required=False, label=_(u"bootstrap switch"),
                widget=CheckBoxBootstrapSwitch(switch={'size': 'small', 'on': 'warning', 'text-label': 'Switch Me'}))
    """
    def __init__(self, switch=None, *args, **kwargs):
        self.switch = switch or {}
        super(CheckBoxBootstrapSwitch, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        checkbox = super(CheckBoxBootstrapSwitch, self).render(name=name, value=value, attrs=attrs)
        data = ''
        size = self.switch.get('size', '')  # 'mini', 'small', 'large' or '' for normal
        # handling of data-properties
        for key in ['on', 'off', 'on-label', 'off-label', 'text-label']:
            data += ' data-%s="%s"' % (key, self.switch[key]) if key in self.switch else ''

        widget = '<div id="switch-%s" class="make-switch' % name
        widget += ' switch-' + size if size else ''
        widget += '"' + data +'>' + checkbox
        widget += '</div>'
        return mark_safe(widget)

class DurationInput(TextInput):

    def _format_value(self, value):
        duration = parse_duration(value)

        days = duration.days
        seconds = duration.seconds
        microseconds = duration.microseconds

        minutes = seconds // 60
        seconds = seconds % 60

        hours = minutes // 60
        minutes = minutes % 60
        print(hours, minutes)

        return '{:02d}:{:02d}'.format(hours, minutes)