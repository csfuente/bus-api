# destacamebus-api-rest

## Clonar repositorio

```bash
$ git clone https://github.com/csfuente/bus-api
$ cd bus-api
```

## Instalar entorno virtual con virtualenv

### En caso de no tener virtualenv instalado en su pc
```bash
$ pip install virtualenv
```

### Crear entorno virtual

```bash
$ virtualenv .
$ source bin/activate
```

### Instalar dependencias
```bash
$ pip install -r requirements.txt
$ python manage.py migrate
```

### Correr ambiente de desarrollo
```bash
$ python manage.py runserver
```
