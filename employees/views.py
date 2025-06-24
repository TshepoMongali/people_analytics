from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

def index(request):
    return render(request, 'worker/index.html')

def employee_list(request):
    employees = Employee.objects.all()
    data = []

    for emp in employees:
        data.append({
            "name": emp.name,
            "position": emp.position,
            "age": emp.age,
            "contract_years": emp.contract_years,
            "shift": emp.shift,
            "performance": emp.performance,
            "retirement_note": "almost due to pension" if emp.age > 55 else ""
        })

    return JsonResponse(data, safe=False)
