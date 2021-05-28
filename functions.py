import matplotlib.pyplot as plt

def display_equation(user_input):
    plt.axes([0.01, 0.01, 0.01, 0.01], frameon=False)
    plt.title('${}$'.format(user_input), fontsize=18)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('generated-eq.png', bbox_inches='tight', transparent=False)
    return 'generated-eq.png'
