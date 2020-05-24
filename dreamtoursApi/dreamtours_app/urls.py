from django.urls import path

from dreamtours_app.views import *#UserList, UserDetail, UserByCity

v = 'v2'

urlpatterns = [
    path(v+'/user/', UserList.as_view(), name='User List'),
    path(v+'/user/<int:pk>', UserDetail.as_view(), name='User Detail'),
    path(v+'/city/', CityList.as_view(), name='City List'),
    path(v+'/city/<int:pk>', CityDetail.as_view(), name='City Detail'),
    path(v+'/particular/', ParticularList.as_view(), name='Particular List'),
    path(v+'/particular/<int:pk>', ParticularDetail.as_view(), name='Particular Detail'),
    path(v+'/particular/city/<int:pk>', ParticularByCity.as_view(), name='Particular By City'),
    path(v+'/company/', CompanyList.as_view(), name='Company List'),
    path(v+'/company/<int:pk>', CompanyDetail.as_view(), name='Company Detail'),
    path(v+'/localtype/', LocalTypeList.as_view(), name='LocalType List'),
    path(v+'/localtype/<int:pk>', LocalTypeDetail.as_view(), name='LocalType Detail'),
    path(v+'/local/', LocalList.as_view(), name='Local List'),
    path(v+'/local/<int:pk>', LocalDetail.as_view(), name='Local Detail'),
    path(v+'/local/city/<int:pk>', LocalByCity.as_view(), name='Local By City'),
    path(v+'/local/type/<int:pk>', LocalByType.as_view(), name='Local By City'),
    path(v+'/local/company/<int:pk>', LocalByCompany.as_view(), name='Local By City'),
    path(v+'/local/distance/<path:orig>/<path:dest>', LocalDistance, name='Local Distance'),
    path(v+'/rating/', RatingList.as_view(), name='Rating List'),
    path(v+'/rating/<int:pk>', RatingDetail.as_view(), name='Rating Detail'),
    path(v+'/rating/local/<int:pk>', RatingByLocal.as_view(), name='Rating By City'),
    path(v+'/rating/user/<int:pk>', RatingByUser.as_view(), name='Rating By City'),
    path(v+'/rating/media/<path:id>', get_rating_media, name='Rating Media'),
    path(v+'/comment/', CommentList.as_view(), name='Comment List'),
    path(v+'/comment/<int:pk>', CommentDetail.as_view(), name='Comment Detail'),
    path(v+'/comment/local/<int:pk>', CommentByLocal.as_view(), name='Comment By City'),
    path(v+'/comment/user/<int:pk>', CommentByUser.as_view(), name='Comment By City'),
]