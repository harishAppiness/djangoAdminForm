from contextlib import redirect_stderr, redirect_stdout
from webbrowser import get
from django.shortcuts import render , redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser

from settings.models import ApplicationSettings
from django.http.response import JsonResponse
from .serializers import ApplicationSettingsSerializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
class Application_Settings(ModelViewSet):
    
    @staticmethod
    def getApplicationSettings(request):
        allObjects = ApplicationSettings.objects.all()
        serializedData=ApplicationSettingsSerializers(allObjects, many=True)
        allObjects = serializedData.data
        return render( request,'home.html',{'allObjects' : allObjects})


@csrf_exempt 
def createApplicationSettings(request):
        allObjects = ApplicationSettings.objects.all()
        serializer = ApplicationSettingsSerializers(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        return JsonResponse('Failed to add',safe=False)  



@csrf_exempt 
def deleteApplicationSettings(request, id):
    allObjects = ApplicationSettings.objects.all()
    appli_settings = ApplicationSettings.objects.filter(id=id)
    appli_settings.delete()
    return redirect('/')      

@csrf_exempt 
def showUpdatePage(request , id):
    appli_settings = ApplicationSettings.objects.get(id=id)
    print(appli_settings)
    return render(request, 'update.html' ,{'appli_settings' : appli_settings})

@csrf_exempt 
def updateApplicationSettings(request,id):
    receivedData = request.POST
    appli_settings = ApplicationSettings.objects.get(id=id)
    serializer = ApplicationSettingsSerializers(appli_settings,data=receivedData)
    if serializer.is_valid():
        serializer.save()
        return redirect('/')
    return JsonResponse('Update failed',safe=False)         
