from django.http import JsonResponse

def transformer(request):
    departamentos = {
        "BARRANQUILLA": "ATLANTICO",
        "BOGOTA": "REGION METROPOLITANA BOGOTA CUNDINAMARCA",
        "STA MARTA": "MAGDALENA",
        "CARTAGENA": "BOLIVAR"
    }
    if request.method == "GET":
        ciudad = request.GET["ciudad"]
        if ciudad in departamentos:
            return JsonResponse({"DEPARTAMENTO": departamentos[ciudad]})
        else:
            return JsonResponse({"DEPARTAMENTO": "NO ENCONTRADO"})