from django.urls import path

from measurement.views import demo

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('demo/',demo)
]
