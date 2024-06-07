## Documentação da Função Lambda - JokenPo

## Descrição
Esta função Lambda implementa o jogo "Pedra, Papel, Tesoura". A função recebe como entrada da escolha de um jogador,e a funçao determina a jogada do segundo jogador e valida quem sera o vencedor e retorna o resultado.

## Funcionalidade
Recebe uma requisição HTTP POST com um corpo JSON contendo as escolha do dois jogadores (jogador1 e maquina).
As escolhas são comparadas para determinar o vencedor com base nas regras tradicionais do jogo.
Retorna o resultado do jogo, indicando se foi um empate ou qual jogador venceu.

## Entrada Esperada
- A função espera uma requisição HTTP POST com um corpo JSON contendo a chave jogador , cujo valor são as escolhas dos jogador. As escolhas devem ser strings representando "Pedra", "Papel" ou "Tesoura" (insensíveis a maiúsculas e minúsculas).
- A Solicitaçao pode ser feita no EndPoint da AWS https://uoq7j4gppoe4hm3zw7ekoraf5y0vwish.lambda-url.us-east-1.on.aws/


### Exemplo de corpo da requisição:

 ``` json 
{
    "jogador": "pedra"
}
``` 

### Exemplo de Resultado: 

```json
{
    "jogador": "Pedra",
    "maquina": "Papel",
    "resultado": "Jogador 2 vence"
}
```



