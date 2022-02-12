from django.http import HttpResponse
from datetime import datetime
from datetime import date
from django.template import Template, Context

def saludo(request):return HttpResponse("Hola Django - Coder")
def segunda_vista(request):return HttpResponse("<h1>Hola!</h1></br><p>Recuerden que esta es mi segunda vista</p>")
def DiaDeHoy(request):
    dia = datetime.now()
    DocumentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(DocumentoDeTexto)

def mi_nombre(self,nombre):
    DocumentoDeTexto2 = f'Mi nombre es: <br><br> {nombre}'

    return HttpResponse(DocumentoDeTexto2)

def AñoNacimiento(self,edad,mescumpleaños):
    AñoActual = format(date.today().year)
    MesActual = format(date.today().month)
    if MesActual>mescumpleaños:
        DocumentoDeTexto3 = f'Naciste en el año: <br><br> {int(AñoActual)-int(edad)}'
    else:
        DocumentoDeTexto3 = f'Naciste en el año: <br><br> {int(AñoActual)-int(edad)-1}'

    return HttpResponse(DocumentoDeTexto3)

def ProbandoTemplate(self):
    miHtml = open ("C:/Users/lemira/ProyectoDjango/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHtml.read()) #se carga en memoria nuestro documento, Template1.
    miHtml.close()
    miContexto = Context() #en este caso no hay nada, ya que no hay parámetros, pero igual hay que crearlo
    documento = plantilla.render (miContexto) #acá renderizamos la plantilla en documento

    return HttpResponse(documento)

