from flask import Flask, render_template, abort, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import re

# Estructura de datos en memoria para los eventos
events = [
    {
        'id': 1,
        'title': 'Conferencia de Python',
        'slug': 'conferencia-python',
        'description': 'Descripción del evento sobre Python y sus aplicaciones en la ciencia de datos.',
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
        'description': 'Torneo abierto para todos los niveles, desde principiantes hasta expertos.',
        'date': '2025-10-05',
        'time': '10:00',
        'location': 'Centro Comunitario',
        'category': 'Deportivo',
        'max_attendees': 20,
        'attendees': [],
        'featured': False
    }
]

# Categorías de eventos
categories = ['Tecnología', 'Académico', 'Cultural', 'Deportivo', 'Social']

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'una-clave-secreta-muy-dificil'

# Clase para el formulario de eventos
class EventForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    date = StringField('Fecha (YYYY-MM-DD)', validators=[DataRequired()])
    time = StringField('Hora (HH:MM)', validators=[DataRequired()])
    location = StringField('Ubicación', validators=[DataRequired()])
    category = SelectField('Categoría', choices=[(c, c) for c in categories], validators=[DataRequired()])
    max_attendees = IntegerField('Cupo Máximo', validators=[DataRequired(), NumberRange(min=1)])
    featured = BooleanField('Destacado')
    submit = SubmitField('Crear Evento')

@app.route('/')
def index():
    """Muestra la página principal con la lista de eventos."""
    return render_template('index.html', events=events)

@app.route('/event/<slug>/')
def event_detail(slug):
    """Muestra los detalles completos de un evento específico."""
    event = next((item for item in events if item['slug'] == slug), None)
    if event is None:
        abort(404)
    return render_template('event_detail.html', event=event)

@app.route('/admin/event/', methods=['GET', 'POST'])
def create_event():
    """Maneja la creación de nuevos eventos a través de un formulario."""
    form = EventForm()
    if form.validate_on_submit():
        new_id = len(events) + 1
        
        # Genera un slug a partir del título
        slug_text = form.title.data.lower().strip()
        new_slug = re.sub(r'[^a-z0-9\s-]', '', slug_text).replace(' ', '-')
        
        new_event = {
            'id': new_id,
            'title': form.title.data,
            'slug': new_slug,
            'description': form.description.data,
            'date': form.date.data,
            'time': form.time.data,
            'location': form.location.data,
            'category': form.category.data,
            'max_attendees': form.max_attendees.data,
            'attendees': [],
            'featured': form.featured.data
        }
        events.append(new_event)
        return redirect(url_for('event_detail', slug=new_slug))
    return render_template('create_event.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)