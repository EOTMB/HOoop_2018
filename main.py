from banco import *
from random import randint
from time import sleep

if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    maxenfila = 30
    filaGeneral = FilaGeneral()
    filasPreferenciales=[FilaPreferencial()]
    i = 0
    j= 0

    while i < 1000:
        createCli = randint(0,99)

        if createCli > 49:
            dni = randint(0,40000000)
            cli = cliente(dni)
            cliCateg = randint(0,2)
            if cliCateg == 2:
                cli.modificarcategoria('preferencial')
                print "El cliente preferencial",cli.dni," acaba de ingresar al banco"
            else:
                print "El cliente ",cli.dni," acaba de ingresar al banco"


            if cli.categoria == "preferencial":
                filaPref = filasPreferenciales[0]
                filaMasCortaBuff = [0,filaPref.enfila]

                cantidadFilasPref = len(filasPreferenciales)
                for i in range(cantidadFilasPref):
                    filaPref=filasPreferenciales[i]
                    longitud = filaPref.enfila
                    if longitud < filaMasCortaBuff[1]:
                        filaMasCortaBuff = [i,longitud]

                filaMasCortaIndex = filaMasCortaBuff[0]
                filaMasCorta = filasPreferenciales[filaMasCortaIndex]
                filaMasCorta.insertar(cli)
                print "El cliente preferencial ",cli.dni," acaba de ingresar a la fila preferencial", filaMasCortaIndex,". Tiene",filaMasCorta.enfila," personas adelante"

                if filaMasCorta.enfila >= maxenfila:
                    filaSiguiente = FilaPreferencial()
                    filasPreferenciales.append(filaSiguiente)

                    filaMasCorta.abrircajanueva(maxenfila,filaSiguiente)
                    print "La fila  ha superado el largo maximo, se ha abierto una nueva caja"
            else:
                filaGeneral.insertar(cli)
                print "El cliente", cli.dni," ingreso a la fila general. Tiene ", filaGeneral.enfila," personas adelante"
        if j >=4:
            if filaGeneral.enfila > 0:
                cliAtendido = filaGeneral.fila[0]
                print "El cliente", cliAtendido.dni," fue atendido"
                filaGeneral.atender()

            for filaPreferencial in filasPreferenciales:
                if filaPreferencial.enfila > 0:
                    cliPrefAtendido = filaPreferencial.fila[0]
                    print "El cliente",cliPrefAtendido.categoria," ",cliPrefAtendido.dni," fue atendido"
                    filaPreferencial.atender()
                j=0
        else:
            j+=1

        i += 1
        sleep(1)
