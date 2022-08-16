from django.urls import re_path, path
from eventex.subscriptions.views import new,detail


app_name= "subscriptions"

urlpatterns = [
    path('', new, name='new'),
    re_path(r'^([\w-]+)/', detail, name='detail'),

]
