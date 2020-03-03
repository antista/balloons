from django.shortcuts import render, redirect

from balloons_counter import counter


def main_page(request):
    if request.method == 'GET':
        return render(request, 'counter/main_page.html', {'balloons_count': 1})
    if request.method == 'POST':
        weight = int(request.POST['weight'])
        measure = request.POST['measure']
        return render(request, 'counter/main_page.html', {'balloons_count': counter.count(weight, measure)})
