import os
import citas

if __name__ == '__main__':
    os.system('cls') and os.system('clear')
    isAddPrincipal=True
    while isAddPrincipal:
        os.system('cls') and os.system('clear')
        print('+','-'*45,'+')
        print('|{:^17}{}{:^16}|'.format('','MENU PRINCIPAL',''))
        print('+','-'*45,'+')
        print('1.Gestion Citas medicas','2.Terminar',sep='\n')
        isValid = True
        while isValid:
            try:
                opcion = int(input("Ingresa la opcion de busqueda: "))
                False
            except ValueError:
                print("Ingresa un numero entero")
            else:
                isValid = False
        if opcion==1:
            citas.loadInfoCitas()
            citas.MainMenu()
        elif opcion==2:
            isAddPrincipal=False
        else:
            print('Opcion no valida,ingresa nueva opcion')
            os.system('sleep 1')