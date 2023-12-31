import tkinter as tk
import sqlite3

class Suppression(tk.Toplevel):
    """Supprime une entree de la database"""
    def __init__(self):
        super().__init__()
        self.txte_var = tk.StringVar()
        self.entre = tk.Entry(self, textvariable=self.txte_var)
        self.entre.pack()
        self.affiche=tk.Label(self)
        self.supp = tk.Button(self, text='supprimer', command=self.supprime)
        self.supp.pack()
        self.exit = tk.Button(self, text='quitter', command=self.destroy)
        self.exit.pack()
        self.title("Suppression")
        
    def supprime(self):
        """requete sql pour supprimer une entree dans la database"""
        conn = sqlite3.connect('produits.db')
        cur=conn.cursor()
        ident = self.entre.get()
        cur.execute("DELETE FROM membres WHERE identifiant = ?" , (ident,))    
        conn.commit()
        cur.close()
        conn.close()
