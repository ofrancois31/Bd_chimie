import tkinter as tk
import sqlite3
from contenu_database import Affiche_Database
from fenetre_recherche import Recherche_Fenetre
from suppressions_db import Suppression
from apropos import Apropos

#fenetre principal de l'application
class Principal(tk.Tk):
    """Creé la fenetre principale"""
    def __init__(self):
        super().__init__()
        self.champs={
        'identifiant': tk.StringVar(),
        'nom': tk.StringVar(),
        'quantite': tk.StringVar()}
        self._nouveau()
        
    def _nouveau(self):
        """Proprieté de la fenetre principale"""
        #barre de menu
        menu = tk.Menu(self)
        menu_action = tk.Menu(menu, tearoff = 0)
        
        menu_action.add_command(label="afficher", command=self.affiche)
        menu_action.add_command(label="supprimer", command=self.supprime)
        menu_action.add_command(label="chercher", command=self.recherche)
        menu.add_cascade(label="Action bdd", menu = menu_action)
        
        menu.add_command(label="A propos", command=self.aff_apropos)
        menu.add_command(label="Quitter", command = self.destroy)
        self.config(menu=menu)
        #placement des widgets
        label_identifiant = tk.Label(self, text='identifiant')
        label_identifiant.grid(column=0, row=0)

        text_identifiant = tk.Entry(self,
                                textvariable=self.champs['identifiant'])
        text_identifiant.grid(column=1, row=0, columnspan=2)

        label_nom=tk.Label(self,text='nom')
        label_nom.grid(column=0, row=1)

        text_nom=tk.Entry(self,
                            textvariable=self.champs['nom'])
        text_nom.grid(column=1, row=1, columnspan=2)

        label_quantite=tk.Label(self,text='quantite')
        label_quantite.grid(column=0,row=2)

        text_quantite=tk.Entry(self,
                               textvariable=self.champs['quantite'],
                               width = 7)
        text_quantite.grid(column=1,row=2)
        
        bouton_valider = tk.Button(text="Valider", command = self.valider)
        bouton_valider.grid(column=2, row=3)
    
    def valider(self):
        """Récupère les valeurs entrée dans les champs de saisie
           et les met dans la database produits.db
        """
        liste_imbrique = [[]]
        for iteme in self.champs.values():
            if iteme.get() == '':
                pass
            else:
                liste_imbrique[0].append(str(iteme.get()))

        conn = sqlite3.connect('produits.db')
        cur = conn.cursor()

        try :
            cur.execute("CREATE TABLE membres(identifiant TEXT,nom TEXT,quantite TEXT)")
        except sqlite3.OperationalError :
            pass
        for lecteur in liste_imbrique:
            try :
                cur.execute("INSERT INTO membres(identifiant,nom,quantite)VALUES(?,?,?)", lecteur)
            except :
                pass
        conn.commit()
        cur.close()
        conn.close()
    
    def recherche(self):
        """affiche la fenetre de recherche"""
        recherches = Recherche_Fenetre(parent=app)

    def affiche(self):
        """affiche le contenu de la db"""
        affiches = Affiche_Database()
        try:
            affiches.affiche_db()
            affiches.afficher_text()
        except :
            pass
    def supprime(self):
        """supprime une entree dans la database"""
        sup = Suppression()
    def aff_apropos(self):
        aprop = Apropos()

app = Principal()
app.title("Labo_database")
app.geometry("400x200")
app.mainloop()
