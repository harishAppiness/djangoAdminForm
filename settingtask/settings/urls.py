from django.urls import path
from .views import Application_Settings
from .views import createApplicationSettings,deleteApplicationSettings , showUpdatePage , updateApplicationSettings

urlpatterns=[
    path('', Application_Settings.as_view({'get': 'getApplicationSettings'})),
    path('create/' ,createApplicationSettings),
    path('delete/<int:id>',deleteApplicationSettings ),
    path('update/<int:id>',showUpdatePage ),
    path('update/edit/<int:id>/',updateApplicationSettings ),
    
]