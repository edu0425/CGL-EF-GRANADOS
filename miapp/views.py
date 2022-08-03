from django.shortcuts import render, HttpResponse

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