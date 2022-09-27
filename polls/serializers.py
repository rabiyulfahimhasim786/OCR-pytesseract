from rest_framework import serializers
from .models import Dropbox#, Standards, Countries, Tag


class DropboxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dropbox
    fields = '__all__'