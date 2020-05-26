from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from dreamtours_app import bbdd_manager
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from . import map_manager
from .models import *
from .serializer import *

class MyPagiantion(PageNumberPagination):
    page_size_query_param = 'page_size'

"""
User View
"""

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPagiantion

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None

"""
City View
"""

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = MyPagiantion

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = None

"""
Particular View
"""

class ParticularList(generics.ListCreateAPIView):
    queryset = Particular.objects.all()
    serializer_class = ParticularSerializer
    pagination_class = MyPagiantion

class ParticularDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Particular.objects.all()
    serializer_class = ParticularSerializer
    pagination_class = None

class ParticularByCity(generics.ListAPIView):
    def get_queryset(self):
        queryset = Particular.objects.filter(city_id=self.kwargs['pk'])
        return queryset
    serializer_class = ParticularSerializer
    pagination_class = None

"""
Company View
"""

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = MyPagiantion

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = None

"""
LocalType View
"""

class LocalTypeList(generics.ListCreateAPIView):
    queryset = LocalType.objects.all()
    serializer_class = LocalTypeSerializer
    pagination_class = MyPagiantion

class LocalTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocalType.objects.all()
    serializer_class = LocalTypeSerializer
    pagination_class = None

"""
Local View
"""

class LocalList(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    pagination_class = MyPagiantion

class LocalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    pagination_class = None

class LocalByType(generics.ListAPIView):
    def get_queryset(self):
        queryset = Local.objects.filter(type_id=self.kwargs['pk'])
        return queryset
    serializer_class = LocalSerializer
    pagination_class = None

class LocalByCompany(generics.ListAPIView):
    def get_queryset(self):
        queryset = Local.objects.filter(company_id=self.kwargs['pk'])
        return queryset
    serializer_class = LocalSerializer
    pagination_class = None

class LocalByCity(generics.ListAPIView):
    def get_queryset(self):
        queryset = Local.objects.filter(city_id=self.kwargs['pk'])
        return queryset
    serializer_class = LocalSerializer
    pagination_class = None

class LocalByCity(generics.ListAPIView):
    def get_queryset(self):
        queryset = Local.objects.filter(city_id=self.kwargs['pk'])
        return queryset
    serializer_class = LocalSerializer
    pagination_class = None

'''class LocalDistance(generics.ListAPIView):
    def get_queryset(self):
        id = map_manager.serilize_distance(map_manager.get_distance(self.kwargs['orig'], self.kwargs['dest']))
        return Distance.objects.filter(id=id)
    serializer_class = DistanceSerializer
    pagination_class = None'''

def LocalDistance(request, orig, dest):
    distance = map_manager.serilize_distance(map_manager.get_distance(orig, dest))
    data = {
        'origin': distance.origin,
        'destination': distance.destination,
        'distance': distance.distance
    }
    return JsonResponse(data)

"""
Rating View
"""

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = MyPagiantion

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = None

class RatingByUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = Rating.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = RatingSerializer
    pagination_class = None

class RatingByLocal(generics.ListAPIView):
    def get_queryset(self):
        queryset = Rating.objects.filter(local_id=self.kwargs['pk'])
        return queryset
    serializer_class = RatingSerializer
    pagination_class = None

def get_rating_media(request, id):
    data = {
        'local_id': id,
        'total_rating': bbdd_manager.get_rate_media(id),
        'rate_amount': bbdd_manager.get_rate_amount(id)
    }
    return JsonResponse(data)

'''def get_rating_media(request):
    objs = Mymodel.objects.all()
    jsondata = serializers.serialize('json', objs)
    return HttpResponse(jsondata, content_type='application/json')'''

"""
Comment View
"""

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = MyPagiantion

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None

class CommentByUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = CommentSerializer
    pagination_class = None

class CommentByLocal(generics.ListAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(local_id=self.kwargs['pk'])
        return queryset
    serializer_class = CommentSerializer
    pagination_class = None
