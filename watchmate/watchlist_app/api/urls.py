from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                    StreamPlatformAV, StreamDetailAV, ReviewList, ReviewDetail, ReviewCreate,
                    StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('movie-list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='streamplatform'),
    # path('stream/<int:pk>', StreamDetailAV.as_view(), name='streamplatform-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/reviews/',ReviewList.as_view(), name='review-list'),
    path('<int:pk>/create-review/',ReviewCreate.as_view(), name='create-review'),
    path('review/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),
]
