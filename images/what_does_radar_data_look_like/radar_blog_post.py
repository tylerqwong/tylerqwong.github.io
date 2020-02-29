import matplotlib
matplotlib.use('Qt4Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas



import contextMaps
import plotRadar
import watermarkUTIG

product = 'pik1'
channel = 2

fig_width = 12.0
fig_height = 6.0
dpi = 150

fontsize = 30
linewidth = 2

#########################

# The all-data figure
contextMaps.create_context_maps([-3000000, 3000000], [-2500000, 2500000], 'all_UTIG',
                                pst_regexps=['.*'], bg_pst_color='k', num_maps=1, horiz=True)









#########################
# The South Pole figure (no context map for it!)
pst = 'NPX/SJB2/NPX02a'

fig = Figure((fig_width, fig_height), dpi=dpi)
canvas = FigureCanvas(fig)
ax = fig.add_axes([0, 0, 1, 1])

pst_frac = plotRadar.plot_radar(ax, pst, product, channel,
                                num_pixels=dpi*fig_width, cmap='gray',
                                tlim=[2700, 7500], slim=[0, 2200])

ax.text(2850, 150, 'Air', color='r', size=fontsize)
ax.text(2850, 800, 'Ice', color='r', size=fontsize)
ax.text(2850, 1900, 'Bed', color='r', size=fontsize)
ax.text(5800, 800, 'South Pole Station', color='r', size=fontsize)
ax.arrow(6200, 875, -200, 450, ec='r', fc='r', width=3, lw=linewidth)

watermarkUTIG.add_logo(fig, 0.01, 0.1, corner='lr')

canvas.draw()
filename = pst.replace('/', '.') + '_full.png'
canvas.print_figure(filename)


#########################
# The Totten figure
pst = 'TOT/JKB2d/X16a'


fig = Figure((fig_width, fig_height), dpi=dpi)
canvas = FigureCanvas(fig)
ax = fig.add_axes([0, 0, 1, 1])

pst_frac = plotRadar.plot_radar(ax, pst, product, channel,
                                num_pixels=dpi*fig_width, cmap='gray',
                                slim=[0, 2500])
watermarkUTIG.add_logo(fig, 0.01, 0.1, corner='ll')
canvas.draw()
filename = pst.replace('/', '.') + '_plain.png'
canvas.print_figure(filename)


# Centered @ 2270, -1160, 400x400
contextMaps.create_context_maps([2070000, 2470000], [-1260000, -860000],
                                pst.replace('/','_'),
                                main_pst=pst, pst_frac=pst_frac,
                                pst_regexps='TOT', num_maps=3, horiz=True)


ax.text(150, 300, 'Air', color='r', size=fontsize)
ax.text(150, 700, 'Ice Shelf', color='r', size=fontsize)
ax.text(150, 1300, 'Ocean', color='r', size=fontsize)
ax.text(6500, 700, 'Grounded Ice', color='r', size=fontsize)
ax.text(7800, 2000, 'Rock', color='r', size=fontsize)
ax.text(2550, 1600, 'Crevasses', color='r', size=fontsize)
ax.arrow(3200, 1450, 100, -200, ec='r', fc='r', width=3, lw=linewidth)

ax.text(5950, 2150, 'Grounding Zone', color='r', size=fontsize, horizontalalignment='right', verticalalignment='center')
gz = matplotlib.patches.Ellipse(xy=[6350, 2150], width=600, height=200,
                                 ec='r', fc='none', linewidth=linewidth)
ax.add_artist(gz)

canvas.draw()
filename = pst.replace('/', '.') + '_full.png'
canvas.print_figure(filename)


#########################
# The MIS figure
pst = 'MIS/JKB2e/Y25a'

fig = Figure((fig_width, fig_height), dpi=dpi)
canvas = FigureCanvas(fig)
ax = fig.add_axes([0, 0, 1, 1])

pst_frac = plotRadar.plot_radar(ax, pst, product, channel,
                                num_pixels=dpi*fig_width, cmap='gray',
                                tlim=[0, 3700], slim=[0, 1400])

# Centered @ 310, -1290; 200x200km
contextMaps.create_context_maps([210000, 410000], [-1390000, -1190000],
                                pst.replace('/','_'), main_pst=pst)


ax.text(75, 450, 'Air', color='r', size=fontsize)
ax.text(75, 575, 'Ice Shelf', color='r', size=fontsize)
ax.text(75, 700, 'Water', color='r', size=fontsize)

ax.text(3625, 450, 'Air', color='r', size=fontsize, horizontalalignment='right')
ax.text(3625, 650, 'Water', color='r', size=fontsize, horizontalalignment='right')

ax.text(1900, 250, 'Ross Island\n(McMurdo)', color='r', size=fontsize,
        verticalalignment='center', horizontalalignment='left')
ax.arrow(1850, 250, -50, 100, ec='r', fc='r', width=3, lw=linewidth)

ax.text(2500, 1225, 'Edge of Ice Shelf', color='r', size=fontsize,
        verticalalignment='center')
ax.arrow(2800, 1150, -50, -75, ec='r', fc='r', width=3, lw=linewidth)
ax.arrow(2850, 1150, 0, -275, ec='r', fc='r', width=3, lw=linewidth)
ax.arrow(2900, 1150, 75, -100, ec='r', fc='r', width=3, lw=linewidth)

ax.text(1300, 1325, 'Multiples', color='r', size=fontsize,
        horizontalalignment='right', verticalalignment='center')

ax.arrow(800, 1250, -50, -465,  ec='r', fc='r', width=3, lw=linewidth)
ax.arrow(850, 1250, 0, -375,  ec='r', fc='r', width=3, lw=linewidth)
ax.arrow(900, 1250, 50, -225,  ec='r', fc='r', width=3, lw=linewidth)

ax.arrow(1150, 1250, -50, -150,  ec='r', fc='r', width=3, lw=linewidth)
ax.arrow(1200, 1250, 0, -110,  ec='r', fc='r', width=3, lw=linewidth)
ax.arrow(1250, 1250, 100, -275,  ec='r', fc='r', width=3, lw=linewidth)


watermarkUTIG.add_logo(fig, 0.01, 0.1, corner='ul')

canvas.draw()
filename = pst.replace('/', '.') + '_full.png'
canvas.print_figure(filename)



#########################
# The crazy noisy figure.
pst = 'ICP2/JKB1a/F09T01a'

fig = Figure((fig_width, fig_height), dpi=dpi)
canvas = FigureCanvas(fig)
ax = fig.add_axes([0, 0, 1, 1])

pst_frac = plotRadar.plot_radar(ax, pst, product, channel,
                                num_pixels=dpi*fig_width, cmap='gray',
                                tlim=[0, 3100], slim=[0, 2200])

watermarkUTIG.add_logo(fig, 0.01, 0.1, corner='ll')

canvas.draw()
filename = pst.replace('/', '.') + '_full.png'
canvas.print_figure(filename)

