from PIL import Image
import pillow_heif
import os

pillow_heif.register_heif_opener()

PASTA = "images"

for arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, arquivo)

    if not os.path.isfile(caminho):
        continue

    try:
        with Image.open(caminho) as img:
            img = img.convert("RGB")

            nome_base = os.path.splitext(arquivo)[0]
            novo_caminho = os.path.join(PASTA, f"{nome_base}.jpg")

            img.save(novo_caminho, "JPEG", quality=90, optimize=True)

            if not arquivo.lower().endswith(".jpg"):
                os.remove(caminho)

            print(f"Convertido: {arquivo} → {nome_base}.jpg")

    except Exception as e:
        print(f"Erro em {arquivo}: {e}")
