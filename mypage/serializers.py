from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    sex = serializers.ChoiceField(choices=Pet.SEX_CHOICES)
    pet_type = serializers.ChoiceField(choices=Pet.PET_TYPE_CHOICES)

    class Meta:
        model = Pet
        fields = ['pet_id', 'pet_name', 'pet_type', 'sex', 'img']  

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'owner' in validated_data:
            validated_data.pop('owner')
        return super().update(instance, validated_data)
