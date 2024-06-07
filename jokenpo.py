import json

def lambda_handler(event, context):
    try:
        # Log do evento recebido
        print(f"Evento recebido: {json.dumps(event)}")

        # Obtém os dados do corpo da requisição
        body = json.loads(event['body'])
        jogador1 = body['jogador1'].capitalize()
        jogador2 = body['jogador2'].capitalize()
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        # Log do erro
        print(f"Erro ao processar o corpo da requisição: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps('Erro: Parâmetros inválidos. Certifique-se de enviar um JSON com as chaves "jogador1" e "jogador2".')
        }

    # Converte as entradas para maiúsculas para validação e comparação
    jogador1 = jogador1.capitalize()
    jogador2 = jogador2.capitalize()

    # Valida as entradas dos jogadores
    opcoes_validas = ["Pedra", "Papel", "Tesoura"]
    if jogador1 not in opcoes_validas or jogador2 not in opcoes_validas:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro: Entrada inválida! Certifique-se de escolher entre Pedra, Papel ou Tesoura.')
        }

    # Determina o vencedor
    resultado = determinar_vencedor(jogador1, jogador2)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Resultado: {resultado}')
    }

def determinar_vencedor(jogador1, jogador2):
    regras = {
        "Pedra": {"Pedra": "Empate", "Tesoura": "Jogador 1 vence", "Papel": "Jogador 2 vence"},
        "Tesoura": {"Tesoura": "Empate", "Papel": "Jogador 1 vence", "Pedra": "Jogador 2 vence"},
        "Papel": {"Papel": "Empate", "Pedra": "Jogador 1 vence", "Tesoura": "Jogador 2 vence"}
    }
    return regras[jogador1][jogador2]
