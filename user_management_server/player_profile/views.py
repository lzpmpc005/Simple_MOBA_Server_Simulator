import json
from django.http import JsonResponse
from .models import Player, Character, CharacterClass
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_player(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'}, status=400)

        account = data.get("account")
        password = data.get("password")
        
        new_player = Player(
            account = account, 
            password = password, 
            )
        
        try:
            new_player.save()
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

        return JsonResponse({'status': 'success', 'message': 'New player created.'})

    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})

@csrf_exempt
def create_character(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'}, status=400)

        name = data.get("name")
        account = data.get("account")
        character_type = data.get("character_type")

        try:
            player = Player.objects.using('default').get(pk=account)
        except Player.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Player does not exist.'}, status=400)
        
        try:
            class_type = CharacterClass.objects.using('default').get(pk=character_type)
        except CharacterClass.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Character type does not exist.'}, status=400)
        
        new_character = Character(
            name = name,
            player = player,
            class_type = class_type
            )
        
        try:
            new_character.save()
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

        return JsonResponse({'status': 'success', 'message': 'New character created.'})

    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})

def example(request):
    if request.method == 'GET':
        data = {
            'message': 'Hello from Django!'
        }
        return JsonResponse(data)
    else:
        error_data = {
            'error': 'Only GET requests are allowed.'
        }
        return JsonResponse(error_data, status=405)
