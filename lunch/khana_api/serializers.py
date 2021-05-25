from rest_framework import serializers
from khana.models import FoodItem, Order, Shop, Date, TempUser

class FoodItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = ['name', 'price', 'shop']
    # name = models.CharField(max_length=64)
    # price = models.IntegerField()
    # shop = models.IntegerField()

    # def create(self, validated_data):
    #     return FoodItem.objects.create(validated_data)
    
    # def update(self, instance, validated_data):
        
    # def __str__(self):
    #     return f'{self.id} {self.name} {self.price} {self.shop}'
