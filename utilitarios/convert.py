from PIL import Image
import os

PASTA = r"C:\Users\thall\mural-pets\assets\icons"

for arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, arquivo)

    if not os.path.isfile(caminho):
        continue

    nome, ext = os.path.splitext(arquivo)

    # ignora arquivos que já são PNG
    if ext.lower() == ".png":
        continue

    try:
        with Image.open(caminho) as img:
            # mantém transparência se existir
            if img.mode in ("RGBA", "LA"):
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")

            novo_caminho = os.path.join(PASTA, f"{nome}.png")
            img.save(novo_caminho, "PNG", optimize=True)

            print(f"Convertido: {arquivo} → {nome}.png")

    except Exception as e:
        print(f"Erro em {arquivo}: {e}")
