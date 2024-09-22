import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
ground = Entity(
    model =   'plane',
    texture = 'grass',
    collider = 'mesh',
    scale = (100,1,100)
)
player = FirstPersonController()

myBall = Entity(model = 'sphere',
                color = color.red,
                collider = 'sphere',
                position = (5, 0.5, 10))



app.run()