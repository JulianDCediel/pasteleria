from django.shortcuts import redirect, render

from gestion_empleados.models import Empleado


def menu_empleado(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('LoginEmp')
    empleado = Empleado.objects.get(id=empleado_id)
    return render(request, 'menu_empleados.html', {'empleado': empleado})