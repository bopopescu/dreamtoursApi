from django.urls import path

from dreamtours_app.views import *#UserList, UserDetail, UserByCity

urlpatterns = [
    path('v1/user/', UserList.as_view(), name='User List'),
    path('v1/user/<int:pk>', UserDetail.as_view(), name='User Detail'),
    path('v1/city/', CityList.as_view(), name='City List'),
    path('v1/city/<int:pk>', CityDetail.as_view(), name='City Detail'),
    path('v1/particular/', ParticularList.as_view(), name='Particular List'),
    path('v1/particular/<int:pk>', ParticularDetail.as_view(), name='Particular Detail'),
    path('v1/particular/city/<int:pk>', ParticularByCity.as_view(), name='Particular By City'),
    path('v1/company/', CompanyList.as_view(), name='Company List'),
    path('v1/company/<int:pk>', CompanyDetail.as_view(), name='Company Detail'),
    path('v1/localtype/', LocalTypeList.as_view(), name='LocalType List'),
    path('v1/localtype/<int:pk>', LocalTypeDetail.as_view(), name='LocalType Detail'),
    path('v1/local/', LocalList.as_view(), name='Local List'),
    path('v1/local/<int:pk>', LocalDetail.as_view(), name='Local Detail'),
    path('v1/local/city/<int:pk>', LocalByCity.as_view(), name='Local By City'),
    path('v1/local/type/<int:pk>', LocalByType.as_view(), name='Local By City'),
    path('v1/local/company/<int:pk>', LocalByCompany.as_view(), name='Local By City'),
    path('v1/local/distance/<path:orig>/<path:dest>', LocalDistance.as_view(), name='Local Distance'),
    path('v1/rating/', RatingList.as_view(), name='Rating List'),
    path('v1/rating/<int:pk>', RatingDetail.as_view(), name='Rating Detail'),
    path('v1/rating/local/<int:pk>', RatingByLocal.as_view(), name='Rating By City'),
    path('v1/rating/user/<int:pk>', RatingByUser.as_view(), name='Rating By City'),
    path('v1/comment/', CommentList.as_view(), name='Comment List'),
    path('v1/comment/<int:pk>', CommentDetail.as_view(), name='Comment Detail'),
    path('v1/comment/local/<int:pk>', CommentByLocal.as_view(), name='Comment By City'),
    path('v1/comment/user/<int:pk>', CommentByUser.as_view(), name='Comment By City'),
]