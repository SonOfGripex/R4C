from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #Отключил проверку csrf токена
from .forms import RobotForm
from .models import Robot


@csrf_exempt
def robots_list(request):
    if request.method == 'GET':
        robots = Robot.objects.all().values()
        data = list(robots)
        return JsonResponse(data, status=200, safe=False)
    else:
        return JsonResponse({'error': 'invalid method'}, status=400, safe=False)


@csrf_exempt
def add_robot(request):
    if request.method == 'POST':
        form = RobotForm(request.POST)
        if form.is_valid():
            try:
                new_robot = form.save()
                robot_dict = model_to_dict(new_robot)
                robot_dict['created'] = new_robot.created.strftime('%Y-%m-%d')
                return JsonResponse(robot_dict, status=201, safe=False)
            except Exception as e:
                return JsonResponse({"error": e}, status=500)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return JsonResponse({'error':'invalid method'}, status=400)