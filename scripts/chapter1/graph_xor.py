
from os.path import join
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
      return tuple(i/inch for i in tupl[0])
    else:
      return tuple(i/inch for i in tupl)

path = '/Users/alexandrearaujo/Desktop/Thesis'

def main():

  fig, ax = plt.subplots(figsize=cm2inch(4, 4))
  ax.scatter([0], [0], marker='^', color='red')
  ax.scatter([0], [1], marker='o', color='blue')
  ax.scatter([1], [0], marker='o', color='blue')
  ax.scatter([1], [1], marker='^', color='red')
  ax.set_xticks(np.arange(0, 2, step=1))
  ax.set_yticks(np.arange(0, 2, step=1))
  ax.set_ylim([-0.1, 1.1])
  ax.set_xlim([-0.1, 1.1])
  
  # Hide the right and top spines
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)

  plt.tight_layout()
  name = join(path, "figures/chapter1/xor_function.pdf")
  plt.savefig(name, dpi=300, format='pdf', bbox_inches="tight")

if __name__  == '__main__':
  main()
