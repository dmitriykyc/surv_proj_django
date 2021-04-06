from django.urls import path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('user/delete/<int:user_pk>/', adminapp.delete_user, name='user_delete')
]
