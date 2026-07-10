import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sensores.db")

cursor = conn.cursor()

cursor.execute("""
SELECT valor
FROM luminosidade
ORDER BY id
""")

dados = cursor.fetchall()

print(dados)

conn.close()