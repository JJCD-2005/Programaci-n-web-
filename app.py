from flask import Flask, render_template

events = [
    {
        'id': 1,
        'title': 'Conferencia de Python',
        'slug': 'conferencia-python',
        'description': 'Descripción del evento sobre Python...',
        'date': '2025-09-15',
        'time': '14:00',
        'location': 'Auditorio Principal',
        'category': 'Tecnología',
        'max_attendees': 50,
        'attendees': [],
        'featured': True
    },
    {
        'id': 2,
        'title': 'Torneo de Ajedrez',
        'slug': 'torneo-ajedrez',
        'description': 'Torneo abierto para todos los niveles.',
        'date': '2025-10-05',
        'time': '10:00',
        'location': 'Centro Comunitario',
        'category': 'Deportivo',
        'max_attendees': 20,
        'attendees': [],
        'featured': False
    }
]

categories = ['Tecnología', 'Académico', 'Cultural', 'Deportivo', 'Social']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)