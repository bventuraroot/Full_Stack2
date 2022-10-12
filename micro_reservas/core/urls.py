from django.urls import path
from .views import registerusers, loginView, courtsfull, courtsfull_detail

urlpatterns = [
    #todo enpoints para darse de alta y el Login
    path('api/register_user', registerusers.as_view()),
    path('api/login_user', loginView.as_view()),

    #todo enpoints para crud de courts
    path('api/courtsfull', courtsfull),
    path('api/courtsfull/<pk>', courtsfull_detail)

     #todo http://127.0.0.1:8000/api/courtsfull
     #todo http://127.0.0.1:8000/api/courtsfull/<pk>

    # {
    #
    #     "courts_name": "Cancha 4",
    #     "courts_descripcion": "Cancha 4",
    #     "courts_location": "CANCHA SUR",
    #     "courts_picture": "https://www.miraflores.gob.pe/wp-content/uploads/2021/04/canchas-foto4.jpg",
    #     "courts_state": true
    # }
]
