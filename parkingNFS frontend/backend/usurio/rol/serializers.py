from rest_framework import serializers
from .models import *


class RolSerializer(serializers.ModelSerializer):

    class meta:
        model = Rol
        fields =('_all_')