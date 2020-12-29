import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc


def plot_graph_attack_iter(path):

  df = pd.read_csv('ch5-plot_attacks_iter_data.csv', sep=';')
  iter_values = df['iter'].values

  # plot 1
  fig, ax = plt.subplots(1, 1)
  ax.plot(iter_values, df['AT-PGD'], marker='^', label='AT PGD-$\ell_\infty$')
  ax.plot(iter_values, df['PM10-PGD'], marker='s', label='AT+PM PGD-$\ell_\infty$')
  ax.plot(iter_values, df['LipReg-PGD'], marker='o', label='AT+LipReg PGD-$\ell_\infty$')

  ax.set_ylabel('Accuracy Under Attack')
  ax.set_xlabel('Number of Iterations')
  ax.set_ylim(0.40, 0.48)
  plt.legend()
  plt.tight_layout()
  plt.savefig('{}/attacks_iter_pgd.pdf'.format(path))


  # plot 2
  fig, ax = plt.subplots(1, 1)
  ax.plot(iter_values, df['AT-CW 0.8'], marker='^', label='AT C\&W-$\ell_2$ 0.8')
  ax.plot(iter_values, df['PM10-CW 0.8'], marker='s', label='AT+PM C\&W-$\ell_2$ 0.8')
  ax.plot(iter_values, df['LipReg-CW 0.8'], marker='o', label='AT+LipReg C\&W-$\ell_2$ 0.8')

  ax.set_ylabel('Accuracy Under Attack')
  ax.set_xlabel('Number of Iterations')
  ax.set_ylim(0.32, 0.57)
  plt.legend()
  plt.tight_layout()
  plt.savefig('{}/attacks_iter_cw.pdf'.format(path))


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
    matplotlib.rc('figure', figsize=(7, 5)) 
    matplotlib.rc('savefig', dpi=600)
    matplotlib.rc('savefig', format='pdf')

    path = '../main/ch5-lipschitz_regularization'
    plot_graph_attack_iter(path)


if __name__ == '__main__':
  main()


