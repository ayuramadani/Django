from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index_view, name='indexing'),
    # path('polls/', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]