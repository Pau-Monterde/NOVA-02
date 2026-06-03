# Capa semántica

class SlotData:
    def __init__(self, action=None, object=None, person=None, location=None, time=None, application=None):
        self.action = action
        self.object = object
        self.person = person
        self.location = location
        self.time = time
        self.application = application

class SemanticExtraction:
    def __init__(self, slots:SlotData):
        self.slots = slots