"""djangoTodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from todo_app import views
from todo_app.views import TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', views.home, name='page-home'),
    path('todo/new', TodoCreateView.as_view(), name='page-todo-new'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='page-todo-detail'),
    path('todo/<int:pk>/update', TodoUpdateView.as_view(), name='page-todo-update'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name='page-todo-delete'),
]
