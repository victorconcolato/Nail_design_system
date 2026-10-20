class Atendimento():

    def __init__(self, cliente, servico, data, hora, forma_pgto, cor=None, marca=None, materiais=None, foto=None, observacao=None):
        self.cliente = cliente #Objeto Cliente
        self.servico = servico #Objeto Servico
        self.data = data
        self.hora = hora
        self.forma_pgto = forma_pgto
        self.cor = cor
        self.marca = marca
        self.materiais = materiais or list()
        self.foto = foto
        self.observacao = observacao