import glob
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def sort_fn(x):
  x = x.split('_')[5]
  cout, cin, ksize, _ = x.split('x')
  return (ksize, cin)

def plot_convergence_bounds(path):

  csv_files = glob.glob('ch5-graph_convergence_bounds_data/convergence_bound*.csv')
  csv_files = sorted(csv_files, key=sort_fn)
  label_list = []
  dim_list = []
  sv_max_list = []
  for filename in csv_files:
    label_list.append(filename.split('_')[5])
    df = pd.read_csv(filename, sep=';')
    dim = df['dim'].values
    sv_max = df['sv_max'].values
    dim_list.append(dim)
    sv_max_list.append(sv_max)

  f, ax = plt.subplots(1, 1)
  for label, dim, sv_max in zip(label_list, dim_list, sv_max_list):
    ax.plot(dim, sv_max, label=label[2:])
  plt.ylim(0, 7)
  plt.legend()
  plt.ylabel('$\Gamma(n)$')
  plt.xlabel('Image Size')
  plt.tight_layout()
  plt.savefig('{}/convergence_bounds.pdf'.format(path))


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

    path = '../main/ch5-lipschitz_regularization/'

    plot_convergence_bounds(path)


if __name__ == '__main__':
  main()



