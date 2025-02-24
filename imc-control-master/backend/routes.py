from flask import Blueprint, request, jsonify
from models import ControlPesoAltura, session
from datetime import datetime
from sqlalchemy import select


bp = Blueprint('api', __name__)

@bp.route('/login', methods=['POST'])
def login():
    # Placeholder for user authentication logic
    username = request.json.get('username')
    password = request.json.get('password')
    # Implement authentication logic here
    return jsonify({"message": "Login successful"}), 200

@bp.route('/summary', methods=['GET'])
def get_summary():
    records = session.scalars(select(ControlPesoAltura)).all()
    summary_data = [
        {
            "fecha": record.fecha.strftime('%Y-%m-%d'),
            "peso_kg": record.peso_kg,
            "altura_m": record.altura_m,
            "imc": record.imc
        }
        for record in records
    ]
    return jsonify(summary_data), 200

@bp.route('/insert', methods=['POST'])
def insert_data():
    fecha = request.json.get('fecha')
    peso_kg = request.json.get('peso_kg')
    altura_m = request.json.get('altura_m')
    imc = peso_kg / (altura_m ** 2)
    respuesta = ""
    if imc < 18.5:
        respuesta = "Bajo peso: Aumenta tu ingesta calórica con alimentos nutritivos."
    elif 18.5 <= imc < 24.9:
        respuesta = "Peso normal: Mantén una alimentación equilibrada y actividad física regular."
    elif 25 <= imc < 29.9:
        respuesta = "Sobrepeso: Reduce el consumo de calorías y aumenta la actividad física."
    else:
        respuesta = "Obesidad: Consulta con un especialista para un plan de alimentación y ejercicio."

    new_record = ControlPesoAltura(
        fecha=datetime.strptime(fecha, '%Y-%m-%d'),
        peso_kg=float(peso_kg),
        altura_m=float(altura_m),
        imc=float(imc)
    )
    session.add(new_record)
    session.commit()
    return jsonify({"message": respuesta    }), 201
    
