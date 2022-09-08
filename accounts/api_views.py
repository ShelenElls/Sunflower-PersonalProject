from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import User

class AccountDetailModelEncoder(ModelEncoder):
    model = User
    properties = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "password",
        "picture_url",
    ]



@require_http_methods(["GET", "POST"])
def api_user(request):
    if request.method == "GET":
        user = User.objects.all()
        return JsonResponse(
            {"user": user},
            encoder=AccountDetailModelEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        newuser = User.objects.create_user(**content)
        return JsonResponse(
            newuser,
            encoder=AccountDetailModelEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "PUT", "GET"])
def api_user_change(request, pk):
    if request.method == "DELETE":
        count, _ = User.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    elif request.method == "PUT":
        content = json.loads(request.body)
        user = User.objects.filter(id=pk).update(**content)
        return JsonResponse(
            user,
            encoder=AccountDetailModelEncoder,
            safe=False,
        )
    else:
        user = User.objects.get(id=pk)
        return JsonResponse(
            user,
            encoder=AccountDetailModelEncoder,
            safe=False,
        )