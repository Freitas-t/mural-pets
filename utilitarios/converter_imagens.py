from PIL import Image
import pillow_heif
import os

pillow_heif.register_heif_opener()

PASTA = "images"
EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png", ".heic", ".webp")

for arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, arquivo)

    if not os.path.isfile(caminho):
        continue

    if not arquivo.lower().endswith(EXTENSOES_VALIDAS):
        continue

    nome_base, ext = os.path.splitext(arquivo)
    ext = ext.lower()

    # Se já for .jpg, ignora
    if ext == ".jpeg":
        continue

    try:
        with Image.open(caminho) as img:
            img = img.convert("RGB")
            novo_caminho = os.path.join(PASTA, f"{nome_base}.jpeg")

            img.save(novo_caminho, "JPEG", quality=90, optimize=True)

        os.remove(caminho)
        print(f"Convertido: {arquivo} → {nome_base}.jpeg")

    except Exception as e:
        print(f"Erro em {arquivo}: {e}")
