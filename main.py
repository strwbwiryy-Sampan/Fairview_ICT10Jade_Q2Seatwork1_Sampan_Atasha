from pyscript import document, display

def checkName(e):
    full_names= ["Atasha Sampan", "Zyrene Nieto", "Pia Bagtas", "Dustin Cunanan"]


    name1= document.getElementById("name1").value
    name2 = document.getElementById("name2").value
    name= name1 + " " + name2

    confirm_name = name in full_names

    message = (f'Sorry {name}, your name is not found.' , f'Congratulations! {name}, your name is found.')

    document.getElementById("output1").innerHTML = message[confirm_name]