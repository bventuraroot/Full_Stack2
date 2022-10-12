# TODO DIA 1
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from .serializers import courts_serializer, TutorialSerializer
from .models import Bookings, Courts, Frecuency, States, Partners, Tutorial
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny

# TODO DIA 2
from django.contrib.auth.models import User  # TODO Tabla user
from rest_framework.authtoken.models import Token  # TODO Tabla Token
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser


# class courtsAllViewSet(generics.ListAPIView):
#     queryset = Courts.objects.all()
#     serializer_class = courts_serializer
#     permission_classes = (IsAuthenticated,)

# class courtsfull(APIView):
#     permission_classes = (AllowAny,)
#
#     # todo metodo me permitira listar las canchas y detalle de cancha
#     def get(self, request):
#         # todo select * from courts
#         canchas = Courts.objects.all()
#         # todo select * from courts where courts_name="cancha1"
#         cancha = request.GET.get('courts_id', None)
#         if cancha is not None:
#             # todo select * from canchas where court_id like '%%'
#             canchas = canchas.filter(courts_id__icontains=cancha)
#         canchas_serializer = courts_serializer(canchas, many=True)
#         return JsonResponse(canchas_serializer.data, safe=False)
#
#     def post(self, request):
#         # todo recibir la informacion en JSON
#         canchas_data = JSONParser().parse(request)
#         # todo enviando informacion a mi archivo serializer
#         canchas_serializer = courts_serializer(data=canchas_data)
#         if canchas_serializer.is_valid():
#             # todo almacena en la BD
#             canchas_serializer.save()
#             return JsonResponse(canchas_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(canchas_serializer.data, status=status.HTTP_400_BAD_REQUEST)


# todo Vistas basadas en funciones

# @api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([AllowAny])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()
#
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
#
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
#         return JsonResponse({'message': '{} Tutoriales delete all'.format(count[0])},
#                             status=status.HTTP_204_NO_CONTENT)
#
#     tutorials_serializer = TutorialSerializer(tutorials, many=True)
#     return JsonResponse(tutorials_serializer.data, safe=False)
#
#
# @api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([AllowAny])
# def tutorial_detail(request, pk):
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#         if request.method == 'GET':
#             tutorial_serializer = TutorialSerializer(tutorial)
#             return JsonResponse(tutorial_serializer.data)
#
#         elif request.method == 'DELETE':
#             tutorial.delete()
#             return JsonResponse({'Message': 'Tutorial eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
#
#         elif request.method == 'PUT':
#             tutorial_data = JSONParser().parse(request)
#             tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
#             if tutorial_serializer.is_valid():
#                 tutorial_serializer.save()
#                 return JsonResponse(tutorial_serializer.data)
#             return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     except Tutorial.DoesNotExist:
#         return JsonResponse({'message': 'El Tutorial dot Not existe'}, status=status.HTTP_404_NOT_FOUND)
#
# # todo esta api me permite registrar nuevos usuarios
class registerusers(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario = request.data['username']
        correo = request.data['email']
        contraseña = request.data['password']
        nombre = request.data['firstname']
        apellidos = request.data['lastname']
        es_staff = request.data['staff']
        nuevo_usuario = User.objects.create_user(usuario, correo, contraseña)
        nuevo_usuario.fist_name = nombre
        nuevo_usuario.last_name = apellidos
        nuevo_usuario.is_staff = es_staff
        nuevo_usuario.save()
        key_usuario = Token.objects.create(user=nuevo_usuario)
        data = {'detail': 'User successfully created ok token ' + key_usuario.key}
        rpta = json.dumps(data)
        return HttpResponse(rpta, content_type='application/json')

#     # todo esta el la clase mas basica para poder construir APIS en DJANGO
#     # todo esta clase APIView me permite definir toda la logica en la funcion
#     # todo y podemos utilizar los metodos GET,POST,PUT,PATCH,DELETE
#     # todo utlizar cuando desea hacer el control total de mi logica

# todo esta api me permite ingresar al sistema
class loginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario = request.data['username']
        clave = request.data["password"]
        usuario = authenticate(username=usuario, password=clave)
        if usuario:
            # todo select key from token where user_id=usuario_id
            key_usuario = Token.objects.get(user_id=usuario.id)
            data = {
                "nombre": usuario.first_name,
                "apellido": usuario.last_name,
                "correo": usuario.email,
                "key": key_usuario.key}
        else:
            data = {"error": "Not the credentiales"}
        rpta = json.dumps(data)
        return HttpResponse(rpta, content_type='application/json')


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def courtsfull(request):
    if request.method == 'GET':
        curts = Courts.objects.all()

        curt = request.GET.get('courts_name', None)
        if curt is not None:
            curts = curts.filter(courts_name__icontains=curt)

    elif request.method == 'POST':
        curts_data = JSONParser().parse(request)
        courtsserializer = courts_serializer(data=curts_data)
        if courtsserializer.is_valid():
            courtsserializer.save()
            return JsonResponse(courtsserializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(courtsserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Courts.objects.all().delete()
        return JsonResponse({'message': '{} Curts delete all'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

    curts_serializer = courts_serializer(curts, many=True)
    return JsonResponse(curts_serializer.data, safe=False)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def courtsfull_detail(request, pk):
    try:
        curt = Courts.objects.get(pk=pk)
        if request.method == 'GET':
            courtsserializer = courts_serializer(curt)
            return JsonResponse(courtsserializer.data)

        elif request.method == 'DELETE':
            curt.delete()
            return JsonResponse({'Message': 'curt eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            curt_data = JSONParser().parse(request)
            courtsserializer = courts_serializer(curt, data=curt_data)
            if courtsserializer.is_valid():
                courtsserializer.save()
                return JsonResponse(courtsserializer.data)
            return JsonResponse(courtsserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Courts.DoesNotExist:
        return JsonResponse({'message': 'El Curts dot Not existe'}, status=status.HTTP_404_NOT_FOUND)
