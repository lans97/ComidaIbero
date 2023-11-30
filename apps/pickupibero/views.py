from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import customLoginForm

from .models import Restaurante, Producto, Orden, OrdenItem

def landing(request):
    context = {}

    lista_restaurantes = Restaurante.objects.all()
    context['restaurantes'] = lista_restaurantes

    return render(request, "restaurantes.html", context)

def menu_view(request, rest_id):
    context = {}
    rest = Restaurante.objects.get(id=rest_id)
    context['restaurante'] = rest
    menu = Producto.objects.filter(restaurante=rest, is_topping=False)
    context['menu'] = menu
    return render(request, "menu.html", context)

def producto_view(request, producto_id):
    context = {}
    producto = Producto.objects.get(pk=producto_id)
    context['producto'] = producto
    relationships = producto.allowable_toppings.all()
    toppings = [r.topping for r in relationships]
    context['toppings'] = toppings
    return render(request, "producto.html", context)

def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('landing')
    if request.method == 'POST':
        form = customLoginForm(request.POST)
        if form.is_valid():
            ncuenta = form.cleaned_data.get('ncuenta')
            digitov = form.cleaned_data.get('digitov')
            password = form.cleaned_data.get('password')

            username = str(ncuenta) + "-" + str(digitov)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Authentication successful, log the user in
                login(request, user)
                return redirect('landing')
            else:
                # Authentication failed, handle accordingly
                form.add_error('ncuenta', 'Invalid credentials')  # Add error to the form

    else:
        form = customLoginForm()

    context['form'] = form
    return render(request, "login/login.html", context)

def logout_view(request):
    logout(request)
    next_url = request.POST.get('next') or request.GET.get('next') or 'landing'
    return redirect(next_url)


@login_required
def agregar_a_carrito(request):
    producto_id = request.POST.get('producto_id')

    if 'carrito' not in request.session:
        request.session['carrito'] = {}
        
    carrito = request.session['carrito']
    
    toppings = request.POST.getlist('topping', [])
    
    numItem = 1
    while str(numItem) in carrito:
        numItem += 1
    
    parentItem = 0

    carrito[str(numItem)] = {
        "parentItem": parentItem,
        "producto": producto_id,
    }
    
    parentItem = numItem
    for t in toppings:
        numItem += 1
        producto_id = int(t)
        carrito[str(numItem)] = {
            "parentItem": parentItem,
            "producto": producto_id,
        }
        
    request.session.modified = True
    
    return redirect('landing')

@login_required
def carrito_view(request):
    context = {}
    carrito = request.session.get('carrito', {})
    productos = []
    
    total = 0
    for numItem, item in carrito.items():
        producto_id = item.get('producto')
        producto = Producto.objects.get(pk=producto_id)
        is_topping = producto.is_topping
        total += producto.precio_unitario
        
        productos.append({
            'numItem': numItem,
            'nombre': producto.nombre,
            'precio_unitario': producto.precio_unitario,
            'is_topping': is_topping,
        })

    context['productos'] = productos
    context['total'] = total

    return render(request, "carrito.html", context)
        
@login_required
def borrar_del_carrito(request, numItem):
    carrito = request.session.get('carrito', {})

    if numItem in carrito:

        carrito = {k: v for k, v in carrito.items() if k != numItem and v.get('parentItem') != int(numItem)}
        
        request.session['carrito'] = carrito
        request.session.modified = True

    return redirect('carrito')

@login_required
def comprar_carrito(request):
    carrito = request.session.get('carrito', {})
    
    if carrito == {}:
        return redirect('landing')

    usuario = request.user
    ordenes = {}
    for numItem, item in carrito.items():
        producto = Producto.objects.get(pk=item.get('producto'))
        if str(producto.restaurante.pk) not in ordenes:
            ordenes[str(producto.restaurante.pk)] = Orden.objects.create(usuario=usuario, restaurante=producto.restaurante, estado='a', notas="")
        OrdenItem.objects.create(orden=ordenes[str(producto.restaurante.pk)], numItem=int(numItem), parentItem=int(item.get('parentItem')), producto=producto)

    request.session['carrito'] = {}
    request.session.modified = True
    
    return redirect('orden-creada')
        
@login_required
def orden_creada(request):
    context = {}
    usuario  = request.user
    ordenes = Orden.objects.filter(usuario=usuario, estado="a")
    context['ordenes'] = ordenes
    return render(request, "orden-creada.html", context)