from django.contrib import admin
from django.urls import path
#from adm.views import index
from adm.views import admListView, admCreateView, admUpdateView, admDeleteView
from django.urls import reverse_lazy

urlpatterns = [
    path("", admListView.as_view(),name='adm_list'),
    path("create", admCreateView.as_view(),name='adm_create'),
    path("update/<int:pk>/", admUpdateView.as_view(),name='adm_update'),
    path("delete/<int:pk>/", admDeleteView.as_view(),name='adm_delete')
]
