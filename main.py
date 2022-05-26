from datetime import datetime

import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/')
def root():
    return "Bienvenido a B2B-API Endpoints!"


@app.route('/items')
def get_items():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT im.i_ean, im.i_item, im.i_factor_volumen, m.fecha, m.ean, m.venta_unidades, m.venta_volumen, " \
              "(m.venta_unidades * im.i_factor_volumen) AS x_venta_volumen " \
              "FROM item_master im INNER JOIN movimiento m ON im.i_ean = m.ean LIMIT 200"
        cursor.execute(sql)
        rows = cursor.fetchall()
        respone = jsonify(rows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/item/<string:ean_id>')
def item_details(ean_id):
    try:
        print(ean_id)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT i_ean, i_item, i_factor_volumen FROM item_master WHERE i_ean=%s", ean_id)
        rows = cursor.fetchone()
        respone = jsonify(rows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/update_venta', methods=['PUT'])
def update_venta_volumen():
    try:
        _json = request.json
        _table_name = _json['table_name']
        _iean = _json['iean']
        if _iean and request.method == 'PUT':
            print("Ejecutando query...")
            sqlQuery = "UPDATE " + _table_name + " mv " \
                "INNER JOIN item_master im ON mv.ean = im.i_ean " \
                "SET mv.venta_volumen = mv.venta_unidades * im.i_factor_volumen " \
                "WHERE mv.ean = %s "
            bindData = (_iean)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Volumen de venta calculado con exito!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Finalizado.")


def add_columns(table_name, column_name):
    try:
        # MySQL query for adding a column
        query = "ALTER TABLE " \
                + table_name + \
                " ADD COLUMN IF NOT EXISTS " \
                + column_name + \
                "DECIMAL(18, 5) DEFAULT NULL "
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Columnas creadas!")


@app.route('/doh-instock', methods=['GET', 'POST'])
def calculate_doh_instock():
    # add_columns(_table_name, ' doh')
    # add_columns(_table_name, ' instock')
    try:
        _json = request.json
        _table_name = _json['table_name']
        _fecha = _json['fecha']
        selected_date = datetime.strptime(_fecha, "%Y-%m-%d").date()
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT fecha, ean, " \
            "@stock_aj := IF(stock < 0 OR stock IS NULL, 0, stock) AS stock_ajustado, " \
            "@promedio := IF(promedio_ventas_uni < 0 OR promedio_ventas_uni IS NULL, 0, promedio_ventas_uni) AS promedio_ventas_uni_ajustado, " \
            "@my_doh := IF(@promedio=0, 0, @stock_aj/@promedio) AS doh, " \
            "IF(@my_doh < 1, 0, 1) AS instock " \
            "FROM " + _table_name + " " \
            "WHERE fecha = %s "
        cursor.execute(sql, selected_date)
        rows = cursor.fetchall()
        respone = jsonify(rows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run()
