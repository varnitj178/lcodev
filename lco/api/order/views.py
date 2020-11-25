from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt



def validate_user_session(id,token):
    UserModel = get_user_model()
    try:
        user = UserModel.object.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id ,token):
        return JsonResponse({'error': 'please re-login','code':'1' })

    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['product']

        total_pro = len(products.split(',')[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.object.get(pk = user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error':'User does not exist'})

        ordr = Order(user=user,products_names=products,total_products=total_pro,transaction_id = transaction_id,total_amount=amount)
        ordr.save()
        return JsonResponse({'success' : True,'error' :False,'msg' : 'order'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer