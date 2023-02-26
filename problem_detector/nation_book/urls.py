#app level urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('about_us/',views.about_us,name='about_us'),
    path('problem_statements/',views.problem_statements,name='problem_statement'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)