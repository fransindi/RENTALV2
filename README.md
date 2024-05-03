# Rental de equipos para la nieve

En este proyecto crearemos una serie de endpoints en FastAPI para crear un MVP de una aplicacion de alquiler de indumentaria y equipamiento para la nieve, utilizando una base de datos SQLITE para la persistencia de los datos
y orientado en un esquema tipo copo de nieve. La aplicacion cubrira los aspectos basicos de un sistema de alquiler y renta.

El flujo principal de la aplicacion esta orientado de manera que un cliente pueda agendar una reserva. Esta reserva contendra miembros que estaran conectados a los equipos que reservan. Una vez confirmada la reserva se crea un contrato donde se calculan
los precios con la solicitud final. El sistema de precios esta compuesto por un sistema donde cada tipo de equipo tiene su precio base, el cual sera multiplicado por un porcentaje de incremento dependiendo de la gama del mismo equipo
(por ejemplo una bota alta gama seria mas costosa que una de gama standard). Este precio compuesto se multiplicara por la escala de dias.


Un ejemplo del DER.

![image](https://github.com/fransindi/RENTALV2/assets/83618758/4fd35199-3500-45b1-be6b-f6fd3e4ad1ec)

  


## Endpoints: 

#### Client
- **POST client/:** Crea un cliente nuevo.
- **GET client/all:** Lista todos los clientes.
- **GET client/{id}:** Lista un cliente especifico.
- **DELETE client/{id}:** Elimina un cliente en especifico.

#### Equipment
- **POST equipment/:** Crea un equipo nuevo.
- **GET equipment/all:** Lista todos los equipamientos.
- **GET equipment/{id}:** Lista un equipo especifico.
- **DELETE equipment/{id}:** Elimina un equipo en especifico.

#### Member
- **POST member/{reservation_id}:** Crea un nuevo miembro para una reserva ya creada.
- **GET member/by_reservation/{id}:** Lista todos los miembros de una reserva

#### Reservation
- **POST reservation/:** Crea una nueva reserva.
- **GET reservation/all:** Lista todas las reservas.
- **GET reservation/{id}:** Lista una reserva en especifico.
- **DELETE reservation/{id}:** Elimina una reserva en especifico.

#### Contract
- **POST contract/{reservation_id}:** Crea un contrato nuevo desde una reserva.
- **GET contract/all:** Lista todos los contratos.
- **POST contract/return/{id}:** Devuelve los equipos de un contrato.
- **DELETE contract/{id}:** Elimina un contato en especifico.


### Instalación

Primero que nada debermos crear un entorno virtual, esto lo haremos con el siguiente comando en bash:

    python3 -m venv env

Ahora debemos hacer uso del entorno con la siguiente linea de codigo.

    source env\Scripts\activate

Una vez descargado el proyecto y en la carpeta raiz del mismo se debe instalar las dependencias con el comando

    pip install -r requirement.txt


### Levantar proyecto


Para ejecutar el proyecto y que se levanta el servidor se deberá en la raiz del repositorio.

    uvicorn main:app --reload

Esto creará un servidor donde está corriendo la app, en la siguiente url http://localhost:8000/

