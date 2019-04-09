from Graphics import Engine
import pyglet

class GraphicalEntity():
    def __init__(self):
        self.oldsprite = None

    def removed_from_segment(self, world_segment):
        pass

    def draw_text(self, batch, name, world_coordinate):
        x, y = Engine.transform(world_coordinate)
        #print(name, x, y)
        pyglet.text.Label(str(name),
                        font_name="Times New Roman",
                        color=(255,255,255, 255),
                        font_size=36,
                        x = x,
                        y = y,
                        anchor_x="center", anchor_y="center", batch=batch)    
       # new_asteroid = pyglet.sprite.Sprite(player_image,
       #                                     x=self.pos.x * (500/10), y=self.pos.y * (500/10),
       #                                     batch=batch)
        #batch.add(1, player_sprite, None, ('v2f', (self.pos.x*50, self.pos.y*50)), ('c3B', (0,0,255)))

    def draw_sprite(self, batch, image, world_coordinate, rotation=None): #direction
        if rotation is not None:
            rotation = rotation - 90
        x, y = Engine.transform(world_coordinate)
        scale = Engine.get_sprite_scale()
        if self.oldsprite is not None and scale == self.oldsprite.scale and rotation == self.oldsprite.rotation:
            self.oldsprite.set_position(x, y)
            self.oldsprite.batch = batch
        else:   
            self.oldsprite = pyglet.sprite.Sprite(image,
                            x=x,
                            y=y,
                            batch=batch)
            self.oldsprite.scale = scale
            if rotation is not None:
                self.oldsprite.rotation = rotation