class Agendamento():
    def __init__(self, cliente, servico, data, hora, observacao=None):
        self.cliente = cliente #Objeto Cliente
        self.servico = servico #Objeto Servico
        self.data = data
        self.hora = hora
        self.observacao = observacao