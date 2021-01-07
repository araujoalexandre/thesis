import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def plot_graph_benchmark_models(path):

  fig, ax = plt.subplots(1, 1)
  ax.scatter( 25, 0.831, c="red",    label="NetVLAD 32, Compact FC 256, MoE 2")
  ax.scatter( 50, 0.851, c="orange", label="NetVLAD 64, Compact FC 512, MoE 4")
  ax.scatter( 51, 0.848, c="brown",  label="NetFV 64, Compact FC 512, MoE 4")
  ax.scatter( 59, 0.861, c="green",  label="DBoF 8192, Compact FC 512, MoE 4")
  ax.scatter( 87, 0.858, c="lime",   label="NetVLAD 256, Compact FC 1024, MoE 4")
  ax.scatter(158, 0.861, c="olive",  label="NetVLAD 128, NetFV 64, Compact FC 1024, MoE 4")
  ax.scatter(159, 0.863, c="blue",   label="NetVLAD 256, NetFV 128, Compact FC 1024, MoE 4")
  ax.scatter(166, 0.861, c="cyan",   label="DBoF 8192,  NetVLAD 128, Compact FC 1024, MoE 4")
  ax.scatter(176, 0.861, c="teal",   label="DBoF 16384, NetVLAD 256, Compact FC 1024, MoE 4")
  ax.set_xlim([0, 200])
  ax.set_ylim([0.81, 0.88])
  plt.legend(title=r"Models", loc='lower right', fontsize='x-small')
  plt.ylabel("Validation GAP")
  plt.xlabel("Number of weights (Millions)")
  plt.tight_layout()
  plt.savefig("{}/graph_benchmark_models.pdf".format(path))


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
    plot_graph_benchmark_models(path)


if __name__ == '__main__':
  main()

