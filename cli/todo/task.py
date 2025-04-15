import json
import os

import requests
from rich.console import Console

console = Console(stderr=True)
API_URL = "http://localhost:8888/api/"
class TasksManager:
    
    def __init__(self):
        self.todo_data = {}
    
    def add_local_task(self, task_id:str, date:str, text:str, completed:bool, username:str)-> None:
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

    def add_remote_task(self, task_id:str, date:str, text:str, completed:bool, username:str):
        "Add remote tasks to API URL"
        
        todo_data = {
                "taskId": task_id, 
                "date": date, 
                "text": text, 
                "isCompleted": completed
            }
        try:
            response = requests.post(API_URL + "addTasks", json = todo_data)

            if(response.status_code == 200):
                console.print(f"[bold green]✔️  Added successfully {task_id}[/bold green]")
            else:
                console.print(f"[red]Connection Error !! \nStatus code: {response.status_code }[/red]")
        except Exception as e:
            console.print(f"[bold red] Connection fail: Server is down[/bold red]")
            

    def get_task(self, all:bool, id: str):
        if(all):   
            response = requests.get(API_URL + "findAllTasks")
        else:
            response = requests.get(f"{API_URL}findAllTask/{id}")
        
        if(response.status_code == 200):
            data = response.json()
            console.print(data)
        else:
            console.print(f"[red]Connection Error !! \nStatus code: {response.status_code }[/red]")
    
    def delete_task(self, taskId: str):
        response = requests.delete(f"{API_URL}deleteTasks/{taskId}")
        if(response.status_code == 200):
            console.print(f"[green]Task Succefully deleted : {taskId}[/green]")
        else:
            console.print(f"[red]Connection Error !! \nStatus code: {response.status_code }[/red]")
    
    def edit_task(self, taskId: str, date:str, text:str, completed:bool):
        new_todo_data = {}
        
        if date is not None:
            new_todo_data["date"] = date
        if text is not None:
            new_todo_data["text"] = text
        if completed is not None:
            new_todo_data["isCompleted"] = completed 


        response = requests.put(f"{API_URL}editTask/{taskId}", json=new_todo_data)
        if(response.status_code == 200):
            data = response.json()
            console.print(data)
        else:
            console.print(f"[red]Connection Error !! \nStatus code: {response.status_code }[/red]")

