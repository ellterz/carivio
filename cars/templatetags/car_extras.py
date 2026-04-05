from django import template

register = template.Library()


@register.filter(name='car_age')
def car_age(year):
    from datetime import date
    age = date.today().year - year
    if age == 0:
        return "Brand new"
    elif age == 1:
        return "1 year old"
    else:
        return f"{age} years old"


@register.filter(name='cost_format')
def cost_format(value):
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return value