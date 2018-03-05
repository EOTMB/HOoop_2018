from random import randint

class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""
    def __init__(self):
        super(FilaPreferencial,self).__init__()
        self.maxenfila = 15
    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        if cliente.categoria == 'pref':
            self.enfila += 1
            self.fila.append(cliente)
        else:
            print "No se pudo agregar el cliente a la fila ya que es solo para clientes preferenciales"
    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila -= 1
        self.fila.pop(0)

    def abrircajanueva(self,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if self.enfila > self.maxenfila:
			filanueva = FilaPreferencial()
			filanueva.enfila = self.enfila/2
			filanueva.fila = self.fila[:filanueva.enfila]
			self.fila[filanueva.enfila:]

        else:
			print "La fila no tiene la longitud necesaria para abrir otra caja"

class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila += 1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente no prederencial"""
        self.enfila -= 1
        self.fila.pop(0)



class cliente(object):
     """clase cliente """
     def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None

     def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria = categoria


if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    sinAtender=[]
    filaGeneral=FilaGeneral()
    filaPreferencial1=FilaPreferencial()
    filaPreferencial2=FilaPreferencial()
    filaPreferencial3=FilaPreferencial()
    i=0
    j=0
    for i in xrange(100):
        dni = randint(0,40000000)
        cli = cliente(dni)
        if i > 60:
            cli.modificarcategoria('pref')
        sinAtender.append(cli)

    for client in sinAtender:
        largoFila1 = filaPreferencial1.enfila
        largoFila2 = filaPreferencial2.enfila
        largoFila3 = filaPreferencial3.enfila
        if largoFila1  == 0 and largoFila2 == 0 and largoFila3 == 0:
            filaPreferencial1.insertar(client)
        elif largoFila2 < largoFila1 and largoFila2 < largoFila3:
            filaPreferencial2.insertar(client)
        elif largoFila3 < largoFila1:
            filaPreferencial3.insertar(client)
        else:
            filaPreferencial1.insertar(client)

        if client.categoria != 'pref':
            filaGeneral.insertar(client)
            print 'El cliente DNI' + string(client.dni) + 'se agrego a la fila general'
        else:
            print 'El cliente DNI' + string(client.dni) + 'se agrego a la fila preferencial'
        filasPreferenciales=[filaPreferencial1,filaPreferencial2,filaPreferencial3]

        for i in range(filasPreferenciales):
            fila = filasPreferenciales[i]
            filanueva = filasPreferenciales[i+1]
            largoFila = fila.enfila
            largofilanueva = filanueva.enfila
            longitudmaxima = fila.maxenfila
            if largoFila >= longitudmaxima:
                fila.abrircajanueva(filanueva)
                print 'Se abrio una nueva caja para clientes preferenciales'

        if j == 2:
            for fila in filasPreferenciales:
                posicionCliente = fila.fila[0]
                clienteAtendido = string(posicionCliente.dni)
                print 'Se atendio el cliente'+ clienteAtendido + 'en la fila preferencial'
                fila.atender()
            j = 0
        if i == 3:
            posicionClienteGeneral = filaGeneral.fila[0]
            clienteGeneralAtendido = string(posicionClienteGeneral.dni)
            print 'Se atendio el cliente'+ clienteGeneralAtendido + 'en la fila preferencial'
            filaGeneral.atender()

        i += 1
        j += 1
