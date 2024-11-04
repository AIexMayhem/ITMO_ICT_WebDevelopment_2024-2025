from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from project_first_app.forms import OwnerForm
from project_first_app.models import Owner, Car

class CarForm(CreateView):

   # specify the model for create view
   model = Car
   template_name = 'car_form.html'

   # specify the fields to be displayed

   fields = ['brand', 'model', 'color', 'number']

class CarList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'car_list.html'


def owner_form(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)


def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': o})


def list_owners(request):
    # dictionary for initial data with
    # field names as keys
    context = {"dataset": Owner.objects.all()}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь

    return render(request, "owner_list.html", context)