import pyglet
import os

filetypes = [".png"]

resources = None
def load_resources():
    global resources
    if resources is None:
        curdir = os.path.dirname(__file__)
        pyglet.resource.path = [curdir]
        pyglet.resource.reindex()
        resources = {}
        for filename in os.listdir(curdir):
            for ft in filetypes:
                if filename.endswith(ft):
                    fixed_name = filename[:-len(ft)]
                    resources[fixed_name] = pyglet.resource.image(filename)
                    resources[fixed_name].anchor_x = resources[fixed_name].width/2
                    resources[fixed_name].anchor_y = resources[fixed_name].height/2
                    
                    break
    return resources