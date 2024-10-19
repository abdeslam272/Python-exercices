import sqlite3

# Connexion à la base de données
conn = sqlite3.connect(r'C:\Users\Abdo\Desktop\Mes Stages & Mes Projets\Mes Projets\Developpement Python\dim_customer.sqlite')
cursor = conn.cursor()

# Lire le contenu de la table 'dim_customers'
cursor.execute("SELECT * FROM dim_customers")
rows = cursor.fetchall()

print("Contenu de la table 'dim_customers' :")
for row in rows:
    print(row)

conn.close()
