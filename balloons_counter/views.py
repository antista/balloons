from django.shortcuts import render, redirect

from balloons_counter import counter
from balloons_counter.forms import ExampleForm
from balloons_counter.models import Entity


def main_page(request, entity_name=None):
    measure = 'gram'
    if request.method == 'POST':
        weight = int(request.POST['weight'])
        measure = request.POST['measure']
    elif entity_name:
        weight = Entity.get_entity(entity_name).weight
    else:
        return render(request, 'counter/main_page.html',
                      {'examples': Entity.get_entities()})

    weight, measure = counter.convert(weight, measure)
    return render(request, 'counter/main_page.html',
                  {'balloons_count': counter.count(weight, measure),
                   'current_value': {'weight': weight, 'measure': measure},
                   'examples': Entity.get_entities()})


# if request.method == 'GET':
#     if not entity_name:
#         return render(request, 'counter/main_page.html', {'balloons_count': 1, 'examples': Entity.get_entities()})
#     return render(request, 'counter/main_page.html',
#                   {'balloons_count': counter.count(Entity.get_entity(entity_name).weight),
#                    'examples': Entity.get_entities()})
#
# if request.method == 'POST':
#     weight = int(request.POST['weight'])
#     measure = request.POST['measure']
#     return render(request, 'counter/main_page.html',
#                   {'balloons_count': counter.count(weight, measure), 'examples': Entity.get_entities()})

def redirect_pictures(request, image_name):
    print('==============================================')
    return redirect('/static/styles/images/entities/{}'.format(image_name))
