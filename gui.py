from webbrowser import open_new

import FreeSimpleGUI as sg
import  functions
import  time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

clock =  sg.Text('', key ="clock")
sg.theme("DarkTeal12")
label= sg.Text("Type  your to do")
input_box = sg.InputText(tooltip="enter your task", key = "add_todo")
add_button = sg.Button(size =3, image_source="add.png", mouseover_colors="lightGrey",
                       tooltip= "Add todo", key ='Add')
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos_list",
                      enable_events=True, size=[45,10])
window = sg.Window('my to-do app',
                   layout=[[clock],[label],[input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))
while True:

    events, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    match events:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['add_todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)

        case "Edit":
            try:
                todo_edit = values['todos_list'][0] #we use [0] to get a string
                new_todo = values['add_todo']
                todos_list = functions.get_todos()
                index = todos_list.index(todo_edit)
                todos_list[index] = new_todo
                functions.write_todos(todos_list)
                window['todos_list'].update(values = todos_list)
            except IndexError:
                sg.popup("Please select an item first", font=("Roman",22))
        case 'todos_list':
            window["add_todo"].update(value = values['todos_list'][0])
        case 'Complete':
            try:
              tod_comp = values['todos_list'][0]
              todos = functions.get_todos()
              todos.remove(tod_comp)
              functions.write_todos(todos)
              window['todos_list'].update(values = todos)
              window['add_todo'].update(value ="")
            except IndexError:
                sg.popup("Please select an item first", font=("Roman",22))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()