import uuid

class Agent:
    def __init__(self, name="Agent"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.memory = []

    def learn(self, data):
        self.memory.append(data)

    def think(self):
        return f"{self.name} [{self.id}] knows {len(self.memory)} things."

    def spawn(self, name="SubAgent"):
        return Agent(name=name)
