from django.shortcuts import render, HttpResponse
from miapp.models import Producto
from miapp.models import Curso
# Create your views here.   

def inicio(request):
    return render(request,'inicio.html', {
        'mensaje':'Bienvenidos mensaje de prueba',
        })

def integrantes(request):
    estudiantes = ['Edgar Raul Cusi Osccorima',
                   'Carlos Eduardo Granados Pretel',
                   'Sebastian Timo Laura Antezana']
 
    return render(request,'integrantes.html', {
        'titulo':'Integrantes',
        'estudiantes': estudiantes
    })
    
def crearproductos(request):
     return render(request,'crearproductos.html')

def crearcursos(request):
     return render(request,'crearcursos.html')

def crear_producto(request):
    producto = Producto(
        codigo = "1923112547",
        nombre = "Polo",
        precio_compra = 2.2,
        precio_venta =  6.6,
        Fecha_compra =  "2022-08-07 15:00:06",
        estado = 'A'
    )
    producto.save()
    return HttpResponse(f"Producto Creado: {producto.codigo} - {producto.nombre}- {producto.precio_compra}- {producto.precio_venta}-{producto.Fecha_compra}- {producto.estado}")

def crear_curso(request):
    curso=Curso(

	    codigo="IS06S2",
        nombre="MICROPROCESADORES",
        horas=4,
        creditos=3,
        estado="A"
    )
    curso.save()
    return HttpResponse(f"Curso creado: {curso.codigo} {curso.nombre} {curso.horas} {curso.creditos} {curso.estado}")
