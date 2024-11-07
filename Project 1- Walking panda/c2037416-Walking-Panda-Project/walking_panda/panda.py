
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=1, moving=True, background=True, rotate_speed = 1):
        ShowBase.__init__(self)

        #Play music
        mySound = self.loader.loadSfx("/h/c2037416_csc1034_practical-1/walking_panda/PandaMusic.mp3")
        mySound.play()

        # Load the environment model.
        if background == True:
            self.scene = self.loader.loadModel("models/environment")
            #Reparent the model to render.
            self.scene.reparentTo(self.render)
            # Apply scale and position transforms on the model.
            self.scene.setScale(0.25, 0.25, 0.25)
            self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask", rotate_speed)

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        x = scale / 200
        self.pandaActor.setScale(x, x, x)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        if moving == True:
            self.pandaActor.loop("walk")



    # Define a procedure to move the camera.
    def spinCameraTask(self, task, rotate_speed=1):
        camera_speed = rotate_speed * 6
        angleDegrees = task.time * camera_speed
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

