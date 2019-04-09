import logging
import pyglet
from pyglet.window import mouse, key
from Helpers.Coordinate import Coordinate, Square
import os

resouce_path = [os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "resources"))]

logger = logging.getLogger("mainLogger")

window = pyglet.window.Window(resizable=True)
window._resizable = True
#window.set_fullscreen()

width = window.width
height = window.height

middle_x = width/2
middle_y = height/2

scroll = 0
scroll_default = width/96 # This only work for my own resolution at maximised
scroll_scale = 1000
scroll_delta = 1/scroll_scale
sprite_scale = 20

window_square = None

def get_sprite_scale():
    return max(min(sprite_scale/current_scroll(), 3.0), 0.3)

def current_scroll():
    return (scroll_default + scroll * scroll_scale)

def transform(world_coordinate=None, x=None, y=None): #Transforms a world coordinate into a screen coordinate
    if world_coordinate:
        assert x is None and y is None
        x = world_coordinate.x
        y = world_coordinate.y
    w_scale = width / current_scroll()
    h_scale = height / current_scroll()
    w_half = width/2
    h_half = height/2
    return ((x - middle_x + w_half) * w_scale + middle_x,
            (y - middle_y + h_half) * h_scale + middle_y)

def reverse_transform(x, y, coordinate=True): #Transforms a screen coordinate into a world coordinate
    w_scale = width / current_scroll()
    h_scale = height / current_scroll()
    w_half = width/2
    h_half = height/2
    wcx = (x-middle_x)/w_scale - w_half + middle_x
    wcy = (y-middle_y)/h_scale - h_half + middle_y
    if coordinate:
        return Coordinate(wcx, wcy)
    else:
        return wcx, wcy

def viewpoint_changed():
    global window_square
    lx, ly = reverse_transform(0,0, coordinate=False)
    ux, uy = reverse_transform(width, height, coordinate=False)
    window_square = Square(lx, ly, ux, uy)
viewpoint_changed() #Initializing window_square

@window.event
def on_resize(w, h):
    global width
    global height
    global middle_x
    global middle_y
    old_width = width
    old_height = height
    width = w
    height = h
    middle_x = middle_x - old_width / 2 + width / 2
    middle_y = middle_y - old_height / 2 + height / 2


pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

gameObject = None

label = None
@window.event
def on_draw():
    window.clear()
    if gameObject is not None:
        if gameObject.batch is not None:
            gameObject.batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    print(symbol, modifiers)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        coord = reverse_transform(x, y)
        print(x, y,coord)
        gameObject.world.set_target(coord)

@window.event
def on_mouse_release(x, y, button, modifiers):
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons == mouse.RIGHT:
        global middle_x
        global middle_y
        gx, gy = reverse_transform(x, y, coordinate=False)
        gdx, gdy = reverse_transform(x + dx, y + dy, coordinate=False)
        delta_x = gx-gdx
        delta_y = gy-gdy
        #delta = current_scroll()*0.0015
        #middle_x -= dx*delta
        #middle_y -= dy*delta
        middle_x += delta_x
        middle_y += delta_y
        viewpoint_changed()

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global scroll
    scroll = min(max(scroll + scroll_y * scroll_delta, 0), scroll_default - 1)
    viewpoint_changed()