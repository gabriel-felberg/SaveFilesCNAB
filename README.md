# Dragon File

A aplicação Dragon File tem como finalidade a conversão do arquivo CNAB para um banco de dados, e a exibição do arquivo através de uma tabela formatada com os dados do usuário.

## Linguagem Principal

Python

## Principais bibliotecas

1.black
2.pycodestyle
3.coverage
4.psycopg2-binary
5.gunicorn

## Framework

Django

## Devemos ter o seguinte programa intalado

```text
Python
```

## Para iniciar o projeto rode o comando

```text
python -m venv venv
```

## Ative o ambiente virtual no powershell

```text
.\venv\Scripts\activate
```

## Instale as bibliotecas

```text
pip install djangorestframework
```

```text
pip install django
```

```text
pip install -r requirements.txt
```

## Agora vamos gerar e aplicar as migrations

```text
python manage.py makemigrations
```

```text
python manage.py migrate
```

## vamos iniciar o projeto

```text
python manage.py runserver
```

## acesse a rota abaixo em seu navegador

```link
http://127.0.0.1:8000/api/start/
```
