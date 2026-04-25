import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bulex.db')

def iniciar_banco():
    with sqlite3.connect(DB_PATH) as conn:  # <-- caminho absoluto
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicamentos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                finalidade TEXT,
                como_tomar TEXT,
                alerta TEXT
            )
        ''')
        medicamentos_iniciais = [
            (1, 'Losartana Potássica', 'Tratamento de pressão alta.', '1 comprimido pela manhã.', 'Cuidado com tonturas ao levantar.'),
            (2, 'Amoxicilina', 'Tratamento de infecções.', '1 cápsula a cada 8 horas.', 'Atenção a manchas vermelhas na pele.'),
            (3, 'Dipirona', 'Dores de cabeça e cefaléias.', '1 cápsula a cada 6 horas.', 'Atenção a alergias.')
        ]
        cursor.executemany('INSERT OR REPLACE INTO medicamentos VALUES (?,?,?,?,?)', medicamentos_iniciais)
        conn.commit()
        print("Banco de dados 'bulex.db' criado com sucesso!")

if __name__ == "__main__":
    iniciar_banco()