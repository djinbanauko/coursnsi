# TP  SQLite

## Notions de bases

Quelques types de  valeurs :

- **NULL** : la valeur null

- **INTEGER** : entier, booléen(0 ou 1)

- **REAL** : nombre flottant

- **VARCHAR(n)** : chaîne de caractère de longueur variable allant jusqu’à  n

- **CHAR(n):**  chaîne de caractère de longueur n



Création de table :

On utilise la commande  **CREATE  TABLE**  de la manière suivante :

```sqlite
CREATE TABLE nom_de_ma_table  (   attribut1   domaine1  contrainte1 ,
                               attribut2   domaine 2  contrainte1 ,                
                               ………………………………....,
                               attribut_n   domaine_n  contrainte_n) ;
```

attribut = nom de la colonnes

domaine = type de valeur : CHAR(n) , VARCHAR(n) , INT , …

contrainte = PRIMARY KEY , REFERENCES une_table (attribut) ,  NOT NULL , … )

*Exemple :*

```sqlite
CREATE TABLE Livre(code_barre CHAR(15)   REFERENCES usager(code_barre),
					isbn CHAR(14)PRIMARY KEY ) ;
```

 à savoir que l ‘attribut *code_barre* est la clé primaire de la table *usager*.



Insertion dans une table :

```sqlite
INSERT INTO  nom_de_la_table      VALUES(valeur1,valeur2,…..) ;
```



## Mise en Pratique

La base de données *lycee* que vous utiliserez pour le tp est composée de 3 tables :

*eleve*  (id_eleve, nom, prenom)

*option*  (id_option, nom option)

*inscription*  (id_eleve, id_option)

- La table eleve contient l'id de l'élève qui est exprimé sur 4 chiffres ainsi que son nom et son prénom qui ont une longueur maximal de 28.	

- La table option contient l’id de l’option exprimé sur un chiffre et le nom de cette option.

- La table inscription contient l'id de l'élève et l'id de l’option dans laquelle il est inscrite .




1. Quelles sont les clés primaires de ces tables ?







2. Récupérer le fichier lycee.db 

3. Lancer sqlite3.exe

4. Importer la base de données *lycee* à l'aide de la commande **.open lycee.db**

5. Afficher les tables présente dans cette base de données à l'aide de la commande**.tables**

6. Créer la table *eleve*.

7. Ajoutez vous dans la table *eleve*.

8. Sauvegarder à l'aide de la commande **.save lycee.db**.

9. Afficher votre table à l’aide de la commande     **SELECT \* FROM eleve ;** 

10. Ajouter votre camarade  dans la table *eleve*.

11. Afficher de nouveau votre table.

12. Créer la table *inscription*.

13. Insérez vous dans la table *inscription*.

14. Afficher la table inscription.





2. Rajoutez l’ensemble de vos camarades dans la table *eleve* puis dans la table *inscription*