import os
import subprocess

def update_server():
    # Update package list
    subprocess.run(["apt", "update"])

# Call the function to update the server
update_server()