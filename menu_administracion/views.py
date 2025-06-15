from django.shortcuts import render, redirect

from gestion_empleados.models import Empleado


def menu_admin(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('LoginEmp')
    empleado = Empleado.objects.get(id=empleado_id)
    return render(request, 'menu_admin.html', {'empleado': empleado})