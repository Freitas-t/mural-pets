import pandas as pd

df = pd.read_excel("SBCD_PETS.xlsx")

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Mural de Pets</title>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-K5CLWCVJCB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-K5CLWCVJCB');
</script>
<style>
h1 {
    text-align: center;
    font-size: 50px;
}

body {
    font-family: Helvetica, sans-serif;
    background: #ffcd00;
    background-image: url("assets/icons/patinha.png");
    background-repeat: repeat;
    background-size: 80px;
    background-position: 20px 30px;
    margin: 0;
    padding: 20px;
}

.mural {
    max-width: 1200px;
    margin: 0 auto;
}

.pet-card {
    background: #1c4482;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    text-align: center;
}

.pet-card h2 {
    margin: 0;
    margin-bottom: 6px;
    font-size: 20px;
    color: #f5f2d0
}

.pet-card p {
    margin: 6px 0 14px 0;
    color: white;
}

.fotos {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
}

.fotos img {
    height: 180px;
    width: auto;
    border-radius: 10px;
    object-fit: cover;
}

.topo {
    position: relative;
    height: 100px;
    margin-bottom: 40px;
    z-index: 1;
}

img.logo {
    position: absolute;
    top: 0;
    height: 80px;
    width: auto;
}

img.logo.esquerda {
    left: 0;
}

img.logo.direita {
    right: 0;
}

.instrucao {
    text-align: center;
    font-size: 24px;
    margin-bottom: 30px;
    opacity: 0,85;
    color: red;
}

.lightbox {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.85);
    justify-content: center;
    align-items: center;
    z-index: 9999;
}

.lightbox img {
    max-width: 90%;
    max-height: 90%;
    border-radius: 12px;
    box-shadow:0 0 30px rgba(0,0,0,0.6);
}

.fotos img {
    cursor: zoom-in;
}

footer{
    text-align: center;
    margin-top: 40px;
    padding: 20px 10px;
    font-size: 21px;
    color: black;
    opacity; 0,8;
}

</style>
</head>
<body>
<div class="topo">
    <img class="logo esquerda" src="assets/logos/logo_direito/logo-direito.jpeg">
    <img class="logo direita" src="assets/logos/logo_esquerdo/logo-esquerdo.jpeg">
</div>


<h1>Mural de Pets 🐾</h1>
<p class="instrucao">Para ver maior, basta clicar na foto!</p>

<div class="mural">
"""

for _, row in df.iterrows():
    nome = row["Seu nome"]
    pet = row["Nome e Idade do seu pet (se for mais de um escreva da seguinte forma NOME E IDADE PET1 | NOME E IDADE PET 2)"]
    fotos_raw = row["fotos"]

    if pd.isna(fotos_raw):
        continue

    fotos_lista = str(fotos_raw).split(";")

    html += f"""
    <div class="pet-card">
        <h2>{nome}</h2>
        <p>{pet}</p>
        <div class="fotos">
    """

    for foto in fotos_lista:
        foto = foto.strip()
        if foto:
            html += f'<img src="images/{foto}" onclick="abrirLightbox(this.src)">'

    html += """
        </div>
    </div>
    """

html += """
</div>
<footer>
    <p>DHOemAção fazendo uma SBCD de pessoas para pessoas.</p>
</footer>
<div class="lightbox" id="lightbox" onclick="fecharLightbox()">
    <img id="lightbox-img">
</div>
<script>
function abrirLightbox(src) {
    const lb = document.getElementById("lightbox");
    const img = document.getElementById("lightbox-img");
    img.src = src;
    lb.style.display = "flex";
}

function fecharLightbox(){
    document.getElementById("lightbox").style.display = "none";
}

document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});
</script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Mural gerado com sucesso")
