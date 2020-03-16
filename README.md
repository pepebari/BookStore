# BookStore
Ejercicio para practicar con Django Rest Framewok

## Instalación

Creamos virtual enviorenment
`python3 -m venv .venv`
`source .venv/bin/activate`

`pip install -r requirements.txt`

Sincronizamos la base de datos y cremaos usuario con permisos
`python manage.py migrate`
`python manage.py createsuperuser --email admin@example.com --username admin`

Ejecutamos el servidor
`python manage.py runserver`

## Peticiones a la API
Consulta la lista de usuarios:
`curl -H 'Accept: application/json; indent=4' -u admin http://127.0.0.1:8000/user/`
Consulta el usuario con id=1:
`curl -H 'Accept: application/json; indent=4' -u admin http://127.0.0.1:8000/user/1/`

Añadir usuario:
`curl --header "Content-Type: application/json"  --request POST  --data '{"name": "Popeye", "birth_date": "2020-03-01", "register_date": "2020-03-01", "phone_number": 13, "points": 0}' -u admin http://127.0.0.1:8000/user/`

Eliminar registro:
`curl -X DELETE -u admin http://127.0.0.1:8000/user/1/`

## TODO
Falta añadir opción para buscar en las diferentes tablas
