import pyglet
ball_image = pyglet.image.load('D:/Coding/TradingGame/resources/square.png')
ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)

window = pyglet.window.Window()

@window.event
def on_draw():
    ball.draw()

pyglet.app.run()