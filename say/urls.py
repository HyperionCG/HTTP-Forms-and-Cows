from django.urls import path

from say import views

urlpatterns = [
    path('',views.index, name ='homepage'),
    path('history/',views.historyview)
    #path('admin/', admin.site.urls),
]
