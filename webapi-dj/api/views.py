from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
import json


@csrf_exempt
def index(request):
    return render(request, 'api/index.json')

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = int(data.get('a', 0))
            b = int(data.get('b', 0))
            result = a + b
            time.sleep(0.5)
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def multiply(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            x = int(data.get('x', 1))
            y = int(data.get('y', 1))
            result = x * y
            time.sleep(0.5)
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def echo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse({'received': data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def health_check(request):
    return JsonResponse({'status': 'healthy', 'uptime': 'OK', 'code': 200})