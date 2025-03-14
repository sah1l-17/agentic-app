import os

plot_filename = os.path.abspath(f"{state.ticker}_plot.png")
plt.savefig(plot_filename)