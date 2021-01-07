
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt


def plot_graph_compactness_layers(path):

  df1 = pd.read_csv('ap2-graph_comparison_learned_diagonal_data/learned_diag.dat', sep='\t')
  df2 = pd.read_csv('ap2-graph_comparison_learned_diagonal_data/fixed_diag.dat', sep='\t')

  fig, ax = plt.subplots(1, 1)
  ax.plot(df1['epoch'].values, df1['gap'].values, label='Model with learned diagonals') 
  ax.plot(df2['epoch'].values, df2['gap'].values, label='Model with fixed diagonals') 
  ax.set_xlim([0, 10])
  ax.set_ylim([0.79, 0.89])
  plt.legend(title=r"Models", loc='upper left')
  plt.ylabel("Validation GAP")
  plt.xlabel("Epochs")
  plt.tight_layout()
  plt.savefig("{}/graph_comparison_learned_diagonal.pdf".format(path))


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

    path = '../appendix/ap2-training_video_classification/'
    plot_graph_compactness_layers(path)


if __name__ == '__main__':
  main()

