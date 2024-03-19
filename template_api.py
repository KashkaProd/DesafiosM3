from consumir_api import request_json
from string import Template

url = "https://aves.ninjas.cl/api/birds"
response = request_json(url)

lista_img = [(elemento['images']['main'], elemento['name']['spanish']) for elemento in response]

nuevo_card = """<div class="card mx-auto my-3" style="width: 18rem; background-color: #181818;">
                <img src="$url" class="card-img-top" style="height: 200px; object-fit: contain; margin-top: 10px;" alt="...">
                <div class="card-body d-flex flex-column justify-content-center">
                    <h5 class="card-title text-white text-center">$title</h5>
                </div>
            </div>
    """

img_template = Template(nuevo_card)
texto_img = ''

for image, name in lista_img:
    texto_img += img_template.substitute(url=image, title=name) + '\n'

html_template = Template('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        body {
            background-color: black;
        }
        .card {
            background-color: #181818;
            color: white;
        }
    </style>
  </head>
  <body>
    <header>
                <h1 class="text-center text-white">Aves de Chile</h1>
    </header>
    <div class="container">
        <div class="row">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body=texto_img)

archivo = open('index.html', 'w+', encoding='utf-8') 
archivo.write(html)
archivo.close()
