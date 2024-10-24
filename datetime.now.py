from datetime import datetime

# Função que simula uma transação e registra a data e hora
def processar_transacao(id_transacao, valor):
    # Captura a data e hora atual
    momento_atual = datetime.now()
    
    # Formata a data e hora
    timestamp = momento_atual.strftime('%Y-%m-%d %H:%M:%S')
    
    # Simula o processamento da transação
    print(f"Transação {id_transacao} processada.")
    
    # Registra a transação no log com a data e hora
    with open('log_transacoes.txt', 'a') as arquivo_log:
        arquivo_log.write(f"{timestamp} - Transação {id_transacao}: R${valor:.2f}\n")

# Simulando algumas transações
processar_transacao(1001, 250.75)
processar_transacao(1002, 450.00)
processar_transacao(1003, 100.25)
