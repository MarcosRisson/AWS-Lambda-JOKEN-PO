import json
import random

def lambda_handler(event, context):
    try:
        # Log do evento recebido
        print(f"Evento recebido: {json.dumps(event)}")

        # Obtém os dados do corpo da requisição
        body = json.loads(event['body'])
        jogador = body['jogador'].capitalize()
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        # Log do erro
        print(f"Erro ao processar o corpo da requisição: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps('Erro: Parâmetros inválidos. Certifique-se de enviar um JSON com a chave "jogador".')
        }

    # Valida a entrada do jogador
    opcoes_validas = ["Pedra", "Papel", "Tesoura"]
    if jogador not in opcoes_validas:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro: Entrada inválida! Certifique-se de escolher entre Pedra, Papel ou Tesoura.')
        }

    # Gera a escolha da máquina
    escolha_maquina = random.choice(opcoes_validas)

    # Determina o vencedor
    resultado = determinar_vencedor(jogador, escolha_maquina)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'jogador': jogador,
            'maquina': escolha_maquina,
            'resultado': resultado
        })
    }

def determinar_vencedor(jogador1, jogador2):
    regras = {
        "Pedra": {"Pedra": "Empate", "Tesoura": "Jogador 1 vence", "Papel": "Jogador 2 vence"},
        "Tesoura": {"Tesoura": "Empate", "Papel": "Jogador 1 vence", "Pedra": "Jogador 2 vence"},
        "Papel": {"Papel": "Empate", "Pedra": "Jogador 1 vence", "Tesoura": "Jogador 2 vence"}
    }
    return regras[jogador1][jogador2]
