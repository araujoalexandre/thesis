
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt


def plot_graph_compactness_layers(path):

  df1 = pd.read_csv('ap2-graph_compactness_layers_data/dense.dat', sep='\t')
  df2 = pd.read_csv('ap2-graph_compactness_layers_data/compact_fc.dat', sep='\t')
  df3 = pd.read_csv('ap2-graph_compactness_layers_data/compact_dbof.dat', sep='\t')
  df4 = pd.read_csv('ap2-graph_compactness_layers_data/compact_moe.dat', sep='\t')

  fig, ax = plt.subplots(1, 1)
  ax.plot(df1['epoch'].values, df1['gap'].values, label='Dense') 
  ax.plot(df2['epoch'].values, df2['gap'].values, label='With compact FC') 
  ax.plot(df3['epoch'].values, df3['gap'].values, label='With compact DBoF') 
  ax.plot(df4['epoch'].values, df4['gap'].values, label='With compact MoE') 
  ax.set_xlim([0, 7])
  ax.set_ylim([0.77, 0.875])
  plt.legend(title=r"Models", ncol=2, loc='upper left')
  plt.ylabel("Validation GAP")
  plt.xlabel("Epochs")
  plt.tight_layout()
  plt.savefig("{}/graph_compact_layers.pdf".format(path))


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

