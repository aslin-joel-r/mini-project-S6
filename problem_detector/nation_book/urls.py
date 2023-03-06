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
    path('problem_statements/<int:pk>/',views.problem_statement,name='problem_statement'),
    path('problem_statements/<int:pk>/solutions/',views.view_solutions,name='view_solutions'),
    path('problem_statements/<int:pk>/my-problems/',views.my_problems,name='my_problems'),
    path('problem_statements/<int:pk>/my-solution/',views.my_solution,name='my_solution'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)