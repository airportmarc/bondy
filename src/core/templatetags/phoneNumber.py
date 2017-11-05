
from django import template

from django.template.defaultfilters import stringfilter

register = template.Library()




@register.filter
@stringfilter
def CanadaPhone(phone):
    if len(phone) == 10:
        area = phone[:3]
        local = phone[3:6]
        last = phone[6:]

        return "({}) - {} - {}".format(area, local, last)
