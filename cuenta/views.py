from django.shortcuts import redirect, render

from cuenta.models import Cliente


def mi_cuenta(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('credenciales')
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'micuenta.html', {'cliente': cliente})