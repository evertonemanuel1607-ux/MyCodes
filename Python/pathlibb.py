from pathlib import Path 

caminho_arquivo = Path(__file__)
caminho_documents = caminho_arquivo.parent.parent.parent

caminho_nova_pasta = caminho_documents / 'pasta'
caminho_nova_pasta.mkdir(exist_ok=True)

caminho_novo_arquivo = caminho_nova_pasta / 'nota.txt'
caminho_novo_arquivo.touch()

caminho_novo_arquivo.unlink()