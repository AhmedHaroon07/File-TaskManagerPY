import PySimpleGUI as sg
import os
import subprocess
import threading
import sys

sg.theme('LightBrown1')

def create_file(file_path):
    try:
        with open(file_path, 'w'):
            sg.popup(f"File '{file_path}' File Created!.")
    except FileExistsError:
        sg.popup(f"File '{file_path}' already exists!")
    except Exception as e:
        sg.popup(f"An error occurred: {str(e)}")

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        sg.popup(f"Folder '{folder_name}' Folder Has Been Created.")
    except FileExistsError:
        sg.popup(f"Folder '{folder_name}' already exists!")

def change_file_permissions(file_path, permissions):
    try:
        os.chmod(file_path, permissions)
        sg.popup(f"Permissions for '{file_path}' changed successfully.")
    except FileNotFoundError:
        sg.popup(f"File '{file_path}' not found!")
    except Exception as e:
        sg.popup(f"An error occurred: {str(e)}")

def search_files(keyword):
    try:
        results = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if keyword in file:
                    results.append(os.path.join(root, file))
        if results:
            sg.popup(f"Files containing '{keyword}':\n{', '.join(results)}")
        else:
            sg.popup(f"No files found containing '{keyword}'.")
    except Exception as e:
        sg.popup(f"An error occurred: {str(e)}")

def sort_array(arr):
    arr.sort()
    sg.popup(f"Sorted array: {arr}")

def scheduling_algorithms(selected_app):
    py_script_dict = {
        'First Come First Serve': '/home/ahmed/fcfs.py',
        'Shortest Job First': '/home/ahmed/SJF.py',
        'Round Robin': '/home/ahmed/rr.py',
        'Priority Scheduling': '/home/ahmed/Priority.py',
    }

    try:
        py_script_path = py_script_dict.get(selected_app)
        if py_script_path:
            # Determine the Python interpreter's executable (python.exe or python3)
            python_executable = sys.executable
            # Construct the command to run the Python script
            command = [python_executable, py_script_path]
 
            subprocess.Popen(command)
            sg.popup(f"Running Python script: {selected_app}")
        else:
            sg.popup("Invalid script option selected.")
    except Exception as e:
        sg.popup(f"An error occurred while running the Python script: {str(e)}")
        
        
def open_from(selected_app):
    py_script_dict = {
        'Image Viewer': 'eog pfp.jpeg',
        'File Explorer': 'nautilus . Documents',
        'Google Chrome': '/usr/bin/google-chrome',
    }

    try:
        app_command = py_script_dict.get(selected_app)
        if app_command:
            subprocess.Popen(app_command, shell=True)
            sg.popup(f"Opening application: {selected_app}")
        else:
            sg.popup("Invalid application option selected.")
    except Exception as e:
        sg.popup(f"An error occurred while opening the application: {str(e)}")
       

#def open_application(selected_app):
 #   py_script_dict = {
   #     'FCFS': '/home/ahmed/fcfs.py',
  #      'SJF': '/home/ahmed/SJF.py',
    #    'RR': '/home/ahmed/rr.py',
     #   'Priority': '/home/ahmed/Priority.py',
#    }

#window starts from here


layout = [
    [sg.Column([
        [sg.Text("\t\tChoose any Option", font=("Helvetica", 20, "bold"), text_color="purple")],
    ], element_justification='center')],
    [sg.Text("File Operations", font=("Helvetica", 14))],
    [sg.Button("Create a File"), sg.InputText(key='-FILE-')],
    [sg.Button("Make a Folder"), sg.InputText(key='-FOLDER-')],
    [sg.Button("Search for a File"), sg.InputText(key='-KEYWORD-')],
    [sg.Button("Change File Permissions"), sg.InputText(key='-FILE-PATH-'), sg.InputText(key='-PERMISSIONS-')],

    [sg.Text("\nArray Operations", font=("Helvetica", 14))],
    [sg.Button("Sort Array"), sg.InputText(key='-ARRAY-')],
    
    [sg.Text("\nScheduling Algorithms", font=("Helvetica", 14))],
    [sg.Button("Scheduling Algorithms"), sg.Combo(['First Come First Serve', 'Shortest Job First', 'Round Robin', 'Priority Scheduling'], key='-APP-', enable_events=True)],
    
    [sg.Text("\nOpen Applications", font=("Helvetica", 14))],
    [sg.Button("Open an APP"), sg.Combo(['Image Viewer', 'File Explorer', 'Google Chrome'], key='-APPLI-', enable_events=True)],
    
    [sg.Text("\t\t\t\t\t\t\t\t\t\t\t\tAhmed Haroon", font=("Calibri", 8),text_color="black", key='-AHMED-')]
]

    
    

 



window = sg.Window('My Operating System', layout, resizable= False, size=(800,540), font=("Futura"))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "Create a File":
        create_file(values['-FILE-'])
        
    if event == "Make a Folder":
        create_folder(values['-FOLDER-'])    
        
    elif event == "Search for a File":
        search_files(values['-KEYWORD-'])            

    elif event == "Change File Permissions":
        file_path = values['-FILE-PATH-']
        permissions = int(values['-PERMISSIONS-'], 8)
        change_file_permissions(file_path, permissions)



    elif event == "Sort Array":
        try:
            arr = [int(x) for x in values['-ARRAY-'].split(',')]
            sort_array(arr)
        except ValueError:
            sg.popup("Please enter a valid comma-separated list of integers.")

    elif event == "-APP-":
        selected_app = values['-APP-']
        scheduling_algorithms(selected_app)
        
    elif event == "-APPLI-":
    	preferred_app = values['-APPLI-']
    	open_from(preferred_app)
    	 

window.close()

