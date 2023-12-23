'''Arquivo principal para execução do programa'''

from psutil import disk_usage
from datetime import datetime
from time import sleep


# Transforma o valor de Byte em Gigabyte
def byte_by_gigabyte(tamnho_byte: int) -> float:
    return tamnho_byte / 1024 / 1024 / 1024


# Obtem informações do espaço livre da máquina
def set_informações_do_sistema() -> float:
    # Obtem a a quantidade de espaço livre no disco rígido da máquina
    disco = disk_usage('/').free
    # Trasformar byte para gigabyte
    espaco_livre = byte_by_gigabyte(disco)
    return espaco_livre


# Mostra as informações do sistema formatado
def get_informacoes_sistema(nome_da_maquina: str) -> str:
    # Informa a data e hora atual
    HORA_DATA = datetime.now().strftime("%d/%m/%Y - %H:%M:%S") # Data e hora do local

    INFO_SISTEMA = set_informações_do_sistema()

    # Envia a informação para o aquivo 'log_armazenamento.txt'
    MENSAGEM = f'Nome da máquina: {nome_da_maquina}; Espaço livre: {INFO_SISTEMA:.2f}GB; Ultima atualização: {HORA_DATA}\n'
    # Escreve o arquivo no caminho especificado
    return MENSAGEM


# Escreve no arquivo sem sobescrever nele pulando uma linha
def criar_arquivo(mensagem: str, caminho_do_arquivo: str):
    with open(file=caminho_do_arquivo, mode='a', encoding='utf-8') as file:
        try:
            file.writelines(mensagem)
        except FileExistsError as er:
            file.writelines(f'Erro 003 >>> Problema pra encontrar aquivo \n{er}')
        except PermissionError as er:
            file.writelines(f'Erro 005 >>> Problema na permisão de gravação \n{er}')
        except OSError as er:
            file.writelines(f'Erro 001 >>> O arquivo não pode ser aberto: \n{er}')
        except ValueError as er:
            file.writelines(f'Erro 002 >>> Existem algum valor que não bate... \n{er}')
        except Exception as e:
            file.writelines(f'Deu pau! =( >>> Erro desconhecido: \n{e}')
        finally:
            sleep(1) # Permitir que escreva somente uma vez no arquivo
            file.close()
        

def get_hota_atual() -> str:
    return datetime.now().strftime("%H:%M:%S")


# Função principal
def main(hora_final: str, hora_do_meio_dia: str, hora_inicial: str, caminho_da_pasta: str, nome_da_maquina: str):
    while True:
        if (get_hota_atual() == hora_inicial or 
            get_hota_atual() == hora_do_meio_dia or 
            get_hota_atual() == hora_final):
            MENSAGEM = get_informacoes_sistema(nome_da_maquina=nome_da_maquina)
            criar_arquivo(mensagem=MENSAGEM,
                          caminho_do_arquivo=caminho_da_pasta)


if __name__ == '__main__':
    # Instâncias principais
    HORA_FINAL = '17:58:00'
    HORA_MEIO_DIA = '12:01:00'
    HORA_DO_DIA = '07:50:00'

    # Informar o nome da máquina que será analizada
    NOME_DA_MAQUINA = input("Digite o nome da máquina que será analisada: ")
    CAMINHO_DA_PASTA = input('Informe o caminho do arquivo: ') + "\\log_armazenamento.txt"
    main(hora_final=HORA_FINAL, 
        hora_do_meio_dia=HORA_MEIO_DIA, 
        hora_inicial=HORA_DO_DIA, 
        caminho_da_pasta=CAMINHO_DA_PASTA,
        nome_da_maquina=NOME_DA_MAQUINA)
