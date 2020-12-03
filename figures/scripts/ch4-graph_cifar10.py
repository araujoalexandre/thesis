import numpy as np
import matplotlib
from matplotlib import pyplot as plt


################################################################################
# cifar10 factor
################################################################################

factor_1 = [
  # layers, weights, accuracy
  ( 2,  21524, 0.5263),
  ( 6,  58388, 0.5138),
  (10,  95252, 0.5224),
  (20, 187412, 0.2911),
  (30, 279572, 0.1000),
  (40, 371732, 0.1000),
]

factor_2 = [
  # layers, weights, accuracy
  ( 6,  49172, 0.5281),
  (10,  95252, 0.5388),
  (20, 187412, 0.5264),
  (30, 279572, 0.4758),
  (40, 371732, 0.1000),
]

factor_3 = [
  # layers, weights, accuracy
  ( 3,  30740, 0.5362),
  ( 9,  86036, 0.5409),
  (15, 141332, 0.5448),
  (21, 196628, 0.5465),
  (30, 279572, 0.5522),
  (39, 362516, 0.5328),
]

################################################################################
# cifar10 type
################################################################################

dense = [
  # weights, accuracy
  (  0, 0.562),
  (372, 0.562)
]

circulant = [
  # weights, accuracy
  ( 21, 0.536),
  ( 49, 0.543),
  ( 95, 0.544),
  (187, 0.560),
  (279, 0.561),
  (371, 0.559)
]

diag_toeplitz = [
  # weights, accuracy
  ( 18, 0.4794),
  ( 43, 0.5111),
  ( 67, 0.5156),
  (129, 0.5253),
  (190, 0.5309),
  (251, 0.5380),
  (288, 0.5399),
  (374, 0.5391)
]

toeplitz = [
  # weights, accuracy
  ( 24, 0.4626),
  ( 52, 0.4729),
  ( 98, 0.5035),
  (190, 0.4959),
  (282, 0.5028),
  (374, 0.4969)
]

low_rank = [
  # layers, weights, accuracy
  ( 21, 0.286),
  ( 49, 0.393),
  ( 95, 0.475),
  (187, 0.509),
  (279, 0.522),
  (372, 0.523)
]


################################################################################
# cifar10 leaky_relu
################################################################################

slope = {
  '0.2': [
    # layers, weights, accuracy
    ( 2,  21524, 0.5245),
    ( 6,  58388, 0.5243),
    (10,  95252, 0.5190),
    (20, 187412, 0.1000),
    (30, 279572, 0.1000),
    (40, 371732, 0.1000)
  ],
  '0.3': [
    # layers, weights, accuracy
    ( 2,  21524, 0.5256),
    ( 5,  49172, 0.5341),
    (10,  95252, 0.5349),
    (20, 187412, 0.5303),
    (30, 279572, 0.3090),
    (40, 371732, 0.1000)
  ],
  '0.5': [
    # layers, weights, accuracy
    ( 2,  21524, 0.5360),
    ( 5,  49172, 0.5430),
    (10,  95252, 0.5443),
    (20, 187412, 0.5599),
    (30, 279572, 0.5609),
    (40, 371732, 0.5586)
  ]
}



def plot_graph_cifar_factor(path):
  data1 = np.array(factor_1)
  data2 = np.array(factor_2)
  data3 = np.array(factor_3)
  fig, ax = plt.subplots(1, 1)
  ax.plot(data1[:, 0], data1[:, 2], label=r"$k=1$", marker='D') 
  ax.plot(data2[:, 0], data2[:, 2], label=r"$k=2$", marker='o') 
  ax.plot(data3[:, 0], data3[:, 2], label=r"$k=3$", marker='s') 
  plt.legend(title=r"Number of factors")
  plt.ylabel(r"Test Accuracy")
  plt.xlabel(r"Number of Layers")
  plt.tight_layout()
  plt.savefig("{}/cifar10_factor.pdf".format(path))

def plot_graph_cifar_type(path):
  data0 = np.array(dense)
  data1 = np.array(circulant)
  data2 = np.array(toeplitz)
  data3 = np.array(diag_toeplitz)
  data4 = np.array(low_rank)
  fig, ax = plt.subplots(1, 1)
  ax.plot(data0[:, 0], data0[:, 1], '--', label=r"Dense (9M weights)")
  ax.plot(data1[:, 0], data1[:, 1], label=r"Diagonal-Circulant", marker='s') 
  ax.plot(data2[:, 0], data2[:, 1], label=r"Diagonal-Toeplitz", marker='^') 
  ax.plot(data3[:, 0], data3[:, 1], label=r"Toeplitz", marker='D') 
  ax.plot(data4[:, 0], data4[:, 1], label=r"Low Rank", marker='o') 
  plt.legend(title=r"Type of Networks")
  plt.ylabel(r"Test Accuracy")
  plt.xlabel(r"Number of Weights (x1000)")
  plt.tight_layout()
  plt.savefig("{}/cifar10_type.pdf".format(path))


def plot_graph_cifar_leaky_relu(path):
  data1 = np.array(slope['0.2'])
  data2 = np.array(slope['0.3'])
  data3 = np.array(slope['0.5'])
  fig, ax = plt.subplots(1, 1)
  ax.plot(data1[:, 0], data1[:, 2], label=r"$\alpha = 0.2$", marker='s') 
  ax.plot(data2[:, 0], data2[:, 2], label=r"$\alpha = 0.3$", marker='^') 
  ax.plot(data3[:, 0], data3[:, 2], label=r"$\alpha = 0.5$", marker='D') 
  plt.legend(title=r"Slope of Leaky-ReLU")
  plt.ylabel("Test Accuracy")
  plt.xlabel("Number of Layers")
  plt.tight_layout()
  plt.savefig("{}/cifar10_leaky_relu.pdf".format(path))



def main():

  with plt.style.context('seaborn-darkgrid'):

    font = {
      'family': 'serif',
      'serif': ['Computer Modern Roman'],
      'size': 14
    }
    matplotlib.rc('text', usetex=True)
    matplotlib.rc('font', **font)
    matplotlib.rc('lines', linewidth=2)
    matplotlib.rc('legend', frameon=True)
    matplotlib.rc('legend', fancybox=True)
    # matplotlib.rc('legend', fontsize='larger')
    matplotlib.rc('figure', figsize=(7, 5)) 
    matplotlib.rc('savefig', dpi=600)
    matplotlib.rc('savefig', format='pdf')

    path = '../main/ch4-diagonal_circulant/'

    plot_graph_cifar_factor(path)
    plot_graph_cifar_type(path)
    plot_graph_cifar_leaky_relu(path)

if __name__ == '__main__':
  main()




