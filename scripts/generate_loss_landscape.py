"""Generate the navigation artwork as level sets of a smooth 2D loss surface.

Run with Python, NumPy and Matplotlib. The SVG is a build-time asset;
visitors do not need JavaScript or these dependencies.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

width, height = 1600, 180
x = np.linspace(-8, 8, 1200)
y = np.linspace(-0.9, 0.9, 200)
xx, yy = np.meshgrid(x, y)
# Smooth nonconvex landscape: a curved valley and three distinct basins.
valley = yy - 0.20 * np.sin(0.85 * xx)
loss = 0.08 * xx**2 + 2.5 * valley**2
loss -= 3.1 * np.exp(-((xx + 4.5)**2 / 1.8 + (yy + 0.12)**2 / 0.20))
loss -= 2.2 * np.exp(-((xx - 0.2)**2 / 1.1 + (yy - 0.12)**2 / 0.14))
loss -= 2.8 * np.exp(-((xx - 4.5)**2 / 2.1 + (yy + 0.08)**2 / 0.28))
fig, ax = plt.subplots()
contours = ax.contour(xx, yy, loss, levels=np.linspace(-2.8, 7.0, 29))
paths = []
for segments in contours.allsegs:
    for segment in segments:
        if len(segment) < 3:
            continue
        points = np.column_stack(((segment[:, 0] + 8) / 16 * width,
                                  (0.9 - segment[:, 1]) / 1.8 * height))
        commands = ['M' + f'{points[0, 0]:.2f},{points[0, 1]:.2f}']
        commands += ['L' + f'{px:.2f},{py:.2f}' for px, py in points[1:]]
        paths.append('<path d="' + ' '.join(commands) + '"/>')
plt.close(fig)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <title>Contour lines of a two-dimensional loss landscape</title>
  <g fill="none" stroke="#68afc1" stroke-opacity="0.28" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
    {''.join(paths)}
  </g>
</svg>
'''
output = Path(__file__).resolve().parents[1] / 'assets/img/loss-landscape.svg'
output.write_text(svg)
print(f'Generated {len(paths)} contour paths in {output.name}')
