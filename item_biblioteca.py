class ItemBiblioteca:
    def __init__(self, codigo: int, titulo: str, ano: int, disponivel: bool):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_ano(self):
        return self.__ano
    
    def is_disponivel(self):
        return self.__disponivel
    
    def set_titulo(self, titulo):
        if titulo.strip() != "":
            self.__titulo = titulo
            
    def set_ano(self, ano):
        if ano > 0:
            self.__ano = ano
    
    def exibir_detalhes(self):
        print(f"Código: {self.__codigo} - Título: {self.__titulo} - Ano: {self.__ano} Disponivel: {self.__disponivel}")
        
    def emprestar(self):
       if self.__disponivel:
           self.__disponivel = False
           print(f"O item {self.__titulo} foi emprestado com sucesso")
       else:
           print(f"O item {self.__titulo} já foi emprestado!")
           
    def devolver(self):
        self.__disponivel = True
        print(f"O item {self.__titulo} foi devolvido com sucesso ")
        
    
# # Criando um item da biblioteca
# item1 = ItemBiblioteca(1, "Dom Casmurro", 1899, True)

# # Exibindo detalhes iniciais
# item1.exibir_detalhes()

# # Testando getters
# print("Código:", item1.get_codigo())
# print("Título:", item1.get_titulo())
# print("Ano:", item1.get_ano())
# print("Disponível:", item1.is_disponivel())

# # Testando empréstimo
# item1.emprestar()

# # Tentando emprestar novamente
# item1.emprestar()

# # Verificando status
# item1.exibir_detalhes()

# # Testando devolução
# item1.devolver()

# # Verificando novamente
# item1.exibir_detalhes()

# # Testando setters
# item1.set_titulo("Dom Casmurro - Edição Especial")
# item1.set_ano(1900)

# item1.exibir_detalhes()