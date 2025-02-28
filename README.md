# Luna rekrutacja

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

Redoc `/redoc/`

### Przykładowi użytkownicy
admin admin -superuser

user1 password1 -staff

user2 password2 -staff