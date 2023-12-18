from django.urls import path

from api.created_post.views import createdViews, createdFeedBackViews, createDirectoryViews, createDirectorySwadViews, \
            createdPostDataViews, IecMaterialDataViews

urlpatterns = [
    path('list/', createdViews.as_view(), name='api_createdPost_list'),
    path('feedbackviews/',createdFeedBackViews.as_view(), name='api_createdFeedBackViews'),
    
    #DIRECTORY
    path('directoryviews/', createDirectoryViews.as_view(), name='api_createDirectoryViews'),
    #VIEWS
    path('directoryswadviews/', createDirectorySwadViews.as_view(), name='api_createDirectorySwadViews'),
    #FORDIRECT
    path('createdpostviews/', createdPostDataViews.as_view(), name='apo_createdPostDataViews'),

    path('iecmaterialviews/', IecMaterialDataViews.as_view(), name='IecMaterialDataViews')
]