FROM python:3.10.16-slim

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./backend/requirements.txt .
RUN pip install -r requirements.txt

COPY ./backend .

EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]