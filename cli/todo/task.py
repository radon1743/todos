import json
import os

import requests
from rich.console import Console

console = Console(stderr=True)
API = "http://localhost:8888/api/"
class TasksManager:
    def __init__(self):
        self.todo_data = {}
    
    def add_task(self, task_id:str, date:str, text:str, completed:bool, username:str)-> None:
        """Add task"""
        todo_data = {task_id: {"date": date, "text": text, "completed": completed}}
        user_file_path = username

        try:
            data = {}
            if not os.path.exists(user_file_path):
                os.makedirs(os.path.dirname(user_file_path), exist_ok=True)
            else:
                with open(user_file_path, "r") as f:
                    data = json.load(f)
            data.update(todo_data)

            with open(user_file_path,"w") as f:
                json.dump(data,f,indent=2)
            
            console.print(f"[green]Task added successfully for user {username.split("/")[-1:][0]} [/green]")
        except Exception as e:
            console.print(f"[red]Error writing data up user {e}: [/red]") 
    
    def get_task(self, username: str, all:bool):
        all = True

        if(all):   
            response = requests.get(API + "findAllTasks")
        else:
            response = requests.get(f"{API}findAllTasks/{username}")
        
        if(response.status_code == 200):
            data = response.json()
            console.print(data)
        else:
            console.print(f"[red]Connection Error !! /n Status code: {response.status_code }[/red]")

