import sqlite3
from datetime import datetime

BANCO = "sensores.db"

def conectar():
    return sqlite3.connect(BANCO)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS luminosidade (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        valor INTEGER,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def salvar_leitura(valor, status):
    conn = conectar()
    cursor = conn.cursor()

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cursor.execute("""
    INSERT INTO luminosidade (data, valor, status)
    VALUES (?, ?, ?)
    """, (data, valor, status))

    conn.commit()
    conn.close()
'''def buscar_leituras():
    conn = conectar()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT * FROM luminosidade
    """)

    leituras = cursor.fetchall()
    conn.commit()
    conn.close()
    return leituras

buscar_leituras()'''