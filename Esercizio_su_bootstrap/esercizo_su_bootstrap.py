def generate_html(N):
    # Blocco iniziale fisso (pag11)
    pag11 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Griglia con Bootstrap</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Pagina di esempio</h1>
            </div>
        </div>'''
    
    # Blocco ripetuto (pag12)
    pag12 = '''
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <img src="cane.webp" class="card-img-top" alt="animale" width"400" height"250"">
                        <h5 class="card-title">Cane</h5>
                        <p class="card-text">Bau bau</p>
                    </div>
                </div>
            </div>
        </div>'''
    
    # Blocco finale fisso (pag13)
    pag13 = '''
        <div class="row">
            <div class="col-12">
                <footer>
                    <p>Footer della pagina</p>
                </footer>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    # Costruzione della pagina HTML completa
    html_content = pag11 + (pag12 * N) + pag13
    
    # Salva il contenuto HTML in un file
    with open("pagina_generata.html", "w") as file:
        file.write(html_content)

# Esempio di utilizzo
N = 5
generate_html(N)
