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
            "email": emp.email,
            "retirement_note": "almost due to pension" if emp.age > 55 else "",
            "performance_note":"keep up with work" if emp.performance <5 else "good work"
        })

    return JsonResponse(data, safe=False)
