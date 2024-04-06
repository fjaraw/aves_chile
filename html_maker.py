def make_cards(fotos):
    cards = ''
    for foto in fotos:
        cards += f'''<div class="col-3">
        <div class="card mt-3" style="width: 18rem;">
            <img src="{foto['images']['main']}" class="card-img-top" alt="{foto['name']['english']}">
            <div class="card-body">
                <h5 class="card-title">{foto['name']['spanish']}</h5>
            </div>
            <ul class="list-group list-group-flush">
                <!-- id de idiomas en ISO 639-1 -->
                <li class="list-group-item"><b>en:</b> {foto['name']['english']}</li>
                <li class="list-group-item"><b>la:</b> {foto['name']['latin']}</li>
            </ul>
            <div class="card-body">
                <a href="{foto['images']['full']}" class="card-link">Ampliar imagen</a>
            </div>
        </div>
    </div>'''
    return cards

def make_full_html(cards):
    html_template = f'''<!doctype html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Aves Chile</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>

    <body>
        <div class="container">
            <h1 class="text-center">Aves Chile</h1>
            <div class="row">
                {cards}
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
            crossorigin="anonymous"></script>
    </body>

    </html>'''
    return html_template