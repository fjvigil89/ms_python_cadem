from datetime import datetime

import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request
from flask import render_template


@app.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')


@app.route('/api/docs')
def get_docs():
    print('Documentación interactiva de APIs!')
    # url: http://127.0.0.1:5000/api/docs
    return render_template('swaggerui.html')


@app.route('/api/items')
def get_items():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT im.i_ean, im.i_item, im.i_factor_volumen, m.fecha, m.venta_unidades, m.venta_volumen, " \
              "(m.venta_unidades * im.i_factor_volumen) AS v_venta_volumen " \
              "FROM item_master im INNER JOIN movimiento m ON im.i_ean = m.ean LIMIT 10"
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


@app.route('/api/update-sales', methods=['PUT'])
def update_venta_volumen():
    try:
        _json = request.json
        _table_name = _json['table_name']
        _ean = _json['ean']
        _retail = _json['retail']
        if _ean and request.method == 'PUT':
            print("Ejecutando query...")
            sqlQuery = "UPDATE " + _table_name + " mv " \
                "INNER JOIN item_master im ON mv.ean = im.i_ean " \
                "SET mv.venta_volumen = mv.venta_unidades * im.i_factor_volumen " \
                "WHERE mv.ean = %s AND mv.retail = %s "
            bindData = (_ean, _retail)
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


@app.route('/api/doh-instock', methods=['GET', 'POST'])
def calculate_doh_instock():
    # add_columns(_table_name, ' doh')
    # add_columns(_table_name, ' instock')
    try:
        _json = request.json
        _table_name = _json['table_name']
        _fecha = _json['fecha']
        _ean = _json['ean']
        _retail = _json['retail']
        selected_date = datetime.strptime(_fecha, "%Y-%m-%d").date()
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT fecha, ean, retail, " \
            "@stock_aj := IF(stock < 0 OR stock IS NULL, 0, stock) AS stock_ajustado, " \
            "@promedio := IF(promedio_ventas_uni < 0 OR promedio_ventas_uni IS NULL, 0, promedio_ventas_uni) AS pvu_ajustado, " \
            "@my_doh := IF(@promedio=0, 0, @stock_aj/@promedio) AS doh, " \
            "IF(@my_doh < 1, 0, 1) AS instock " \
            "FROM " + _table_name + " " \
            "WHERE fecha=%s AND ean=%s AND retail=%s "
        bindData = (selected_date, _ean, _retail)
        cursor.execute(query, bindData)
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
