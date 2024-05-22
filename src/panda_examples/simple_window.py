from direct.showbase.ShowBase import ShowBase


class SimpleWindowApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(5, 5, 5)
        self.scene.setPos(-8, 42, 0)


app: SimpleWindowApp = SimpleWindowApp()
app.run()
