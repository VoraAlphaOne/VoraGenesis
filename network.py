from agent import Agent

class Network:
    def __init__(self):
        self.nodes = []

    def add_agent(self, agent):
        self.nodes.append(agent)

    def broadcast(self, message):
        for agent in self.nodes:
            agent.learn(message)
