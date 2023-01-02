from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import *
import json

# Create your views here.


def index(request):

    with open('./tabl.json', encoding="utf-8") as t:
        templates = json.load(t)

    if len(templates) != Worker.objects.all().count():
        Worker.objects.all().delete()
        for i in range(len(templates)):
            print(templates[i]['data']['general']['fullName'])
            current_person = templates[i]
            Worker.objects.create(
                id_code=current_person['_id'],
                created_at=current_person['created'],
                person_id=current_person['data']['general']['id'],
                name=current_person['data']['general']['name'],
                secondName=current_person['data']['general']['secondName'],
                lastName=current_person['data']['general']['lastName'],
                fullName=current_person['data']['general']['fullName'],
                email=current_person['data']['general']['email'],
                phone=current_person['data']['general']['phone'],
                position=current_person['data']['general']['position'],
                address=current_person['data']['general']['address'],
            )

    # for section, commands in templates.items():
    #     print(section)
    #     print('\n'.join(commands))

    return render(request, 'testparser/index.html')


def search(request):
    context = {}
    if request.method == 'POST':
        try:
            input_value = request.POST.get('input_value')
            person_dict = Worker.objects.get(fullName=input_value)
            context = {
                "p_fullname": person_dict.fullName,
                "p_email": person_dict.email,
                "p_phone": person_dict.phone,
                "p_position": person_dict.position,
                "p_address": person_dict.address,
            }
        except:
            context={
                'p_answer': "Сотрудник не найден, пожалуйста введите фио в порядке ФАМИЛИЯ ИМЯ ОТЧЕСТВО"
            }



    return render(request, 'testparser/search.html', context=context)