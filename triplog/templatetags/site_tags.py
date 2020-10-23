from django import template

register = template.Library()


@register.inclusion_tag('triplog/_stars.html')
def show_stars(count):
    if count == '':
        count = 0
    return {
        'star_count': range(count),
        'leftover_count': range(count, 5)
    }
