import json
import os

import click
from rich.console import Console

from datetime import datetime
from . import __version__
from . import task

tasks_manager = task.TasksManager()
console = Console(stderr=True)
USER_FILE = "./users/users.json"
SESSION_FILE = "./users/session.json"
DATA_FILE = "./users/data/"

def user_file_exits():
    """Ensure User file exist, if not it creates it"""
    if not os.path.exists(USER_FILE):
        os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
        with open(USER_FILE,'w+') as f:
            json.dump({}, f, indent=2)

def save_session(username):
    """Save session Info"""
    current_time = str(datetime.now())

    with open(SESSION_FILE, 'r') as f:
        session_data = json.load(f)
        session_data.update({current_time:username})
    with open(SESSION_FILE, 'w') as f:    
        json.dump(session_data, f, indent=2)

@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """CLI based TODO application"""
    # user = get_user()
    # if user!="guest":
    #     console.print(f"[green]{user}[/green]", end=" ")
    # console.print("> ", end="")  
    pass

@main.command()
@click.option("-s", "--session", type=bool, required=False, is_flag=True, help="Flush session")
def flush(session:bool):
    """Clears out or outputs session file"""
    if(not session): 
        with open(SESSION_FILE, 'w') as f:
            json.dump({}, f, indent=2)
    else:
        with open(SESSION_FILE, 'r') as f:
            console.print(list(json.load(f))) 

@main.command()
def get_user() -> str:
    """Check the signed-in user."""
    with open(SESSION_FILE, 'r') as f:
        data = json.load(f)
        if(len(data)>0):
            user = data.popitem()[1]
            console.print(f"Current signed in user > [blue]{user}[/blue]")
            return user
        else:
            console.print(f"[red] No user signed in [/red]")
            return "guest"

@main.command()
@click.option("-u", "--username", type = str, required=True, help="User name")
@click.option("-p", "--password", type = str, required=True, help="Password")
def sign_in(username:str,password:str) -> None:
    """
    Sign in with: >todo sign-in -u {username} -p {password}

    If sign in successful the Datetime and username is stored in session 
    """
    with open(USER_FILE,"r") as f:
            data = json.load(f)
    
    if username in data.keys() and password == data[username]:
        save_session(username)
        console.print(f"[green]Signed in successfully as {username}[/green]")
    else:
        console.print(f"[red]Invalid username or password[/red]")
    

@main.command()
@click.option("-u", "--username", type = str, required=True, help="User name")
@click.option("-p", "--password", type = str, required=True, help="Password")
def make_user(username:str,password:str)-> None:
    """Make new user and set up passowrds"""
    user_file_exits()
    try:
        user_data = {username:password}
        with open(USER_FILE, "r") as f:
            data = json.load(f)
            data.update(user_data)
            
        with open(USER_FILE,"w") as f:
            json.dump(data,f,indent=2)
            
    except Exception as e:
        console.print(f"[red]Error Signing up user {e}: [/red]")

def get_curr_user() -> str:
    """Check the signed-in user."""
    with open(SESSION_FILE, 'r') as f:
        data = json.load(f)
        if(len(data)>0):
            user = data.popitem()[1]
            return DATA_FILE + user + ".json"
        else:
            return DATA_FILE + "guest" + ".json"


@main.command()
@click.option("-d", 
              "--date",
              type=str,default= str(datetime.now().strftime("%d/%m/%Y")),
              required=False,
              help="Conpletion date for Task")
@click.option("-t", 
              "--text", 
              type=str, 
              required=True, 
              help="Text for Task")
@click.option("-c", 
              "--completed", 
              is_flag=True, 
              help="Is the task completed?")
@click.option("-l", 
              "--local", 
              is_flag=True , 
              help="Save task only locally")
def add_task(date:str, text:str, completed:bool, local:bool)-> None:
    """Add task"""
    task_id  = str(datetime.now().timestamp()).replace(".","")
    if (local):
        tasks_manager.add_local_task(task_id,date,text,completed,get_curr_user())
    else:
        tasks_manager.add_remote_task(task_id,date,text,completed,get_curr_user())


@main.command()
@click.option("-a", "--all", is_flag=True, help="Get all tasks")
@click.option("-i", 
              "--id", 
              type=str, 
              help="Task id")
def get_tasks(all:bool, id:str)->None:
    "Get remote tasks"
    username = get_curr_user()
    tasks_manager.get_task(all, id)

@main.command()
@click.option("-i", 
              "--id", 
              type=str, 
              required=True, 
              help="Task id to be deleted")
def del_task(id:str) ->None:
    "Delete task"
    tasks_manager.delete_task(id)

@main.command()
@click.option("-i", 
              "--id", 
              type=str, 
              required=True, 
              help="Task id to be edited")
@click.option("-d", 
              "--date",
              type=str,
              required=False,
              default=None,
              help="Conpletion date for Task")
@click.option("-t", 
              "--text", 
              type=str,
              default=None,
              help="Text for Task")
@click.option("-c", 
              "--completed", 
              is_flag=True,
              default=None,
              help="Is the task completed?")
def edit_task(id:str, date:str, text:str, completed:bool) ->None:
    "Edit task"

    tasks_manager.edit_task(id, date, text, completed)

if __name__=="__main__":
    main()