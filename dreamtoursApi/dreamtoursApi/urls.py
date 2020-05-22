from django.urls import path, include

urlpatterns = [
    path('dreamtoursApi/', include('dreamtours_app.urls'))
]