from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from parkapp.models import  tipovehiculo, empleados, vehiculos, ticket
from parkapp.Forms import tipovehiculoForm, empleadosForm, loginForm, ticketForm
from django.contrib import messages
from datetime import datetime

autenticacion = False
usuario = None
instancia = None

def list_tipos(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    return render_to_response("tipovehiculo.html", {"tipovehiculo": tipovehiculo.objects.all(), "messages": messages.get_messages(request), 'usuario' : usuario})

def update_tipo(request, tipoid):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    instance = get_object_or_404(tipovehiculo, id=tipoid)
    form = tipovehiculoForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El tipo de vehiculo ha sido actualizado!")
            return HttpResponseRedirect("/tipos/list/")
    return render(request, 'form_tipovehiculo.html', {'form': form, 'usuario' : usuario} )

def list_usuarios(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    return render_to_response("empleados.html", {"empleados": empleados.objects.all(), "messages": messages.get_messages(request), 'usuario' : usuario})

def add_usuario(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    form = empleadosForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El usuario ha sido guardado!")
            return HttpResponseRedirect("/usuarios/list/")

    return render(request, 'form_empleados.html', {'form': form, 'usuario' : usuario})

def update_usuario(request, usuarioid):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    instance = get_object_or_404(empleados, id=usuarioid)
    form = empleadosForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El usuario ha sido actualizado!")
            return HttpResponseRedirect("/usuarios/list/")

    return render(request, 'form_empleados.html', {'form': form, 'usuario' : usuario})

def delete_usuario(request, usuarioid):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    instance = get_object_or_404(empleados, id=usuarioid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El usuario con id %s ha sido borrado!" % usuarioid)
    return HttpResponseRedirect("/usuarios/list/")

def login(request):
    form_class = loginForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                user = request.POST['usuario']
                query = empleados.objects.get(usuario=user)
                if query.clave == request.POST['contraseña']:
                    global autenticacion
                    autenticacion=True
                    global usuario
                    usuario = user
                    print(usuario)
                    return HttpResponseRedirect("/ticket/add/")
                else:
                    messages.add_message(request, messages.ERROR, "Contraseña incorrecta")
            except empleados.DoesNotExist:
                    messages.add_message(request, messages.ERROR, "El usuario ingresado no existe")
    return render(request, 'login.html', {'form': form, "messages": messages.get_messages(request)})

def tickets(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    form_class = ticketForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            placa = request.POST['placa']
            tipo = request.POST['tipovehiculo']
            v = vehiculos(placa=placa, tipovehiculo= tipovehiculo.objects.get(pk=tipo))
            v.save()
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t = ticket(fechain=fecha, fechaout=fecha, total=0, vehiculos=vehiculos.objects.latest('id'))
            t.save()
        else:
            print("Form invalido")
    tabla = ticket.objects.filter(estado=False)
    return render(request, 'tickets.html', {'form': form, 'tabla' : tabla, 'usuario' : usuario})

def logout(request):
    messages.add_message(request, messages.SUCCESS, "Ha cerrado la sesión satisfactoriamente")
    global autenticacion
    autenticacion = False
    return render(request, 'logout.html', {"messages": messages.get_messages(request)})

def calcular(request, ticketid):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    global instancia
    instancia = get_object_or_404(ticket, id=ticketid)
    instancia.fechaout = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    instancia.fechaout = datetime.strptime(instancia.fechaout, "%Y-%m-%d %H:%M:%S")
#    fin = datetime.strptime(instancia.fechaout, "%Y-%m-%d %H:%M:%S")
    print(instancia.fechaout)
    print(instancia.fechain)
    diferencia = instancia.fechaout - instancia.fechain
    total = 0
    segundos = 0
    if(diferencia.days >= 1):
        segundos = diferencia.days * 86400
    horas = int (((diferencia.seconds + segundos) / 60) / 60) + 1
    print(diferencia.seconds + segundos)
    print(horas)
    if(horas > 0):
        total = instancia.vehiculos.tipovehiculo.tarifa * horas
    else:
        total = instancia.vehiculos.tipovehiculo.tarifa
    instancia.total = total
    return render(request, 'calcular.html', {'ins': instancia, 'dif' : diferencia})

def confirmar(request):
    if(autenticacion == False):
        messages.add_message(request, messages.ERROR, "Primero inicia sesión")
        return HttpResponseRedirect("/login")
    global instancia
    instancia.estado = True
    instancia.save()
    messages.success(request, "Vehiculo retirado satisfactoriamente")
    return HttpResponseRedirect("/ticket/add/")
