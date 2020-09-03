import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()

ax = fig.add_subplot(111)

gs = gridspec.GridSpec(3,1)
ax.set_position(gs[0:2].get_position(fig))
ax.set_subplotspec(gs[0:2])              # only necessary if using tight_layout()

# fig.add_subplot(gs[2])

# fig.tight_layout()                       # not strictly part of the question

plt.show()