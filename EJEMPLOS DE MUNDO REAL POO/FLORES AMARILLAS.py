from flask import Flask, render_template_string

app = Flask(__name__)

# HTML con rosas amarillas y un mensaje
html_code = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flores Amarillas</title>
    <style>
        body {
            background-color: #2c3e50;
            color: white;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }

        h1 {
            margin-top: 50px;
            font-size: 3em;
            color: #ffd700;
        }

        h2 {
            font-size: 1.5em;
            margin-bottom: 20px;
        }

        .rosas {
            margin-top: 20px;
            width: 300px;
            height: auto;
        }

        button {
            font-size: 1.2em;
            padding: 10px 20px;
            margin-top: 30px;
            background-color: #ffcc00;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        button:hover {
            transform: scale(1.1);
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }

        button {
            animation: pulse 2s infinite;
        }
    </style>
</head>
<body>
    <h1>MI AMOR (｡♥‿♥｡)</h1>
    <h2>Tengo un regalo para ti 🌹</h2>
    <img class="rosas" src="https://example.com/rosas_amarillas.png" alt="Rosas Amarillas">
    <button onclick="window.location.href='https://example.com/regalo'">Ver regalo 💛</button>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
