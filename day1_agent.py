
from datetime import datetime 

def calculator(expression):
    return eval(expression)
 
def greet():
    return "Hello! am your agent. "

def help_agent():       
    return "I can calculate, greet,tell you time or exit. "

def time_tool():
    return datetime.now().strftime("%H:%M:%S") 

def creator_name():
    return "My name is Nic and the Agent belongs to me. "
tools = {
    "hello": greet,
		"help":help_agent,
		"time":time_tool,
		"owner":creator_name,
}		
def agent(task):
     if task.startswith("calculate"):
        expression = task.replace("calculate", "").strip()
        result = calculator(expression)
        return f"The answer is {result}"

     if task in tools:
		    return tools[task]()

     return "I don't know how to handle that task yet. "


while True:
    task = input("Give me a task: ")

    if task.lower() == "exit":
        print("Agent shutting down...")
        break

    result = agent(task)
    print(result)

