from product.serializers.product_serializers import ProductSerializer
class Orderserializer(serializer.ModelSerializers):
    product = ProductSerializer(read_only=True, many=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, instance):
        total = sum ([product.price for product in instance.product.all()])
        return total
    
    class Meta:
        model = order 
        fields =  ['product', 'total','user', 'products_id']
        extra_kwargs = {'product':{'required':False}}
        