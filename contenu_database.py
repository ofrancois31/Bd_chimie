import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import sqlite3
#affiche une fenetre scollable et affiche tout le contenu de la database
class Affiche_Database(tk.Toplevel):
    """Fenetre secondaire qui affiche le contenu de la database"""
    def __init__(self):
        super().__init__()
        self.text_area = ScrolledText(self, width = 100, height= 100)
        self.text_area.pack()
        self.title("Contenu_database")
    
    def affiche_db(self):
        """requete sql pour afficher le contenu de la database"""
        try :
            conn = sqlite3.connect('produits.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM membres")
            variable=cur.fetchall()
            return(str(variable))
        
        except sqlite3.OperationalError :
            pass    
            

    def afficher_text(self):
        """insert le contenu de la database dans la fenetre scrollable"""
        texte = self.affiche_db()
        self.text_area.insert(tk.END, texte)

