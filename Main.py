import tkinter as tk
import mysql.connector
from login import*

config = {
        'user': 'uny6nwhsl2130sgv',
        'password': 'McTB25yUL5RJdeurHpJx',
        'host': 'bdsukinarwhdghga6v7d-mysql.services.clever-cloud.com',
        'database': 'bdsukinarwhdghga6v7d',
        'raise_on_warnings': True
}

def consulta(sql):
    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except mysql.connector.Error as error:
        return [("Error", str(error))]