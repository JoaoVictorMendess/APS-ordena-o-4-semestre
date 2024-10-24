# pip install mysql-connector-python (Para instalar a biblioteca)

import mysql.connector


# Função para conectar ao banco de dados
def conectar_banco():
    conexao = mysql.connector.connect(
        host="", # Qualquer um (localhost por exemplo)
        user="",  # Mesma coisa que o host (root por exemplo)
        password="",  # Senha do banco
        database="faculdade"  # Nome do banco de dados
    )
    return conexao


# Função para criar uma tabela no banco de dados
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            idade INT,
            curso VARCHAR(255)
        )
    """)
    conexao.commit()
    print("Tabela 'estudantes' criada com sucesso!")


# Função para inserir dados na tabela
def inserir_dados(conexao, nome, idade, curso):
    cursor = conexao.cursor()
    sql = "INSERT INTO estudantes (nome, idade, curso) VALUES (%s, %s, %s)"
    valores = (nome, idade, curso)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Dados inseridos: {nome}, {idade}, {curso}")


# Função para consultar dados da tabela
def buscar_dados(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM estudantes")
    resultado = cursor.fetchall()
    print("Dados na tabela 'estudantes':")
    for linha in resultado:
        print(linha)


# Função para atualizar dados
def atualizar_dados(conexao, estudante_id, novo_curso):
    cursor = conexao.cursor()
    sql = "UPDATE estudantes SET curso = %s WHERE id = %s"
    valores = (novo_curso, estudante_id)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Dados atualizados para o estudante com ID {estudante_id}: Novo curso: {novo_curso}")


# Função para deletar dados
def deletar_dados(conexao, estudante_id):
    cursor = conexao.cursor()
    sql = "DELETE FROM estudantes WHERE id = %s"
    valores = (estudante_id,)
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"Estudante com ID {estudante_id} deletado.")


# Função que executa as operações
def main():
    # Conexão com o banco de dados
    conexao = conectar_banco()

    # Cria a tabela (pprt se n for óbvio tá tirando)
    criar_tabela(conexao)

    # Insere os dados (...)
    inserir_dados(conexao, "João", 20, "Engenharia")
    inserir_dados(conexao, "Maria", 22, "Medicina")

    # Busca os dados (.....)
    buscar_dados(conexao)

    # Atualiza os dados (.......)
    atualizar_dados(conexao, 1, "Engenharia de Software")

    # Busca os dados de novo mais uma vez novamente
    buscar_dados(conexao)

    # Deleta os dados (:DDD)
    deletar_dados(conexao, 2)

    # Busca os dados novamente para verificar o delete
    buscar_dados(conexao)

    # Fecha a conexão
    conexao.close()


# Executa o programa
if __name__ == "__main__":
    main()

