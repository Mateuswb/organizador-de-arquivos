from organizador import OrganizadorArquivos
from tipos_arquivos import tipos
import os

def organizar_pasta(pasta):
    if not pasta:
        print("Informe o caminho da pasta!")
        return
    if not os.path.exists(pasta):
        print("Caminho informado não existe!")
        return

    organizador = OrganizadorArquivos(pasta, tipos)
    organizador.criar_pastas()
    organizador.organizar_arquivos()
    print("Arquivos organizados com sucesso!")


if __name__ == "__main__":
    caminho = input("Informe o caminho da pasta que deseja organizar: ")
    organizar_pasta(caminho)
