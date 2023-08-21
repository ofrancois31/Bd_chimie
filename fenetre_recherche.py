import tkinter as tk
import sqlite3
#fenetre secondaire de recherche de nom dans la database
class Recherche_Fenetre(tk.Toplevel):
    """fenetre secondaire de recherche de nom dans la database"""    
    def __init__(self, parent):
        super().__init__(parent)
        self.textvar= tk.StringVar()
        self.saisie = tk.Entry(self,textvariable=self.textvar)
        self.saisie.insert(0,"Entrez ici votre texte")
        self.saisie.pack()
        self.button = tk.Button(self, text="Quitter",command=self.destroy)
        self.affiche = tk.Label(self, text="Affichage", justify="left")
        self.affiche.pack()
        self.button.pack(pady=5, ipadx=2, ipady=2) 
        self.btn = tk.Button(self, text='Rechercher', command=self.action_saisie)
        self.btn.pack()
        self.title("Recherche")
        self.geometry("400x200")
    
    def action_saisie(self):
        """requete sql pour rechercher le nom si il existe et l'affiche dans self.affiche"""
        conn = sqlite3.connect('produits.db')
        cur = conn.cursor()
        nom= self.saisie.get()
        cur.execute("SELECT identifiant , nom , quantite FROM membres WHERE nom = ?" ,(nom,))
        reponse = cur.fetchall()
        if reponse == []:
            self.affiche.config(text="Pas de correspondance")
        else:
            self.affiche.config(text=str(reponse)+'\n')
        cur.close()
        conn.close()
        
        
        
        
