import FreeSimpleGUI as sg
import  functions
label= sg.Text("Type  your to do")
input_box = sg.InputText(tooltip="enter your task", key = "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos_list",
                      enable_events=True, size=[45,10])
window = sg.Window('my to-do app',
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_edit = values['todos_list'][0]
            new_todo = values['todo_list']
            functions.write_todos(new_todo)
            

        case sg.WIN_CLOSED:
            break

window.close()