import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=630, height=630)
screen.title("Jogo dos Estados")
imagem = "brasil.gif"
screen.addshape(imagem)
turtle.shape(imagem)

# Abre arquivo com estados e suas coordenadas
dados = pd.read_csv("27_estados.csv")
# Cria lista apenas com os estados
lista_estados = dados.estado.to_list()
# Lista com os estados que o usuário acerta
acertos = []

# While para manter o jogo aberto equanto não acertar os 27 estados
while len(acertos) < 27:
    resposta = screen.textinput(title=f"{len(acertos)} de 27 estados!", prompt="Qual o estado do Brasil?").title()

    # Digitar Sair para sair do jogo
    if resposta == "Sair":
        break
    # Se o usuário acerta, o nome do estado é adicionada na lista de acertos
    if resposta in lista_estados:
        # Se repetir algum estado não adiciona na lista
        if resposta not in acertos:
            acertos.append(resposta)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pencolor("darkgreen")
        # Escreve o nome do estado no mapa
        t.goto(int(dados[dados.estado == resposta].x.item()), int(dados[dados.estado == resposta].y.item()))
        t.write(resposta, font=("Arial", 8, "bold"))

# Estados esquecidos: cria uma lista com os estados não citados no jogo e salva em um .csv
esquecidos = [estado for estado in lista_estados if estado not in acertos]

novos_dados = pd.DataFrame(esquecidos)
novos_dados.to_csv("estados_para_lembrar.csv")


# # Código para descobrir as coordenadas de cada estado.
# def get_coor_estados(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_coor_estados)

# turtle.mainloop()