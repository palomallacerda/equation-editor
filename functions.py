import matplotlib.pyplot as plt

def display_equation(user_input):
    plt.axes([0.01, 0.01, 0.01, 0.01], frameon=False)
    plt.title('${}$'.format(user_input), fontsize=30)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('generated-eq.png', bbox_inches='tight', transparent=True)
    return 'generated-eq.png'
