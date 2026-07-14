# Sistema IoT de Monitoramento de Luminosidade

Sistema simples de IoT que lê dados de um sensor de luminosidade conectado a um Arduino via porta serial, classifica o ambiente (muito escuro, muito claro ou ideal) e armazena as leituras em um banco de dados SQLite.

## Funcionalidades

- Leitura contínua de um sensor de luminosidade via comunicação serial (Arduino)
- Classificação automática do ambiente com base no valor lido:
  - **Muito escuro!** → luminosidade > 600
  - **Muito claro!** → luminosidade < 160
  - **Ambiente Ideal!** → entre 160 e 600
- Registro de cada leitura (data/hora, valor e status) em banco de dados SQLite
- Exibição em tempo real das leituras no terminal

## Estrutura do projeto

```
.
├── main.py         # Loop principal: lê o sensor, classifica e salva os dados
├── serial_io.py    # Comunicação serial com o Arduino
├── banco.py        # Criação da tabela e persistência dos dados (SQLite)
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.14+
- Arduino (ou placa compatível) com sensor de luminosidade (ex.: LDR) conectado, enviando o valor lido pela porta serial em cada linha
- Biblioteca [`pyserial`](https://pypi.org/project/pyserial/)

### requirements.txt

```
pyserial
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd SistemaIot
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

No arquivo `serial_io.py`, ajuste a porta serial e a taxa de transmissão de acordo com o seu ambiente:

```python
PORTA = "COM5"   # ex.: "COM5" no Windows ou "/dev/ttyUSB0" no Linux
BAUD = 9600
```

O Arduino deve enviar, a cada leitura, apenas o valor numérico do sensor seguido de quebra de linha (`Serial.println(valor);`).

## Uso

Com o Arduino conectado e a porta serial configurada, execute:

```bash
python main.py
```

O sistema irá:
1. Criar automaticamente a tabela `luminosidade` no banco `sensores.db` (caso ainda não exista)
2. Ler continuamente os valores do sensor
3. Classificar e salvar cada leitura no banco
4. Exibir no terminal a luminosidade e o status correspondente

Para encerrar, pressione `Ctrl+C`.

## Banco de dados

As leituras são armazenadas na tabela `luminosidade`, dentro do arquivo `sensores.db` (SQLite), com a seguinte estrutura:

| Coluna | Tipo    | Descrição                          |
|--------|---------|-------------------------------------|
| id     | INTEGER | Identificador único (auto-incremento) |
| data   | TEXT    | Data e hora da leitura (`dd/mm/aaaa hh:mm:ss`) |
| valor  | INTEGER | Valor lido do sensor                |
| status | TEXT    | Classificação do ambiente           |

## Melhorias futuras

- [ ] Tratamento de erros na comunicação serial (porta indisponível, timeout, etc.)
- [ ] Configuração via arquivo `.env` ou argumentos de linha de comando
- [ ] Dashboard web para visualização das leituras
- [ ] Testes automatizados

## Licença

Defina aqui a licença do projeto (ex.: MIT).
