from rest_framework import serializers
from api.models import ADUser
from components.helper.sam_account_name_helper import create_sam_account_name


class ADUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ADUser
        fields = '__all__'

    def create(self, validated_data):
        ad_user = ADUser.objects.create(**validated_data)
        ad_user.SAM_account_name = create_sam_account_name(ad_user.first_name, ad_user.last_name, ad_user.pager)
        ad_user.save()
        return ad_user
