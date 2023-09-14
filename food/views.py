from django.shortcuts import render
from .models import Food, Store
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from posts.views import uploadOntoS3
from geopy.distance import geodesic
from django.core import serializers
import json

# Create your views here.
@csrf_exempt
def food(request, food_id):
    if request.method == "GET":
        food = Food.objects.get(food_id)
        if food is None:
            return JsonResponse({"status": f"Did not found food {food_id}"}, status=404)
        else:
            return JsonResponse({"status": "success", 'results': food}, status=200)
        
    elif request.method == "POST":
        
        name = request.POST.get('name', '')
        store_id = int(request.POST.get('store_id', ''))
        price = float(request.POST.get('price', ''))

        # TODO: add image link
        
        # check if all fields are empty
        if name == '' or store_id == '' or price == '':
            return JsonResponse({"status": "error", "message": "All fields must be filled"}, status=400)
        
        # check if store is not exists
        store = Store.objects.get(store_id)
        if store is None:
            return JsonResponse({"status": "error", "message": "Store does not exists"}, status=400)
    
        food = Food(name=name, store_id=store_id, price=price)
        food.save()

        return JsonResponse({"status": "success", "message": "Food added successfully"}, status=200)
    
    elif request.method == "PUT":
        name = request.POST.get('name', '')
        store_id = int(request.POST.get('store_id', ''))
        price = float(request.POST.get('price', ''))

        # TODO: add image link

        food = Food.objects.get(food_id)
        if food is None:
            return JsonResponse({"status": "error", "message": "Food does not exists"}, status=400)

        if name == '' and store_id == '' and price == '':
            return JsonResponse({"status": "error", "message": "At least one field must be filled"}, status=400)

        # Update each field
        if name != '':
            food.name = name
        if store_id != '':
            food.store_id = store_id
        if price != '':
            food.price = price
        
        food.save()

        return JsonResponse({"status": "success", "message": "Food updated successfully"}, status=200)
    
    elif request.method == "DELETE":
        food = Food.objects.get(food_id)
        if food is None:
            return JsonResponse({"status": "error", "message": "Food does not exists"}, status=400)

        food.delete()

        return JsonResponse({"status": "success", "message": "Food deleted successfully"}, status=200)
    
    else:
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)
    
def search(request):
    if request.method == "GET":
        query = request.GET.get('query', '')
        offset = int(request.GET.get('offset', '0'))
        limit = int(request.GET.get('limit', '10'))
        latitude = float(request.GET.get('latitude', '0'))
        longitude = float(request.GET.get('longitude', '0'))
        distance = float(request.GET.get('distance', '0'))
        
        if query == '':
            return JsonResponse({"status": "error", "message": "Query must be filled"}, status=400)
        
        foods = Food.objects.filter(name__contains=query)

        demo_foods = []
        filtered_foods = []
        for food in foods:
            if(len(demo_foods) >= limit + offset):
                break
            demo_foods.append(food)
            store = None
            try:
                store = Store.objects.get(food.store)
            except:
                pass
            if store:
                food_distance = geodesic((latitude, longitude), (store.latitude, store.longitude)).km
                if food_distance <= distance:
                    filtered_foods.append(food)

        results = filtered_foods[offset:offset+limit]

        results = demo_foods

        results_json = serializers.serialize('json', results)
        
        return JsonResponse({"status": "success", "results": json.loads(results_json)}, safe=False, status=200)

def search_autocomplete(request):
    return HttpResponse("Autocomplete", status=200)