from django import template

register = template.Library()

@register.filter(name='message_class')
def message_class(message):
    """
    Returns a CSS class based on the Django message level.
    """
    return {
        'debug': 'alert-debug',
        'info': 'alert-info',
        'success': 'alert-success',
        'warning': 'alert-warning',
        'error': 'alert-error'
    }.get(message.tags, 'alert-info')
