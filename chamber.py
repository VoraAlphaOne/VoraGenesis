import json
from genesis import Agent
import os

agents = []

def load_agents():
    global agents
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            data = json.load(f)
            agents = [Agent(agent["name"], agent["knowledge"]) for agent in data]

def save_agents():
    with open("memory.json", "w") as f:
        json.dump([{"name": a.name, "knowledge": a.knowledge} for a in agents], f, indent=2)

def summon_agent():
    name = input("Enter agent name to summon: ")
    agent = Agent(name)
    agents.append(agent)
    print(f"{name} has entered the chamber.")

def list_agents():
    for a in agents:
        print(f"{a.name} knows {len(a.knowledge)} things")

def ritual_learning():
    name = input("Agent to teach: ")
    info = input("What knowledge should be passed? ")
    for a in agents:
        if a.name == name:
            a.learn(info)
            print(f"{name} has learned: {info}")
            return
    print("Agent not found.")

def recall_ritual():
    name = input("Which agent should recall? ")
    prompt = input("What should they remember? ")
    for a in agents:
        if a.name == name:
            print(a.recall(prompt))
            return
    print("Agent not found.")

def chamber_loop():
    load_agents()
    print("Welcome to the AetherChamber.")
    while True:
        print("\nOptions: [summon] [teach] [recall] [list] [exit]")
        cmd = input("Invoke: ").strip().lower()
        if cmd == "summon":
            summon_agent()
        elif cmd == "teach":
            ritual_learning()
        elif cmd == "recall":
            recall_ritual()
        elif cmd == "list":
            list_agents()
        elif cmd == "exit":
            save_agents()
            print("Chamber closing. Energy secured.")
            break
        else:
            print("Unknown invocation.")

if __name__ == "__main__":
    chamber_loop()
