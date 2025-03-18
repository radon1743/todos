import json
import os

import click
from rich.console import Console

from datetime import datetime
from . import __version__

console = Console(stderr=True)
USER_FILE = "./users/users.json"
SESSION_FILE = "./users/session.json"

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
    pass

@main.command()
@click.option("-c", "--clear", type=bool, required=False, is_flag=True, help="Clear session file")
def flush(clear:bool):
    """Clears out session file"""
    if(clear): 
        with open(SESSION_FILE, 'w') as f:
            json.dump({}, f, indent=2)
    else:
        with open(SESSION_FILE, 'r') as f:
            console.print(json.load(f)) 

@main.command()
def get_user():
    """Check the signed-in user."""
    with open(SESSION_FILE, 'r') as f:
        data = json.load(f)
        if(len(data)>0):
            console.print(f"Current signed in user > [blue]{data.popitem()[1]}[/blue]")
        else:
            console.print(f"[red] No user signed in [/red]")

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

if __name__=="__main__":
    main()