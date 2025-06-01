from django import template

register = template.Library()

@register.filter
def bootstrap_alert_class(tag):
    return {
        'error': 'danger',
        'debug': 'secondary',
    }.get(tag, tag)