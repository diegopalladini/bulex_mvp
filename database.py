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
            (1, 'Losartana Potássica', 'Tratamento de pressão alta (hipertensão).', '1 comprimido de 50mg pela manhã.', 'Cuidado com tonturas ao levantar. Beba bastante água.'),
            (2, 'Amoxicilina', 'Tratamento de infecções bacterianas.', '1 cápsula de 500mg a cada 8 horas.', 'Atenção a reações alérgicas. Não suspenda antes de terminar.'),
            (3, 'Dipirona', 'Alívio de dores e febre.', '1 comprimido de 500mg a cada 6 horas.', 'Evite em caso de alergia. Máximo 4g por dia.'),
            (4, 'Metformina', 'Controle do diabetes tipo 2.', '1 comprimido de 500mg com as refeições (1-3x ao dia).', 'Pode causar enjoo. Não usar em caso de insuficiência renal.'),
            (5, 'Atenolol', 'Tratamento de pressão alta e problemas cardíacos.', '1 comprimido de 50mg pela manhã.', 'Não pare o tratamento abruptamente. Pode causar falta de ar.'),
            (6, 'Sinvastatina', 'Redução de colesterol no sangue.', '1 comprimido de 20mg à noite.', 'Evite álcool em excesso. Dor muscular requer avaliação.'),
            (7, 'Omeprazol', 'Proteção do estômago e refluxo gástrico.', '1 cápsula de 20mg pela manhã, antes das refeições.', 'Tomar 30 minutos antes da primeira refeição.'),
            (8, 'Paracetamol', 'Alívio de dor e febre.', '1 comprimido de 500mg a cada 6 horas.', 'Máximo 4g por dia. Cuidado com overdose.'),
            (9, 'Tramadol', 'Alívio de dor moderada a intensa.', '1 comprimido de 50mg a cada 6-8 horas conforme necessário.', 'Pode causar sonolência. Não dirija após tomar.'),
            (10, 'Ranitidina', 'Redução de ácido estomacal (esofagite/úlcera).', '1 comprimido de 150mg de 12 em 12 horas.', 'Tome 30 minutos antes das refeições. Evite alimentos gordurosos.')
        ]
        cursor.executemany('INSERT OR REPLACE INTO medicamentos VALUES (?,?,?,?,?)', medicamentos_iniciais)
        conn.commit()
        print("Banco de dados 'bulex.db' criado com sucesso!")

if __name__ == "__main__":
    iniciar_banco()