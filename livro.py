from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, disponivel, autor, num_paginas):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        print(f"[LIVRO] Código: {self.get_codigo()} | "
              f"Título: {self.get_titulo()} | "
              f"Autor: {self.__autor} | "
              f"Páginas: {self.__num_paginas} | "
              f"Ano: {self.get_ano()} | "
              f"Disponível: {self.is_disponivel()}")
        
        
# if __name__ == "__main__":
#     livro = Livro(10, "meu livro", "Isabelly Rafaella", 100, 2026, "sim" )

#     livro.exibir_detalhes()
#     livro.emprestar()
#     livro.exibir_detalhes()