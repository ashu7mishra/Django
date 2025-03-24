from rest_framework.serializers import ModelSerializer
from .models import User, ShippingAddress


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class CreateShippingAddressSerializer(ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ["street", "city", "state", "zip_code", "country"]


class ShippingAddressSerializer(ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = "__all__"
