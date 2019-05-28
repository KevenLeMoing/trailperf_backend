# trailperf

Project structure
https://drivendata.github.io/cookiecutter-data-science/#directory-structure
https://github.com/d6t/d6tpipe

API to help trailers in their logistic management

@TODO
- adapt the code to persist results in mongoDB. Files inpacted: docker-compose, config, etc...
- use mongokit inside the app.

application factory pattern

######setup local env:
`$ virtualenv venv` 

(please update .gitignore in case you choose an other name for your virtualenv)

`$ pip install flask flask_script`
`$ pip install Flask-PyMongo`

######launch the app :
 
`$ python ./manage.py runserver`

######In case you use any new dependency:

`$ pip freeze >> requirements.txt`


######Build your docker image

`docker image build -t flask-starter-kit:latest .`

`docker container run -p 5000:5000 flask-starter-kit`

######deploy services

`docker-compose up` !!!!!!! replace MySQL with MongoDB