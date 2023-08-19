# DATA Splitter
### Le code pour diviser les données accomplit les actions suivantes :

 - Il démarre en important les bibliothèques nécessaires pour manipuler les données (pandas) et interagir avec une base de données SQL Server en utilisant l'ORM SQLAlchemy.
 - Il charge un fichier CSV, le mélange et renomme les colonnes.
 - L'utilisateur sélectionne des proportions pour trois formats : JSON, CSV et la base de données SQL Server.
 - Les données sont séparées en parties conformément aux proportions choisies.
 - Les parties de données destinées au format JSON sont sauvegardées dans un fichier JSON.
 - Les parties destinées au format CSV sont sauvegardées dans un fichier CSV.
 - Les données sont préparées pour être insérées dans une table SQL.
 - Une table est créée de manière dynamique dans la base de données SQL Server en utilisant l'ORM SQLAlchemy, s'adaptant aux types de données.
 - Les données sont insérées dans la table de manière dynamique en utilisant les fonctionnalités de l'ORM SQLAlchemy, ce qui permet une insertion flexible en s'ajustant aux changements de structure.
#
En résumé, ce code prend des données CSV, les répartit dans divers formats, les stocke en fichiers JSON et CSV, puis les organise et les insère dans une base de données SQL Server. L'utilisation de l'ORM SQLAlchemy facilite la création dynamique de la table et l'insertion flexible des données, rendant le processus adaptable et évolutif.
