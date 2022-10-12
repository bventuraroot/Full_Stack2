from django.shortcuts import render
import requests


def index(request):
    template_name = "index.html"
    response = requests.get('http://127.0.0.1:8000/back/api/tutoriales')
    todos = response.json()
    print(todos)
    return render(request, template_name, {"todos": todos})
