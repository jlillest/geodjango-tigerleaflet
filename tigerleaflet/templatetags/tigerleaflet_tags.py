from django import template

register = template.Library()


@register.inclusion_tag('tigerleaflet_init.html')
def init_tigerleaflet_map():
    return


@register.inclusion_tag('tigerleaflet_country.html')
def show_tigerleaflet_country(map_name, prefix, y, x, zoom_level):
    context = {'map_name': map_name,
               'prefix': prefix,
               'latitude': y,
               'longitude': x,
               'zoom_level': zoom_level,
               }
    return context


@register.inclusion_tag('tigerleaflet_state.html')
def show_tigerleaflet_state(map_name, prefix, state):
    context = {'map_name': map_name,
               'prefix': prefix,
               'state': state,
               }
    return context


@register.inclusion_tag('tigerleaflet_county.html')
def show_tigerleaflet_county(map_name, prefix, state, county):
    context = {'map_name': map_name,
               'prefix': prefix,
               'state': state,
               'county': county,
               }
    return context
