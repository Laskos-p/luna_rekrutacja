# Luna rekrutacja
## Informacje
Aplikacja CRUD w Django, która umożliwia zarządzanie systemami hydroponicznymi


## Uruchomienie projektu

dodaj plik .env. 
Ustaw zmienne np.:
```
DJANGO_SECRET_KEY=very_secret_key
DEBUG=True
DJANGO_LOGLEVEL=info
DJANGO_ALLOWED_HOSTS=0.0.0.0
DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=luna
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

Uruchom aplikację
`docker compose up --build`

### Dokumentacja API

Swagger-ui `/swagger/`
- można uwierzytelnić się logując się przez django admin
- lub generując token podając dane użytkownika na endpoint '/api/token', a następnie wklejając go w autoryzacji `Bearer <token>`


Redoc `/redoc/`

### Przykładowi dane

Znajdują się w plikach .json w folderze `backend`

#### Użytkownicy
admin admin -superuser

user1 password1 -staff

user2 password2 -staff

### Endpointy

`/api/systems` - pobieranie listy systemów oraz wstawianie nowego systemu
`/api/systems/<id>` - pobieranie szczegółów systemu, usuwanie oraz modyfikacja systemu
`/api/systems/<id>/sensor` - pobieranie listy pomiarów dla danego systemu oraz wstawianie nowego pomiaru

`/api/token` - generowanie tokenów do uwierzytelniania

