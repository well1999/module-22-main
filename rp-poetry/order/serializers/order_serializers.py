S

class Orderserializer(serializers.ModelSerializer):
    Product = ProductSerializer(required=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField
    
    def get_total(self,instance):
    total =sun([Product.price for product in instance.product.all()])
    return total

class Meta:
    model = Product
    fields = ['product','total','user','product_id', ]
    extra_kwargs = {'product':{'required':False}}

def create = (self,validated_data):
    Product_data = validated_data.pop('products_id')
    user_data = validated_pop('user')
    
    order = order.objects.create(user=user_data)
    for pruduct in product_data: 
        order.product.add(product)
        return  order    