"""menu.py

Autor:                   Vinícius Matté Gregory
Data de Criação:         26/06/2017
Última Modificação:      02/07/2017
Local:                   Brasília (Brasil)

Essa é a definição da classe Menu, minha classe principal para
gerenciar menus e suas ações em interfaces de linha de comando.
"""
_OPÇÃO_INVÁLIDA = "ESSA OPÇÃO É INVÁLIDA!"
_MSG_DE_ESPERA = "Pressione ENTER para continuar. . ."


class Menu:
    """Classe para gerenciar diferentes menus e suas respectivas ações."""

    def __init__(self, título):
        """Inicializa um menu com uma lista vazia de Opções.

        Args:
            :param título: título do menu
        """
        self.título = título
        self._opções = []

    def adicionar_opção(self, descrição, função):
        """Adiciona uma opção ao menu.

        Args:
            :param descrição: descrição da opção
            :param função: função a ser chamada pela opção
        """
        opção = _Opção(descrição, função)
        self._opções.append(opção)

    def exibir_menu(self):
        """Exibe o menu na linha de comando."""
        print(self.título.upper())
        print("-" * len(self.título))

        for i in range(len(self._opções)):
            print("   %2d : %s" % (i + 1, self._opções[i].descrição))

        try:
            opção = input(">>> ")
            self._opções[int(opção) - 1].executar()
        except (IndexError, ValueError):
            print(_OPÇÃO_INVÁLIDA)
            input(_MSG_DE_ESPERA)
            print()
            self.exibir_menu()


class _Opção:
    """Representa as opções presentes no menu de linha de comando."""

    def __init__(self, descrição, função):
        """Inicializa uma opção com uma descrição e uma função.

        Args:
            :param descrição: Breve descrição da opção.
            :param função: Função a ser executada pela opção.
        """
        self.descrição = descrição
        self._função = função

    def executar(self):
        """Executa a função correspondente à opção."""
        self._função()
