# Proyecto CADEM API-B2B

## Descripción

Este proyecto está constituido por tres Endpoint o Microservicio.

1- Microservicio Cálculo Venta Volumen.  
2- Microservicio Cálculo DOH - INSTOCK.  
3- Microservicio (pendiente por definir)  


## Dependencias del proyecto
Para ejecucion de estos Endpoint es necesario instalar las siguientes dependencias de Python.

En la consola como administrador teclear el comando: 

`$ pip3 install flask`  
`$ pip3 install flask-cors`  
`$ pip3 install flask-mysql`  
`$ pip3 install pymysql`  
`$ pip3 install python-dotenv`


O simplemente instalar las dependencias a partir de un archivo de requerimiento con el siguiente comando

`$ pip3 install -r requeriments.txt`

Con este último comando, se instalan las dependencias necesaria para el funcionamiento de estos microservicios.

#### Configurar los parámetros de la conexión
Este apartado cuenta con un fichero .env que contiene los parámeteros para conectarse al servidor y la 
base de datos a consultar.  

`DB_HOST="localhost"`  
`DB_PORT="3306"`  
`DB_NAME="b2b"`  
`DB_USER="admin"`  
`DB_PASS="mi_password"`

>Estos valores se deben de cambiar por los oficiales que estan en Amazon.  

## Utilización de los EndPoints

El primer Endpoint con la url: `http://<ip_host>:<[puerto]>/update_venta`   
En el cuerpo del Endpoint adicionar dos parámetros en formato JSON:  

{
	"table_name": "movimiento",
	"iean": "7803908001420"
}

* En table_name, se define el nombre de la tabla a actualizar, sea movimiento, movimiento_historia o movimiento_historia_YYYY.
* En iean, el código ean del item a actualizar

El segundo Endpoint con la url: `http://<ip_host>:<[puerto]>/doh-instock`   
En el cuerpo del Endpoint adicionar dos parámetros en formato JSON:  

{
	"table_name": "movimiento",
	"fecha": "2022-04-01"
}

* En table_name, se define el nombre de la tabla a actualizar, sea movimiento, movimiento_historia o movimiento_historia_YYYY.
* En fecha, la fecha a consultar para realizar los cálculos


## Tecnologías empleadas

* [Python](https://www.python.org): Version 3.7

### Autor
Jose Ramón Vidal Wilson
- [Email: jramonholy@gmail.com](mailto:jramonholy@gmail.com?subject=Hi% "Hi!")
