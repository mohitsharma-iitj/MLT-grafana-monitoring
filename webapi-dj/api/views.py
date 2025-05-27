from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
import json
import logging
from opentelemetry import trace
tracer = trace.get_tracer(__name__)

logger = logging.getLogger(__name__)

# uncomment below line to check log saving in webapi.log file
# logger.error("Log1 on Webapi m1!") #; this always runs whenever any api from this file is called, so better to comment it out or remove it
@csrf_exempt
def index(request):
    logger.info("✅ Successful execution of GET / on Webapi")
    # create log for success, 
    return render(request, 'api/index.json')

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = int(data.get('x', 0))
            b = int(data.get('y', 0))
            result = a + b
            time.sleep(0.5)
            logger.info("✅ Successful execution of POST/add on Webapi")
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    logger.error("❌ Error in POST /add, method not allowed")
    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def multiply(request):
    with tracer.start_as_current_span("Heavy task") as span:
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                x = int(data.get('x', 1))
                y = int(data.get('y', 1))
                result = x * y
                time.sleep(0.5)
                logger.info("✅ Successful execution of POST/multiply on Webapi")
                return JsonResponse({'result': result})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        logger.error("❌ Error in POST /multiply, method not allowed")
        return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def echo(request):
    logger.error("Log1 on Webapi/echo, GET /!")   #not a error, just defining it
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse({'received': data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def health_check(request):
    logger.info("✅ Health check endpoint called")
    return JsonResponse({'status': 'healthy', 'uptime': 'OK', 'code': 200})