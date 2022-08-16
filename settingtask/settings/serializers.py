from rest_framework import serializers
from .models import ApplicationSettings


class ApplicationSettingsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ApplicationSettings
        fields = '__all__'