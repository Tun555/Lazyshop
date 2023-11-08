# import part and view to work
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete)
]
