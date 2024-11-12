from django.contrib import admin
from app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('setting/', views.setting, name='setting'),
    path('hot/', views.hot, name='hot'),
    path('registration/', views.registration, name='registration'),
    path('single/', views.single, name='single'),
    path('tag/blablabla', views.tag, name='tag'),
    path('question/<int:question_id>/', views.question, name='one_question'),
]
