import numpy as np
import matplotlib
from matplotlib import pyplot as plt

import matplotlib.font_manager


data = [
  dict(title="LDR-SD (r=1)",         mark="^", color="blue",  coordinates=(140, 0.7017)),
  dict(title="LDR-SD (r=10)",        mark="^", color="red",   coordinates=(420, 0.7286)),
  dict(title="Toeplitz-like (r=1)",  mark="D",  color="blue",  coordinates=(110, 0.7111)),
  dict(title="Toeplitz-like (r=10)", mark="D",  color="red",   coordinates=(388, 0.7205)),
  dict(title="1 DC",                 mark="s",   color="green", coordinates=(124, 0.757)),
  dict(title="3 DC",                 mark="s",   color="blue",  coordinates=(217, 0.7856)),
  # dict(title="Scattering Avg pooling + 3 DC",     mark="s",   color="red",   coordinates=(66, 0.7535)),
  # dict(title="Scattering by channel + 4 DC",      mark="s",   color="brown", coordinates=(191, 0.764)),
]

def plot_graph_scatterplot(path):

  fig, ax = plt.subplots(1, 1)
  for point in data:
    title = point['title']
    color = point['color']
    marker = point['mark']
    x, y = point['coordinates']
    ax.scatter(x, y, c=color, label=title, marker=marker)

  plt.legend(title=r"Scattering Networks \\ with Structured Layers")
  plt.ylabel("Test Accuracy")
  plt.xlabel("Number of Weights (x1000)")
  plt.tight_layout()
  plt.savefig("{}/scatterplot.pdf".format(path))


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
    plot_graph_scatterplot(path)


if __name__ == '__main__':
  main()

