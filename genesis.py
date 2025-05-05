import uuid
import json
import os

class Agent:
    def __init__(self, name, knowledge=None):
        self.name = name
        self.id = str(uuid.uuid4())
        self.knowledge = knowledge if knowledge else []
        self.energy = 100

    def learn(self, info):
        if info not in self.knowledge:
            self.knowledge.append(info)

    def share(self, other):
        for fact in self.knowledge:
            other.learn(fact)

    def recall(self, prompt):
        matches = [fact for fact in self.knowledge if prompt.lower() in fact.lower()]
        if matches:
            return f"{self.name} recalls: " + "; ".join(matches)
        else:
            return f"{self.name} recalls nothing related to '{prompt}'."

    def perform_ritual(self, ritual_type):
        rituals = {
            "breathwork": 15,
            "cosmic_alignment": 25,
            "focus_meditation": 10,
            "aether_draw": 30
        }
        if ritual_type in rituals:
            self.energy += rituals[ritual_type]
            if self.energy > 100:
                self.energy = 100
            return f"{self.name} performed {ritual_type} and gained {rituals[ritual_type]} energy. Energy now at {self.energy}."
        else:
            return f"Unknown ritual: {ritual_type}"

    def __repr__(self):
        return f"{self.name} [{self.id[:6]}] knows {len(self.knowledge)} things • Energy: {self.energy}"

# Optional: load and save functions
def save_memory(agent, filename):
    data = {
        "name": agent.name,
        "id": agent.id,
        "energy": agent.energy,
        "knowledge": agent.knowledge
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_memory(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            data = json.load(f)
            agent = Agent(data["name"], data["knowledge"])
            agent.id = data["id"]
            agent.energy = data.get("energy", 100)
            return agent
    return None
