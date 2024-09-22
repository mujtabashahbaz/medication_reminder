# Flask app routes
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Medication

# Home route to list all medications
@app.route('/')
def index():
    medications = Medication.query.all()
    return render_template('index.html', medications=medications)

# Route to add a new medication
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        med_name = request.form['name']
        med_time = request.form['time']
        med_dosage = request.form['dosage']

        new_medication = Medication(name=med_name, time=med_time, dosage=med_dosage)
        db.session.add(new_medication)
        db.session.commit()

        return redirect(url_for('index'))

# Route to delete a medication
@app.route('/delete/<int:id>')
def delete(id):
    medication_to_delete = Medication.query.get_or_404(id)
    db.session.delete(medication_to_delete)
    db.session.commit()

    return redirect(url_for('index'))
