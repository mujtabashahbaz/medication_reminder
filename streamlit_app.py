# Streamlit app for frontend interaction
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from datetime import datetime

# Set up SQLAlchemy
DATABASE_URL = "sqlite:///app/medications.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Medication model for storing data
class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    time = Column(String(100), nullable=False)
    dosage = Column(String(50), nullable=False)
    date_added = Column(String, default=datetime.utcnow)

Base.metadata.create_all(engine)

# Streamlit app UI
st.title("Medication Reminder")

# Form to add medication
with st.form("medication_form"):
    name = st.text_input("Medication Name")
    time = st.text_input("Time (e.g., 9:00 AM)")
    dosage = st.text_input("Dosage (e.g., 500 mg)")
    submitted = st.form_submit_button("Add Medication")

    if submitted:
        new_medication = Medication(name=name, time=time, dosage=dosage)
        session.add(new_medication)
        session.commit()
        st.success(f"Medication '{name}' added!")

# Display list of medications
st.subheader("Your Medications")
medications = session.query(Medication).all()

for medication in medications:
    st.write(f"{medication.name} - {medication.time} - {medication.dosage}")
    if st.button(f"Delete {medication.name}"):
        session.delete(medication)
        session.commit()
        st.experimental_rerun()  # Refresh the page after deletion
