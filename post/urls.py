from django.urls import path,include
from .views import PostListView,VoteCreateView, PostRetrieveDestroyView

urlpatterns = [    
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/vote', VoteCreateView.as_view(), name='posts' ),
    path('<int:pk>/', PostRetrieveDestroyView.as_view(), name='post-delete')
    
]