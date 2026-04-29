class ArrayList:
    def __init__(self):
        self.array = [None] * 10
        self.size = 0

    def add(self, value):
        self.array[self.size] = value
        self.size += 1

    def get(self, index):
        return self.array[index]

    def show(self):
        if self.size == 0:
            print("Nenhum item.")
        else:
            for i in range(self.size):
                print(f"- {self.array[i]}")

    def contains(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return True
        return False


def adicionar_pista(pistas, pista):
    if not pistas.contains(pista):
        pistas.add(pista)
        print(f"\n[PISTA] {pista}")
    else:
        print("\nVocê já coletou essa pista.")


def jogo():
    pistas = ArrayList()
    historico = ArrayList()

    print("-- CASO BLACKWOOD --")
    print("Você é um detetive chamado para investigar")
    print("o assassinato do empresário Sr. Blackwood.")
    print("O crime aconteceu dentro da mansão durante a noite.")
    print("Não há sinais de arrombamento...")
    print("O assassino provavelmente estava dentro da casa.\n")

    print("Suspeitos:")
    print("Amora - esposa da vítima")
    print("Sansão - motorista da família")
    print("Mabel - sócia da vítima\n")

    while True:
        print("\nO que deseja fazer?")
        print("1 - Investigar sala")
        print("2 - Investigar quarto")
        print("3 - Investigar jardim")
        print("4 - Interrogar Amora")
        print("5 - Interrogar Sansão")
        print("6 - Interrogar Mabel")
        print("7 - Ver pistas")
        print("8 - Ver histórico")
        print("9 - Acusar")
        print("10 - Sair")

        op = input("Escolha: ")

        if op == "1":
            print("\nVocê observa a sala do crime.")
            print("Há uma taça quebrada no chão e nenhum sinal de arrombamento.")
            adicionar_pista(pistas, "Sem sinais de arrombamento")
            adicionar_pista(pistas, "Taça quebrada no chão")
            historico.add("Investigou a sala")

        elif op == "2":
            print("\nVocê entra no quarto do Sr. Blackwood.")
            print("O quarto está organizado demais, mas uma gaveta está aberta.")
            adicionar_pista(pistas, "Alguém mexeu na gaveta")
            historico.add("Investigou o quarto")

        elif op == "3":
            print("\nVocê vai até o jardim da mansão.")
            print("Na terra molhada, existem pegadas recentes.")
            adicionar_pista(pistas, "Pegadas recentes no jardim")
            historico.add("Investigou o jardim")

        elif op == "4":
            print("\nAmora responde às perguntas com poucas palavras.")
            print("Ela afirma que estava dormindo no momento do crime.")
            adicionar_pista(pistas, "Amora estava fria durante o interrogatório")
            historico.add("Interrogou Amora")

        elif op == "5":
            print("\nSansão evita contato visual durante a conversa.")
            print("Ele diz que estava na garagem.")
            adicionar_pista(pistas, "Sansão estava nervoso")
            historico.add("Interrogou Sansão")

        elif op == "6":
            print("\nMabel responde com tranquilidade incomum.")
            print("Ela afirma que saiu cedo, mas os horários não coincidem.")
            adicionar_pista(pistas, "Mabel deu um álibi inconsistente")
            historico.add("Interrogou Mabel")

        elif op == "7":
            print("\nPistas coletadas:")
            pistas.show()

        elif op == "8":
            print("\nHistórico de ações:")
            historico.show()

        elif op == "9":
            if pistas.size < 3:
                print("\nVocê precisa de mais pistas antes de acusar alguém!")
                continue

            print("\nQuem você acusa?")
            print("1 - Amora")
            print("2 - Sansão")
            print("3 - Mabel")

            escolha = input("Escolha: ")

            if escolha == "3":
                print("\nVocê conectou as pistas corretamente...")
                print("Mabel mentiu sobre seu álibi.")
                print("O motivo era interesse financeiro.")
                print("\nCASO RESOLVIDO.")
            else:
                print("\nVocê acusou a pessoa errada...")
                print("O verdadeiro culpado escapou.")
                print("\nCASO NÃO RESOLVIDO.")

            break

        elif op == "10":
            print("\nVocê saiu da investigação.")
            break

        else:
            print("\nOpção inválida.")


jogo()