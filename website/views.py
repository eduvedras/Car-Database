from flask import Blueprint, render_template, request, flash, jsonify
from .models import Car
from . import db
import json
from sqlalchemy import func, select

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html") #this is the home page

@views.route('/delete-car', methods=['POST'])
def delete_car():
    car = json.loads(request.data) # this function expects a JSON from the INDEX.js file
    carId = car['carId']
    car = Car.query.get(carId)
    if car:
        db.session.delete(car)
        db.session.commit()

    return jsonify({})

@views.route("/adicionarcarro",methods=['GET', 'POST'])
def adicionarcarro():
    if request.method == 'POST':
        marca = request.form.get('marca')
        ano = request.form.get('ano')
        modelo = request.form.get('modelo')
        preco = request.form.get('preco')
        new_car = Car(brand=marca, year=ano, model=modelo, price=preco)
        db.session.add(new_car) #adding the car to the database
        db.session.commit()
        #flash('Carro adicionado!', category='success')

    return render_template("adicionarcarro.html")

@views.route("/removercarro",methods=['GET', 'POST'])
def removercarro():
    #if len(res) == 0:
    #    flash('Não existem carros na base de dados!', category='error')

    return render_template("removercarro.html", result=Car.query.all())

@views.route("/pesquisar",methods=['GET', 'POST'])
def pesquisar():
    res = Car.query.all()
    if request.method == 'POST':
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        ano = request.form.get('ano')

        if len(marca) != 0 and len(modelo) == 0 and len(ano) == 0:
            res = Car.query.filter(Car.brand == marca).all()
        elif len(marca) != 0 and len(modelo) != 0 and len(ano) == 0:
            res = Car.query.filter(Car.brand == marca, Car.model == modelo).all()
        elif len(marca) != 0 and len(modelo) != 0 and len(ano) != 0:
            res = Car.query.filter(Car.brand == marca, Car.model == modelo, Car.year == ano).all()

    if len(res) != 0:
        sum = 0
        max_val = res[0].price
        min_val = res[0].price
        for car in res:
            if car.price > max_val:
                max_val = car.price
            if car.price < min_val:
                min_val = car.price
            sum += car.price
        avg = sum/len(res)
    else:
        avg = 0
        max_val = 0
        min_val = 0
        #flash('Não foram encontrados resultados!', category='error')

    return render_template("pesquisar.html", result=res, average=avg, max_val=max_val, min_val=min_val)
