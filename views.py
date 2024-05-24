
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import ModelData
from .serializers import ModelDataSerializer

@api_view(['POST'])
@parser_classes([JSONParser])
def import_data(request):
    try:
        data = JSONParser().parse(request)
        for model_data in data:
            for model_name, model_data in model_data.items():
                serializer = ModelDataSerializer(data=model_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    # Zpracujte chybný formát dat
                    error_message = serializer.errors
                    return JsonResponse({'errors': error_message}, status=400)
        return Response({'message': 'Data byla úspěšně importována.'})
    except Exception as e:
        # Zpracujte obecnou chybu
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def get_model_data(request, model_name):
    try:
        model_data = ModelData.objects.filter(model_name=model_name)
        serializer = ModelDataSerializer(model_data, many=True)
        return Response(serializer.data)
    except ModelData.DoesNotExist:
        return JsonResponse({'error': f"Model s názvem '{model_name}' neexistuje."}, status=404)

@api_view(['GET'])
def get_model_data_detail(request, model_name, id):
    try:
        model_data = ModelData.objects.get(model_name=model_name, id=id)
        serializer = ModelDataSerializer(model_data)
        return Response(serializer.data)
    except ModelData.DoesNotExist:
        return JsonResponse({'error': f"Záznam s ID '{id}' v modelu '{model_name}' neexistuje."}, status=404)


