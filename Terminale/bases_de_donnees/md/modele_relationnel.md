# Modèle relationnel

## Définitions

Une **relation** est considérée comme un tableau à 2 dimensions. Elle contient des colonnes et des lignes. Il s'agit donc d'un groupe d'informations relatives à un sujet.

Les **attributs** de la relation correspondent aux colonnes du tableau. 

Un **enregistrement** est un p-uplet mettant en relation les attributs. C'est donc une des lignes du tableau. 

Chaque case est une **entrée**, aussi appelé **valeur**.



*Exemple :*

Voici un tableau à deux dimensions représentant la relation appelée *Artistes*.

| id_artiste | prenom   | nom              | pseudonyme      | date_de_naissance |
| ---------- | -------- | ---------------- | --------------- | ----------------- |
| 1          | Aurélien | Cotentin         | Orelsan         | 01/08/1982        |
| 2          | William  | Kalubi Mwamba    | Damso           | 10/05/1992        |
| 3          | Julien   | Schwarzer        | SCH             | 06/04/1993        |
| 4          | Issa     | Lorenzo Diakhaté | Freeze Corleone | 06/06/1992        |

1. Quels sont les attributs de cette relation?



2. Donner le premier enregistrement.



3. Donner la dernière entrée de cette relation.





Chaque attribut est associé à un **domaine**, c'est l'ensemble de valeurs que peut prendre une donnée. Le domaine est en quelque sorte un équivalent du type en python.

Par exemple, un **domaine** peut être :

- L'ensemble des entiers (INT)
- L'ensemble des nombres flottants (FLOAT)
- Les chaines de caractères (TEXT) 
- Les dates (DATE)
- Les booléens (BOOL)
- etc 

Dans notre exemple :

- Les attributs pseudonyme, nom et prenom sont des chaînes de caractères, on dit alors qu'ils sont associés au domaine TEXT.

- Le domaine de l'attribut date_de_naissance est DATE.

- Le domaine de l'attribut id_artiste est INT.

Sur les domaines, une contrainte se pose, la **contrainte de Domaine** : seules les valeurs présentent dans le domaine sont utilisables.

## Clé primaire

Dans une relation, une **clé primaire** (Primary Key) identifie de manière unique un enregistrement d'une relation. Elle ne peut être vide (NULL). Elle peut être composée d'un ou plusieurs attributs.

4. Dans la relation *Artistes* vue plus haut, quel attribut peut être une clé primaire ?



5. Peut-on choisir une autre clé primaire ? Justifier.





*Remarque :*

Dans certaines relations, les attributs ne permettent pas choisir une clé primaire appropriée, en cas d'homonymes par exemple. On ajoute alors à la relation une colonne dédiée qui sera la clé primaire avec un simple numéro, un identifiant souvent appelé **id**  qui fera une clé primaire simple et fiable.

L'existence d'une clé primaire est une **contrainte d'entité** qui permet de vérifier qu'il n'existe pas deux enregistrements identiques dans la base. Ce qui est interdit comme nous l'avons déjà dit. 

## Base de données relationnelle

Une base de données est constituée d'un ensemble de relations (donc de plusieurs tables).

Reprenons notre exemple, on peux ajouter à notre base de données, la relation suivante, que nous appellerons *Albums*.

| id_album | titre                | id_artiste | date_de_sortie | label                 |
| -------- | -------------------- | ---------- | -------------- | --------------------- |
| 1        | Ipséité              | 2          | 28/04/2017     | Capitol               |
| 2        | La fête est finie    | 1          | 20/10/2017     | Wagram                |
| 3        | Rooftop              | 3          | 29/11/2019     | Maison Baron Rouge    |
| 4        | Le chant des sirènes | 1          | 05/05/2011     | Wagram                |
| 5        | FDT                  | 4          | 11/09/2016     | M.M.S Records         |
| 6        | Anarchie             | 3          | 27/05/2016     | Braabus               |
| 7        | Batterie faible      | 2          | 08/07/2016     | Universal             |
| 8        | JVLIVS II            | 3          | 19/03/2021     | Warner                |
| 9        | Perdu d'avance       | 1          | 16/02/2009     | Wagram                |
| 10       | QALF                 | 2          | 18/12/2020     | Universal             |
| 11       | Deo Favente          | 3          | 05/05/2017     | Capitol               |
| 12       | Projet Blue Beam     | 4          | 13/11/2018     | M.M.S Records         |
| 13       | Civilisation         | 1          | 19/11/2021     | Wagram                |
| 14       | A7                   | 3          | 13/11/2015     | Braabus               |
| 15       | LMF                  | 4          | 11/09/2020     | M.M.S Records         |
| 16       | Lithopédion          | 2          | 15/06/2018     | Universal             |
| 17       | Projet Purrp Beam    | 4          | 25/11/2019     | CJusteRalenti Records |
| 18       | JVLIVS               | 3          | 19/10/2018     | Maison Baron Rouge    |

6. Quels sont les attributs de cette relation ? 



7. Donner le cinquième enregistrement de la relation Albums.



8. Donner une entrée.



9. Donner un attribut ou un groupe d'attributs pouvant constituer une clé primaire pour cette relation.





La base peut contenir plus de deux relations bien entendu. Voici, par exemple, une autre relation que nous appellerons *Chansons* :

| titre                | id_artiste | id_album | numero | annee_de_sortie |
| -------------------- | ---------- | -------- | ------ | --------------- |
| Freeze Raël          | 4          | 15       | 1      | 2020            |
| 911                  | 2          | 10       | 11     | 2020            |
| Mannschaft           | 3          | 8        | 5      | 2021            |
| L'odeur de l'essence | 1          | 13       | 8      | 2021            |

*Remarque :*

C'est le fait d'avoir plusieurs tables qui rend inutile de stipuler, pour chaque album, quel est la date de création de son label par exemple.  **Définir plusieurs tables évite donc la redondance des valeurs et des colonnes et optimise ainsi la base de données.**

10. Quels attributs de la relation peuvent être obtenues à partir d'une autre relation ? 



Par la suite, nous allons donc supprimer cet attribut !

Il faut maintenant créer un lien entre nos relations.

## Clé étrangère

Pour établir un lien entre 2 relations $R_A$ et $R_B$, on ajoute à $R_A$ un attribut x qui prendra les valeurs de la clé primaire de $R_B$. Cet attribut x est appelé clef étrangère (l'attribut correspond à la clé primaire d'une autre table, d'où le nom).

Dans l'exemple ci-dessus, l'attribut "id_album" de la relation *Chansons* permet bien d'établir un lien entre la relation *Chansons* et la relation *Albums*, conclusion : "id_album" est une clé étrangère.

Une clé étrangère est une **contrainte d'intégrité** qui permet de garder une cohérence entre les deux relations :

- Ces valeurs doivent pré-exister dans la relation à laquelle elle fait référence : on ne peut pas ajouter à la clé étrangère une valeur qui n'est pas présente parmi les valeurs de la clé primaire de l'autre relation.
- On ne peut pas supprimer une valeur d'une clé primaire qui est référencée dans une clé étrangère.

Dans notre exemple, impossible d'enregistrer un album de JUL ou de supprimer l'album Civilisation de la relation *Albums*.

Il nous faut déterminer un attribut (ou groupe d'attribut) qui constitue une clé étrangère de la relation *Chansons* vers la relation *Albums*.

Pour rappel, la relation *Chansons* a été modifiée et se trouve être celle-ci :

| titre                | id_album | numero |
| -------------------- | -------- | ------ |
| Freeze Raël          | 15       | 1      |
| 911                  | 10       | 11     |
| Mannschaft           | 8        | 5      |
| L'odeur de l'essence | 13       | 8      |

11. A quelles possibles clés primaires de la relation *Albums* la relation *Chansons* ne peut en aucun cas faire référence ?



12. Quelle clé primaire doit-on alors impérativement choisir pour la relation *Albums* ?



13. Quelle est la clé étrangère de la relation *Chansons* qui référence cette clé primaire ? 



## Autres contraintes

Nous avons vu que la clé primaire imposait une **contrainte d'unicité** et la clé étrangère une **contrainte d'intégrité**. Il existe d'autre type de contraintes, par exemple :

- Une bonne pratique consiste à interdire qu'un attribut ne pas pas être nul (NULL). Cette contrainte de non nullité se fait au moyen du mot clé **NOT NULL**.

- Il arrive parfois qu'un attribut, bien qu'il ne soit pas une clé primaire, doivent être unique. Il est possible de forcer cette unicité sans utiliser l'attribut comme clé primaire.

- On peut définir des **contraintes de domaine** en réduisant le domaine. Par exemple, un attribut entier peut voir sa plage réduite à un chiffre. Cela se fait lors de la requête pur créer la table ou en modifiant une table déjà existante.

  

## Schéma relationnel

Un **schéma de relation** d'une relation en précise le nom, les attributs et leurs domaines, la clé primaire et, éventuellement , la clé étrangère.

Ainsi, le schéma de relation de *Chansons* est :

Chansons(<u>titre</u> : TEXT, <u>numero</u> : INT,#id_album : INT)

14. Donner le schéma de relation de la relation *Artistes*.

```txt
```

15. Donner le schéma de relation de la relation *Albums*.

```python
```

On appelle **schéma relationnel** l'ensemble de tous les schémas de relation d'une base de donnée.

16. Donner le schéma relationnel de notre base, constituée des relations *Artistes*, *Chansons* et *Albums*.

```txt




```



## Exercices

*Difficulté 1*

**Exercice 1 :**

Associer chaque terme du modèle à sa description.

Clé étrangère                                       p-uplet mettant en relation les attributs.

Clé primaire										 Fait "référence" à un élément.

Domaine                                               Ensemble de valeurs possibles.

Enregistrement                                    Identifie de façon unique chaque élément.



**Exercice 2 :**

Soit la table suivante :

| id_voiture | marque  | modele | kilométrage | couleur |
| ---------- | ------- | ------ | ----------- | ------- |
| 1          | Renault | Clio   | 12000       | Rouge   |
| 2          | Peugeot | 205    | 22000       | Noir    |
| 3          | Toyota  | Yaris  | 33000       | Noir    |

1. Combien d'attributs comporte cette table ? 

   

2. Quel est le domaine de l'attribut kilométrage ?



3. Donner un attribut ou un groupe d'attributs pouvant constituer une clé primaire pour cette relation.



4. Donner le schéma de relation de la table.





**Exercice 3 :**

Une sandwicherie effectuant des livraisons à domicile dispose d'une base de données dont certains extraits de tables sont reproduits ci-dessous. 

La table *Sandwichs* :

| nom_sandwich  | prix  |
| ------------- | ----- |
| Cheeseburger  | 3,90  |
| Double cheese | 4,90  |
| Italien       | 4,90  |
| Foie gras     | 15,00 |

La table *Clients* :

| nom     | prenom | adresse                          | numero_client |
| ------- | ------ | -------------------------------- | ------------- |
| Bernard | Alain  | 9, rue Bienvenu, 13008 Marseille | 42            |
| Bernard | Yves   | 2, rue Lafayette, 13400 Aubagne  | 51            |

La tables *Commandes* :

| numero_client | nom_sandwich | quantite | numero_commande | date       |
| ------------- | ------------ | -------- | --------------- | ---------- |
| 42            | Italien      | 2        | 12452           | 11/12/2019 |
| 42            | Foie gras    | 1        | 12452           | 11/12/2019 |
| 51            | Cheeseburger | 4        | 13301           | 23/12/2019 |

1. Une commande peut-elle comporter plusieurs sandwichs de types différents ? 



2. Quel attribut ou groupe d'attribut peut constituer une clé primaire pour la table *Sandwichs* ? 



3. Quels attributs ou groupe d'attribut sont des clés étrangères dans la table *Commandes* ?



4. Quel est le schéma de relation de cette base de données ?





5. Cette base de données semble-t-elle bien modélisée ? Si ce n'est pas le cas, proposer une modification.









*Difficulté 2*

**Exercice 4 :**

On souhaite modéliser un annuaire téléphonique simple dans lequel chaque personne (identifiée par son nom et son prénom) est associée à son numéro de téléphone . Proposer un schéma de relation de cet annuaire.





**Exercice 5 :**

Donner la modélisation relationnelle d'un bulletin scolaire. Cette dernière doit permettre de mentionner :

- Des élèves, possédants un numéro d'étudiant alphanumérique unique.
- Un ensemble de matière fixées, mais qui ne sont pas données.
- Au plus une note sur 20, par matière et par élève.













