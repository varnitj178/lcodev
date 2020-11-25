from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt


import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="vcd2gx4568s7ybx9",
        public_key="y2jpypws7b5pxpnm",
        private_key="44ab3bb8db8457afa4865555a7b4c739"
    )
)


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
def generate_token(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error': 'Invalid session !!'})

    return JsonResponse({'clientToken': gateway.client_token.generate(),'success':True})

@csrf_exempt
def process_payment(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error': 'Invalid session !!'})

    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = gateway.transaction.sale({
        "amount":amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options":{
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        return JsonResponse({
            'success': result.is_success,
            'transaction': {'id':result.transaction.id,'amount':result.transaction.amount}
        })
    else:
        return JsonResponse({'error':True,'success': False})