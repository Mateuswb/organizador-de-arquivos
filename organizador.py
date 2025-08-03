from pathlib import Path
import shutil

class OrganizadorArquivos:
    def __init__(self, caminho, tipos_arquivos):
        self.caminho = Path(caminho)
        self.tipos = tipos_arquivos
        self.ext_para_categoria = {
            ext: categoria
            for categoria, extensoes in tipos_arquivos.items()
            for ext in extensoes
        }

    def criar_pastas(self):
        for pasta in self.tipos:
            (self.caminho / pasta).mkdir(exist_ok=True)
        (self.caminho / "Outros").mkdir(exist_ok=True)

    def organizar_arquivos(self):
        arquivos = [f for f in self.caminho.iterdir() if f.is_file()]
        for arquivo in arquivos:
            categoria = self.ext_para_categoria.get(arquivo.suffix.lower())
            destino = (
                self.caminho / categoria / arquivo.name
                if categoria else self.caminho / "Outros" / arquivo.name
            )

            try:
                shutil.move(str(arquivo), str(destino))
                print(f'Movido: {arquivo.name} → {destino.parent.name}')
            except Exception as e:
                print(f'Erro ao mover {arquivo.name}: {e}')
