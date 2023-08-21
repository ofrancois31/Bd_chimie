import tkinter as tk

class Apropos(tk.Toplevel):
    """
    affiche le texte dans le menu apropos
    """
    def __init__(self):
        super().__init__()
        texte = tk.Label(self,text="Gestion de base de donnée de produits chimiques")
        texte.pack()
        texte2 = tk.Label(self, text="code par ofrancois")
        texte2.pack()
        bouton_quitter = tk.Button(self, text="Quitter", command=self.destroy)
        bouton_quitter.pack()
