import matplotlib
import matplotlib.pyplot as plt


def Ajuda():
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # Set titles for the figure and the subplot respectively
    ax.set_title('Informações')

    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')

    # Set both x- and y-axis limits to [0, 10] instead of default [0, 1]
    ax.axis([0, 10, 0, 10])

    #Retira a legenda dos eixos x e y
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)


    #coloca o texto dentro da caixa
    ax.text(0.25, 9, 'Editor de formatação de formulas matematicas', fontsize=9)
    ax.text(0.25, 9.5, 'Feito por Paloma, Rodrigo, Antero e Yanka(Pray)', fontsize=9)


    plt.show()
