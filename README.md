# Conversor de Moedas

## Descrição
Este projeto é um simples conversor de moedas que utiliza a API do FreeCurrencyAPI para converter valores entre diferentes moedas. O programa permite que o usuário escolha uma moeda base e exibe as taxas de câmbio para outras moedas pré-definidas.

## Funcionalidades
- Conversão de moedas em tempo real usando a API FreeCurrencyAPI.
- Suporte para as moedas: USD, CAD, EUR, AUD, CNY e BRL.
- Interface de linha de comando interativa.
- Possibilidade de sair do programa digitando "s".

## Requisitos
- Python 3.x
- Biblioteca `requests` (instale com `pip install requests`)
- Chave de API válida do FreeCurrencyAPI (obtenha em [freecurrencyapi.com](https://freecurrencyapi.com/))

## Como Usar
1. Clone o repositório ou copie o código para um arquivo (ex.: `currency_converter.py`).
2. Instale a biblioteca necessária:
   ```bash
   pip install requests
   ```
3. Substitua a variável `API_KEY` no código pela sua chave de API do FreeCurrencyAPI.
4. Execute o programa:
   ```bash
   python currency_converter.py
   ```
5. Insira a moeda base (ex.: `USD`, `BRL`) ou digite `s` para sair.
6. O programa exibirá as taxas de câmbio para as moedas disponíveis em relação à moeda base escolhida.

## Exemplo de Uso
```plaintext
Insira a moeda base (s para sair): USD
CAD: 1.3598
EUR: 0.9215
AUD: 1.5032
CNY: 7.2461
BRL: 5.1567
Insira a moeda base (s para sair): s
```

## Estrutura do Código
- **API_KEY**: Chave da API para autenticação.
- **BASE_URL**: URL base da API com a chave de autenticação.
- **CURRENCIES**: Lista de moedas suportadas.
- **convert_currency(base)**: Função que faz a requisição à API e retorna as taxas de câmbio.
- **Loop principal**: Solicita a moeda base do usuário e exibe as taxas de câmbio.

## Notas
- Certifique-se de ter uma conexão com a internet para que as requisições à API funcionem.
- Caso a moeda inserida não seja válida, o programa exibirá uma mensagem de erro e permitirá nova tentativa.
- A API utilizada possui limites de uso na versão gratuita. Consulte o site do FreeCurrencyAPI para mais detalhes.

## Licença
Este projeto é de código aberto e pode ser usado sob a licença MIT.
