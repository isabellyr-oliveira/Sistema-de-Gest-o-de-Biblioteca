from item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, disponivel, edicao, mes):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__edicao = edicao
        self.__mes = mes

    def exibir_detalhes(self):
        print(f"[REVISTA] Código: {self.get_codigo()} | "
              f"Título: {self.get_titulo()} | "
              f"Edição: {self.__edicao} | "
              f"Mês: {self.__mes} | "
              f"Ano: {self.get_ano()} | "
              f"Disponível: {self.is_disponivel()}")
        
# if __name__ == "__main__":
#     revista = Revista(20, "Tech News", "45", "Março", 2024, "sim")

#     revista.exibir_detalhes()
#     revista.emprestar()
#     revista.exibir_detalhes()