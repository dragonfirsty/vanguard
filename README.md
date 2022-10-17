<h1 align="center">
Vanguard
</h1>

## 💻 Projeto

Projeto com base de criar uma api que pega dados de uma transação e guarda os dados do beneficiario, da loja e da propria transação em si dentro de um banco de dados relacional

## ✨ Tecnologias

- [x] Django
- [x] Django Rest Framework

# Instruções:

### Crie o ambiente virtual

```
python -m venv venv
```

### Ative o venv

```bash
# linux:

source venv/bin/activate

```

```bash
# windows:

.\vevn\Scripts\activate

```

### Crie o .env com o env.example de base
```

touch .env

```

### Instale as dependências

```
pip install -r requirements.txt
```

```
### Execute as migrações
```

./manage.py migrate

```
### Rode a aplicação
```

./manage.py runserver

```


Api realizada interamente em python com django-rest-framework.
```
