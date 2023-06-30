import mysql.connector
try:
    conexao = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'pychat',
        'raise_on_warnings': True
        }
    conn = mysql.connector.connect(**conexao)
    print('conexão bem sucedida ao Pychat')
    class Pychat:
        def __init__(self,cursor='',nome=''):
            self.cursor = conn.cursor()
            self.nome = ''
        def Nome(self):
            nome = str(input('Digite seu nome: '))
            if nome == '':
                self.nome = 'DEFAULT'
            else:
                self.nome = nome
        def Chat(self):
            on = True
            while on == True:
                print('\n' * 50)
                print('-' * 100)
                self.cursor.execute("SELECT * FROM chat")
                chat = self.cursor.fetchall()
                for textos in chat:
                    print(f'{textos[0]} : {textos[1]}')
                print('-' * 100)
                write = input('> ')
                atualizar = f"""
                INSERT INTO chat
                VALUES('{self.nome}','{write}');
                    """
                self.cursor.execute(atualizar)
                conn.commit()
except mysql.connector.Error as erro:
    print('Falha Na Conexão:',erro)