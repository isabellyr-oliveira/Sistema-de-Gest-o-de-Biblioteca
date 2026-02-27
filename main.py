class ItemBiblioteca:
    def __init__(self, codigo: int, titulo: str, ano: int, disponivel: bool):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Código: {self.__codigo} - Título: {self.__titulo} - Ano: {self.__ano} Disponivel: {self.__disponivel}")
        
        
detalhes = ItemBiblioteca(1, "pequeno principe", 1943, "sim")
detalhes.exibir_detalhes()