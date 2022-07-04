# Eventex

Sistemas de Eventos

## Como desenvolver? 

1. Clone o repositório
2. Crie uma virtualenv
3. Ative o seu virtualenv.
4. Instale as dependencias
5. Configure a instância com o .env
6. execute os tests.

```console
git clone git@github.com:alefenba/wttd_.git wttd
cd wttd
python -m venv .wttd
.wttd/Scripts/Activate.ps1
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como Fazer Deploy?
1. Crie uma instancia no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o serviço de emai.
6. Envie o código para o heroku

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=python contrib/secret_gen.py"
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force



```