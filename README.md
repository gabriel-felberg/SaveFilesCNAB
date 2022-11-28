# Dragon File

A aplicação Dragon File tem como finalidade a conversão do arquivo CNAB para um banco de dados, e a exibição do arquivo através de uma tabela formatada com os dados do usuário.

## Linguagem Principal

1.Python

## Principais bibliotecas

1.black
2.pycodestyle
3.coverage
4.psycopg2-binary
5.gunicorn

## Framework

1.Django

## Devemos ter o seguinte programa intalado

```json
1.Python
```

## Para iniciar o projeto rode o comando

```json
python -m venv venv
```

## Ative o ambiente virtual no powershell

```json
.\venv\Scripts\activate
```

## Instale as bibliotecas

```json
pip install djangorestframework
```

```json
pip install django
```

```json
pip install -r requirements.txt
```

## Agora vamos gerar e aplicar as migracoes

```json
python manage.py makemigrations
```

```json
python manage.py migrate
```

### Não se esquesa de configurar as variáveis de ambiente de acordo com o arquivo ".env.example" e coloqueas em um arquivo chamado ".env"

## vamos iniciar o projeto

```json
python manage.py runserver
```

## acesse a rota abaixo em seu navegador

```link
http://127.0.0.1:8000/api/start/
```
