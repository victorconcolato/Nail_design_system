class Clientes:
    def __init__(self, nome, endereço, whatsapp, alergia, tipo_de_unha, observacoes=None):
        self.nome = nome
        self.endereço = endereço
        self.whatsapp = whatsapp
        self.alergia = alergia
        self.tipo_de_unha = tipo_de_unha
        self.observacoes = observacoes
    
cliente_01 = Clientes("Maria", "Rua das Flores, 123", "11999999999", "Não", "Acrílica")

print(cliente_01.__dict__)