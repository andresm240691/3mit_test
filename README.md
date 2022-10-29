# 3mit_test

### Requirements ###

* Python 3.8.5
* Postgres 14


### Enviroments ###

    # Database Postgres SQL 
    export DB_NAME=treemittest
    export DB_USER=admin
    export DB_PASSWORD=admin
    export DB_HOST=localhost
    export DB_PORT=5433

    # Configuration
    export ALLOWED_HOSTS=*
    export LOG_PATH='/home/andres/Projects/3mit_test/logs/debug.log'
    export API_URL='https://www.coingecko.com/es/all-cryptocurrencies
    export STATIC_ROOT='/home/andres/Projects/3mit_test/3mit_test/statics'

### Installation ###
    ### make a virtual enviroment ###
    virtualenv -p python3 venv
    source venv/bn/activate
    
    ### Install the requirements ###
    pip install -r requirements/dev.txt

### Deploy Application ###
    
    ### Migrate Database ###
    python manage.py makemigrations
    python manage.py migrate

    ### Create User ####
    python manage.py createsuperuser
        - username: admin
        - password: admin

    ### Run the project ###
    python manage.py runserver 0.0.0.0:8000

  

