
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt


def plot_graph_robust_dbof(path):

  df1 = pd.read_csv('ap2-graph_robust_dbof_data/dbof_robust.dat', sep='\t')
  df2 = pd.read_csv('ap2-graph_robust_dbof_data/dbof_max_pooling.dat', sep='\t')
  df3 = pd.read_csv('ap2-graph_robust_dbof_data/dbof_avg_pooling.dat', sep='\t')

  fig, ax = plt.subplots(1, 1)
  ax.plot(df1['epoch'].values, df1['gap'].values, label='Robust DBoF') 
  ax.plot(df2['epoch'].values, df2['gap'].values, label='DBoF w/max pooling') 
  ax.plot(df3['epoch'].values, df3['gap'].values, label='DBoF w/average pooling') 
  ax.set_ylim([0.76, 0.88])
  plt.legend(title=r"Type of Pooling")
  plt.ylabel("Validation GAP")
  plt.xlabel("Epochs")
  plt.tight_layout()
  plt.savefig("{}/graph_robust_dbof.pdf".format(path))


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
    plot_graph_robust_dbof(path)


if __name__ == '__main__':
  main()

