# Sistema Informativo do Espaço Livre em Disco

## Objetivo
Implementar uma solução mais prática para gerar um relatório do armazenamento dos sistemas operacionais em períodos pré definidos pelo sistema (inicio de expediente, almoço e final de expediente).

## Detalhes

- Versão do Python
    Python 3.12.0

## Processos do sistema

1. Obter o nome da máquina, pelo usuário.
2. Verificar se o horário é igual ao (inicio de expediente, almoço ou final de expediente).
3. Sendo verdadeira uma das opções cidatas, gera um arquivo (log_armazenamento.txt) informando: espaço livre do disco, registrando a data e hora em que foi analizada.
## Comandos Utilizados

1. Comando para atualizar a lista de bibliotecas utilizadas.

        pip freeze > requirements.txt

2. Comando para atualizar o arquivo .exe
        
        pyinstaller --onefile main.py

