from django.shortcuts import render, redirect

from cuenta.models import Cliente


def carrito(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('credenciales')

    # Obtener carrito de la sesión
    carrito = request.session.get('carrito', {})

    # Preparar datos para la plantilla
    productos_carrito = []
    subtotal = 0
    envio = 8000  # Costo fijo de envío por ahora
    descuento = 0  # Podrías implementar descuentos aquí
    total = subtotal + envio - descuento

    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'carrito.html', {'cliente': cliente,'productos_carrito': productos_carrito,
        'subtotal': subtotal,
        'envio': envio,
        'descuento': descuento,
        'total': total})