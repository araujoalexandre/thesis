
import pickle
import glob
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def pickle_load(path):
  with open(path, 'rb') as f:
    return pickle.load(f, encoding='latin1')

def plot_graph_jacobian(path):

  data_path = 'ch5-graph_jacobian_distribution_data'

  # this test data
  filename_baseline = '{}/2020-05-02_21.05.41_7393.pkl'.format(data_path)
  filname_lipreg = '{}/2020-05-05_18.03.07_9841.pkl'.format(data_path)
  filename_at = '{}/2020-05-07_11.37.50_3891.pkl'.format(data_path)
  filename_at_lipreg = '{}/2020-05-06_21.31.17_8103.pkl'.format(data_path)

  values_baseline = pickle_load(filename_baseline)
  values_lipreg = pickle_load(filname_lipreg)
  values_at = pickle_load(filename_at)
  values_at_lipreg = pickle_load(filename_at_lipreg)

  n_bins = 100

  # plot 1
  fig, ax = plt.subplots(1, 1)
  sns.distplot(values_baseline, label='Baseline', bins=n_bins)
  sns.distplot(values_lipreg, label='LipReg', bins=n_bins)
  ax.set_xlim(0, 200)
  plt.xlabel('Distribution of the Jacobian Norm on CIFAR10 testset')
  plt.legend()
  plt.tight_layout()
  plt.savefig('{}/jacobian_distribution_v1.pdf'.format(path))

  # plot 2
  fig, ax = plt.subplots(1, 1)
  sns.distplot(values_at, label='AT', bins=n_bins)
  sns.distplot(values_at_lipreg, label='AT+LipReg', bins=n_bins)
  ax.set_xlim(0, 15)
  plt.xlabel('Distribution of the Jacobian Norm on CIFAR10 testset')
  plt.legend()
  plt.tight_layout()
  plt.savefig('{}/jacobian_distribution_v2.pdf'.format(path))


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
    plot_graph_jacobian(path)

if __name__ == '__main__':
  main()





