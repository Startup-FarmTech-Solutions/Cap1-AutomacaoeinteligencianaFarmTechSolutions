from django.urls import path
from .views import LeituraSensorListCreateView

urlpatterns = [
    path('leituras/', LeituraSensorListCreateView.as_view(), name='leituras'),
]
