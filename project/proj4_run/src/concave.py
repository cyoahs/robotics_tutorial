import pybullet as p
import os

f_in = os.path.join('project', 'proj4_run', 'rsc', 'mesh', 'map.obj')
f_out = os.path.join('project', 'proj4_run', 'rsc', 'mesh', 'map_concave.obj')
log = os.path.join('project', 'proj4_run', 'rsc', 'mesh', 'log.txt')

p.vhacd(f_in, f_out, log, resolution=32000000)
