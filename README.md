# 3mit_test

### Requirements ###

* Python 3.8.10
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
    export LOG_PATH='<str_path>/debug.log'
    export API_URL='https://www.coingecko.com/es/all-cryptocurrencies
    export STATIC_ROOT='<str_path>/statics'

### Installation ###
    ### make a virtual enviroment ###
    virtualenv -p python3 venv
    source venv/bin/activate
    
    ### Install the requirements ###
    pip install -r requirements/dev.txt

    ### Load enviroment ###
    source variables.sh

### Deploy Application ###
    
    ### Migrate Database ###
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    
    ### Create User ####
    python manage.py createsuperuser
        - username: admin
        - password: admin
    
    ### Execute web scrapping ###
    python manage.py getcoins

    ### Run the project ###
    python manage.py runserver 0.0.0.0:8000

### Login ###

    Use the user admin/admin created in the previous step to 
    enter the login of the application



