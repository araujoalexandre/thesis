import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

def plot_graph_acdc(path):
  df = pd.read_csv('acdc_cifar10.csv', sep=";")
  fig, ax = plt.subplots(1, 1)
  ax.plot(df['epochs'].values, df['acdc_2_layers'].values,  label=r"Cosine Transform -- 2 layers")
  ax.plot(df['epochs'].values, df['acdc_5_layers'].values,  label=r"Cosine Transform -- 5 layers")
  # ax.plot(df['epochs'].values, df['acdc_10_layers'].values, label=r"Cosine Transform -- 10 layers")
  ax.plot(df['epochs'].values, df['circ_2_layers'].values,  label=r"Fourier Transform -- 2 layers")
  ax.set_ylim([0.1, 0.6])
  plt.legend(title=r"Type of Network")
  plt.ylabel(r"Loss")
  plt.xlabel(r"Number of Epochs")
  plt.tight_layout()
  plt.savefig("{}/acdc_cifar10.pdf".format(path))


def plot_graph_acdc_regression(path):
  df = pd.read_csv('acdc_regression.csv', sep=';')
  fig, ax = plt.subplots(1, 1)
  ax.plot(df['steps'].values, df['acdc_2_layers'].values, label=r"Cosine Transform -- 2 layers")
  ax.plot(df['steps'].values, df['acdc_4_layers'].values, label=r"Cosine Transform -- 4 layers")
  ax.plot(df['steps'].values, df['circ_2_layers'].values, label=r"Fourier Transform -- 2 layers")
  ax.set_ylim([1, 4])
  plt.legend(title=r"Type of Network")
  plt.ylabel(r"Loss")
  plt.xlabel(r"Number of Steps")
  plt.tight_layout()
  plt.savefig("{}/acdc_regression.pdf".format(path))


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

    path = '../main/ch4-diagonal_circulant/'

    plot_graph_acdc(path)
    plot_graph_acdc_regression(path)

if __name__ == '__main__':
  main()

