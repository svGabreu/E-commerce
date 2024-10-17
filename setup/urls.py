from django.contrib import admin
from django.urls import path
#from adm.views import index
from adm.views import admListView
from adm.views import admCreateView
from adm.views import admUpdateView
from adm.views import admDeleteView
from django.urls import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", admListView.as_view()),
    path("create", admCreateView.as_view()),
    path("update", admUpdateView.as_view()),
    path("delete", admDeleteView.as_view())
]
