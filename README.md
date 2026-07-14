Sistema de Monitoramento de Luminescência (IoT)

Nosso projeto é um Sistema de IoT que monitora, em tempo real, o nível de luminosidade de um ambiente, classificando as condições de luz e guardando um histórico das leituras.

Como funciona

Utilizamos um sensor de luminosidade (LDR) conectado a um Arduino, que mede a quantidade de luz do ambiente e transforma essa informação em um valor numérico. Esse valor é enviado do Arduino para o computador pela porta USB, e nosso programa em Python recebe essas leituras em tempo real.

A cada leitura, comparamos o valor recebido com faixas que definimos para classificar o ambiente:


Menor que 50: muito claro
Entre 50 e 300: ambiente ideal
Maior que 300: muito escuro


Definimos essas faixas dessa forma porque o sensor funciona de forma inversa à luz: quanto mais luz incide sobre ele, menor é o valor gerado; quanto menos luz, maior o valor. Por isso, valores baixos indicam ambiente claro e valores altos indicam ambiente escuro.

Cada leitura, junto com a data, hora e o status calculado, é salva em um banco de dados por nós, criando um histórico de como a luminosidade variou ao longo do tempo. Esse processo se repete automaticamente a cada segundo, permitindo o monitoramento contínuo do ambiente.

Tecnologias que utilizamos


Arduino
Python
Comunicação Serial
Banco de dados SQLite

Autores



Nicolas Pinheiro
