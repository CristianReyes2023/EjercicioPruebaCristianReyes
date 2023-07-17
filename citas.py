from curses.ascii import isalnum, isalpha
import os
import core
from datetime import datetime
import random
diccCitas={}

def loadInfoCitas():
    global diccCitas
    if(core.checkFile("citas.json")):
        diccCitas = core.loadInfo('citas.json')
    else:
        core.crearInfo('citas.json',diccCitas)
    
def MainMenu():
    os.system('cls') and os.system('clear')
    isMainMenu = True
    print('+','-'*45,'+')
    print('|{:^12}{}{:^11}|'.format('','GESTION DE CITAS MEDICAS',''))
    print('+','-'*45,'+')
    print('1. Agregar Citas','2. Buscar Citas','3. Modificar Citas','4. Eliminar cita','5. Salir',sep='\n')
    isValid = True
    while isValid:
        try:
            opcion = int(input("Ingresa la opcion de busqueda: "))
            False
        except ValueError:
            print("Ingresa un numero entero")
        else:
            isValid = False
    if(opcion==1):
        os.system('cls') and os.system('clear')
        print('+','-'*45,'+')
        print('|{:^14}{}{:^14}|'.format('','AGREGAR CITA MEDICA',''))
        print('+','-'*45,'+')
        numeroCita=str(random.randint(1,10000)).zfill(5)
        nombrePaciente=input("Ingresa nombre del paciente: ").upper()
        while(True):
            fecha_str=input("Ingresa fecha en formato dd-mm-yyyy: ")
            try:
                fecha = datetime.strptime(fecha_str,"%d-%m-%Y").date()
                break
            except ValueError:
                print('Fecha no valida.Ingresar nueva fecha')
        fechaFinal=fecha.strftime("%d-%m-%Y")
        print('','NOTA:LAS CITAS SE ASIGNAN CADA MEDIA HORA','',sep='\n')
        while(True):
            hora_str=input("Ingresa hora en formato de 24H HH:MM: ")
            try:
                hora = datetime.strptime(hora_str,"%H:%M").time()
                break
            except ValueError:
                print('Hora no valida.Ingresar nueva hora')
        horaFinal=hora.strftime("%H:%M")
        try:
            for key,value in diccCitas.items():
                if(value['fechaCita'] == fechaFinal and value['horaCita'] == horaFinal):
                    print("Ya existe una cita en esa fecha y hora")
                    pause=input("Pause, presiona ENTER para continuar")
                    MainMenu()
        except Exception:
            print("Error: Se volvera al menu principal")
            MainMenu()       
        motivo=input("Motivo de la cita: ").upper()
        cita={
            'citaNumero':numeroCita,
            'nombrePaciente':nombrePaciente,
            'fechaCita':fechaFinal,
            'horaCita':horaFinal,
            'motivo':motivo
        }
        diccCitas.update({f"{numeroCita}":cita})
        core.crearInfo('citas.json',diccCitas)
    elif(opcion==2):
        os.system('cls') and os.system('clear')
        print('+','-'*45,'+')
        print('|{:^15}{}{:^14}|'.format('','BUSCAR CITA MEDICA',''))
        print('+','-'*45,'+')
        print('Buscar Cita por: ','1. Nombre paciente','2. Fecha cita',sep='\n')
        isValid = True
        while isValid:
            try:
                opcion = int(input("Ingresa la opcion de busqueda: "))
                False
            except ValueError:
                print("Ingresa un numero entero")
            else:
                isValid = False
            
        if(opcion == 1):
            i=1
            j=0
            nombreBusqueda = input("Ingresa nombre del paciente:").upper()
            contador=len(diccCitas)
            for key,value in diccCitas.items():
                if(value['nombrePaciente'] == nombreBusqueda):
                    print("-"*25)
                    print(f"Cita # = {value['citaNumero']}")
                    print(f"Paciente = {value['nombrePaciente']}")
                    print(f"Fecha = {value['fechaCita']}")
                    print(f"Hora = {value['horaCita']}")
                    print(f"Motivo = {value['motivo']}")
                    print("-"*25)
                    j+=1
                elif(contador==i and j==0):
                    print("No se encontre cita con el nombre ingresado")
                i+=1
            pause=input("Pause, presiona ENTER para continuar")
            MainMenu()
        elif(opcion == 2):
            i=1
            j=0
            while(True):
                fecha_str=input("Ingresa fecha en formato dd-mm-yyyy: ")
                try:
                    fecha = datetime.strptime(fecha_str,"%d-%m-%Y").date()
                    break
                except ValueError:
                    print('Fecha no valida.Ingresar nueva fecha')
            fechaBusqueda=fecha.strftime("%d-%m-%Y")
            contador=len(diccCitas)
            for key,value in diccCitas.items():
                if(value['fechaCita'] == fechaBusqueda):
                    print("-"*25)
                    print(f"Cita # = {value['citaNumero']}")
                    print(f"Paciente = {value['nombrePaciente']}")
                    print(f"Fecha = {value['fechaCita']}")
                    print(f"Hora = {value['horaCita']}")
                    print(f"Motivo = {value['motivo']}")
                    print("-"*25)
                    j+=1
                elif(contador==i and j==0):
                    print("No se encontre cita con la fecha ingresado")
                i+=1
            pause=input("Pause, presiona ENTER para continuar")
            MainMenu()
        else:
            print("Opcion no valida...")
            pause=input("Pause, presiona ENTER para salir")
            MainMenu()
    elif(opcion==3):
        os.system('cls') and os.system('clear')
        print('+','-'*45,'+')
        print('|{:^15}{}{:^14}|'.format('','EDITAR CITA MEDICA',''))
        print('+','-'*45,'+')
        print('Buscar Cita por: ','1. Nombre paciente','2. Fecha cita',sep='\n')
        isValid = True
        while isValid:
            try:
                opcion = int(input("Ingresa la opcion de busqueda: "))
                False
            except ValueError:
                print("Ingresa un numero entero")
            else:
                isValid = False
            
        if(opcion == 1):
            i=1
            j=0
            nombreBusqueda = input("Ingresa nombre del paciente:").upper()
            contador=len(diccCitas)
            for key,value in diccCitas.items():
                if(value['nombrePaciente'] == nombreBusqueda):
                    print("-"*25)
                    print(f"Cita # = {value['citaNumero']}")
                    print(f"Paciente = {value['nombrePaciente']}")
                    print(f"Fecha = {value['fechaCita']}")
                    print(f"Hora = {value['horaCita']}")
                    print(f"Motivo = {value['motivo']}")
                    print("-"*25)
                    j+=1
                elif(contador==i and j==0):
                    print("No se encontre cita con el nombre ingresado")
                i+=1
            pause=input("Pause, presiona ENTER para continuar")
        elif(opcion == 2):
            i=1
            j=0
            while(True):
                fecha_str=input("Ingresa fecha en formato dd-mm-yyyy: ")
                try:
                    fecha = datetime.strptime(fecha_str,"%d-%m-%Y").date()
                    break
                except ValueError:
                    print('Fecha no valida.Ingresar nueva fecha')
            fechaBusqueda=fecha.strftime("%d-%m-%Y")
            contador=len(diccCitas)
            for key,value in diccCitas.items():
                if(value['fechaCita'] == fechaBusqueda):
                    print("-"*25)
                    print(f"Cita # = {value['citaNumero']}")
                    print(f"Paciente = {value['nombrePaciente']}")
                    print(f"Fecha = {value['fechaCita']}")
                    print(f"Hora = {value['horaCita']}")
                    print(f"Motivo = {value['motivo']}")
                    print("-"*25)
                    j+=1
                elif(contador==i and j==0):
                    print("No se encontre cita con la fecha ingresado")
                i+=1
            pause=input("Pause, presiona ENTER para continuar")
        else:
            print("Opcion no valida...")
            pause=input("Pause, presiona ENTER para salir")
            MainMenu()
        isAddEncontrado=True
        while(isAddEncontrado):
            j=0
            try:
                idCita = input("Ingresa el numero de cita: ").zfill(5)
                for i in idCita:
                    j+=1
                if (j==5):
                    isAddEncontrado=False
            except Exception as e:
                print("No se ingreso Cita # correctamente")
                isAddEncontrado=True
                pause=input("Pause, presiona ENTER para continuar")
        r=1
        for key,value in diccCitas.items():
            contador=len(diccCitas)
            if(value['citaNumero'] == idCita):
                numeroCita=value['citaNumero']
                nombrePaciente=input("Ingresa nombre de paciente o ENTER para continuar: ").upper() or value['nombrePaciente']
                while(True):
                    fecha_str=input("Ingresa fecha en formato dd-mm-yyyy o ENTER para continuar: ") or value['fechaCita']
                    try:
                        fecha = datetime.strptime(fecha_str,"%d-%m-%Y").date()
                        break
                    except ValueError:
                        print('Fecha no valida.Ingresar nueva fecha')
                fechaFinal=fecha.strftime("%d-%m-%Y")
                print('','NOTA:LAS CITAS SE ASIGNAN CADA MEDIA HORA','',sep='\n')
                while(True):
                    hora_str=input("Ingresa hora en formato de 24H HH:MM o ENTER para continuar: ") or value['horaCita']
                    try:
                        hora = datetime.strptime(hora_str,"%H:%M").time()
                        break
                    except ValueError:
                        print('Hora no valida.Ingresar nueva hora')
                horaFinal=hora.strftime("%H:%M")
                motivo=input("Ingresa el nuevo motivo cita o ENTER para continuar: ").upper() or value['motivo']
                break
            elif(contador==r):
                print("No se encontre cita.")
                pause=input("Pause, presiona ENTER para continuar")
                MainMenu()          
            r+=1  
        cita={
            'citaNumero':numeroCita,
            'nombrePaciente':nombrePaciente,
            'fechaCita':fechaFinal,
            'horaCita':horaFinal,
            'motivo':motivo
        }
        diccCitas.update({f"{numeroCita}":cita})
        core.editarData('citas.json',diccCitas)
    elif(opcion==4):
        os.system('cls') and os.system('clear')
        print('+','-'*45,'+')
        print('|{:^14}{}{:^13}|'.format('','ELIMINAR CITA MEDICA',''))
        print('+','-'*45,'+')
        i=1
        j=0
        nombreBusqueda = input("Ingresa nombre del paciente:").upper()
        contador=len(diccCitas)
        for key,value in diccCitas.items():
            if(value['nombrePaciente'] == nombreBusqueda):
                print("-"*25)
                print(f"Cita # = {value['citaNumero']}")
                print(f"Paciente = {value['nombrePaciente']}")
                print(f"Fecha = {value['fechaCita']}")
                print(f"Hora = {value['horaCita']}")
                print(f"Motivo = {value['motivo']}")
                print("-"*25)
                j+=1
            elif(contador==i and j==0):
                print("No se encontre cita con el nombre ingresado")
                pause=input("Pause, presiona ENTER para continuar")
                MainMenu()
            i+=1
        isAddEncontrado=True
        while(isAddEncontrado):
            j=0
            try:
                idCita = input("Ingresa el numero de cita: ").zfill(5)
                for i in idCita:
                    j+=1
                if (j==5):
                    isAddEncontrado=False
            except Exception as e:
                print("No se ingreso Cita # correctamente")
                isAddEncontrado=True
                pause=input("Pause, presiona ENTER para continuar")
        r=1
        for key,value in diccCitas.items():
            contador=len(diccCitas)
            if(value['citaNumero'] == idCita):
                diccCitas.pop(idCita)
                core.editarData('citas.json',diccCitas)
                MainMenu()
            elif(contador==r):
                print("No se encontre cita.")
                pause=input("Pause, presiona ENTER para continuar")
                MainMenu()          
            r+=1 
    elif(opcion==5):
        isMainMenu = False
    else:
        print('Opcion no valida.Ingresar nueva opcion')
        os.system('sleep 2')
        MainMenu()