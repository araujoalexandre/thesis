
import copy
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x, alpha):
    return np.maximum(alpha * x, x)

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def plot_figures(x, data, locator, lim_and_ticks, function):

  data = data[function]
  locator = locator[function]
  lim_and_ticks = lim_and_ticks[function]

  fig, ax = plt.subplots(1, 1, figsize=(5, 5))
  ax.spines['new_left'] = copy.copy(ax.spines['left'])
  ax.spines['new_bottom'] = copy.copy(ax.spines['bottom'])
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position(('data', 0))

  ax.xaxis.set_major_locator(
    MultipleLocator(locator['major']['xaxis']))
  ax.yaxis.set_major_locator(
    MultipleLocator(locator['major']['yaxis']))

  ax.xaxis.set_minor_locator(
    MultipleLocator(locator['minor']['xaxis']))
  ax.yaxis.set_minor_locator(
    MultipleLocator(locator['minor']['yaxis']))

  ax.set_xlim(lim_and_ticks['xlim'])
  ax.set_ylim(lim_and_ticks['ylim'])
  ax.set_xticks(lim_and_ticks['xticks'])
  ax.set_yticks(lim_and_ticks['yticks'])
  if lim_and_ticks['yticklabels'] is not None:
    ax.set_yticklabels(lim_and_ticks['yticklabels'])
  ax.grid(which='major', linewidth=0.6, color='black', linestyle='-')
  ax.grid(which='minor', linewidth=0.3, color='grey', linestyle='-')
  ax.xaxis.set_tick_params(labelsize=12, zorder=10000)
  ax.yaxis.set_tick_params(labelsize=12, zorder=10000)
  ax.plot(x, data, linewidth=2)
  plt.savefig('main/ch2-background/{}.pdf'.format(function), dpi=300, format='pdf')



def main():

  x = np.linspace(-6, 6, num=10000)
  data = {
    "sigmoid": [sigmoid(v) for v in x],
    "tanh": [tanh(v) for v in x],
    "relu": [relu(v, 0.1) for v in x]
  }

  locator = {
    "sigmoid": {
      "major": {'xaxis': 5, 'yaxis': 1},
      "minor": {'xaxis': 1, 'yaxis': 0.1}
    },
    "tanh": {
      "major": {'xaxis': 2, 'yaxis': 2},
      "minor": {'xaxis': 0.4, 'yaxis': 0.4}
    },
    "relu": {
      "major": {'xaxis': 1, 'yaxis': 1},
      "minor": {'xaxis': 0.2, 'yaxis': 0.2}
    }
  }

  lim_and_ticks = {
    "sigmoid": {
      'xlim': (-5.75, 5.75), 
      'ylim': (-0.1, 1.1),
      'xticks': (-5, 5), 
      'yticks': (0, 0.5, 1),
      'yticklabels': ['0', '0.5', '1']
    },
    "tanh": {
      'xlim': (-2.3, 2.3),
      'ylim': (-2.3, 2.3),
      'xticks': (-2, 0, 2),
      'yticks': (-2, 2),
      'yticklabels': None
    },
    "relu": {
      'xlim': (-1.3, 1.3),
      'ylim': (-1.3, 1.3),
      'xticks': (-1, 0, 1),
      'yticks': (-1, 1),
      'yticklabels': None
    }
  }

  plot_figures(x, data, locator, lim_and_ticks, 'sigmoid')
  plot_figures(x, data, locator, lim_and_ticks, 'tanh')
  plot_figures(x, data, locator, lim_and_ticks, 'relu')


if __name__ == '__main__':
  main()
