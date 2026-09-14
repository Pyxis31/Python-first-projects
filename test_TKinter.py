from tkinter import *

window = Tk()
window.geometry("400x200")  # Taille de la fenêtre

# Centrer la fenêtre sur l'écran
window.eval('tk::PlaceWindow . center')  # Méthode pour centrer la fenêtre

# Label avec texte en rouge et police de taille 20
MyLabel = Label(
    window,
    text="Hello World !",
    fg="red",
    font=("Arial", 20)
)
MyLabel.pack(pady=20)  # Espace vertical

# Bouton
MyButton = Button(
    window,
    text="Cliquez ici",
    font=("Arial", 12)
)
MyButton.pack()

window.mainloop()