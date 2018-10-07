# README 

## Python virtualenv

It is recommended to install Superset inside a virtualenv. Python 3 already ships virtualenv, for Python 2 you need to install it. If it’s packaged for your operating systems install it from there otherwise you can install from pip:
`pip install virtualenv`

### Creating a virtualenv
 In UNIX systems you can create and activate a virtualenv by:
`virtualenv venv`
`. ./venv/bin/activate`

On windows the syntax for activating it is a bit different:
`venv\Scripts\activate`

### Deactivating a virtualenv
Once you activated your virtualenv everything you are doing is confined inside the virtualenv. To exit a virtualenv just type `deactivate`.

## Python’s setup tools and pip

### Put all the chances on your side by getting the very latest pip and setuptools libraries.:
`pip install --upgrade setuptools pip`


## Superset installation and initialization

Follow these few simple steps to install Superset.:

### Install superset
`pip install superset`

### Create an admin user (you will be prompted to set username, first and last name before setting a password)
`fabmanager create-admin --app superset`

### Initialize the database
`superset db upgrade`

### Load some data to play with
`superset load_examples`

### Create default roles and permissions
`superset init`

### To start a development web server on port 8088, use -p to bind to another port
`superset runserver -d`

## Post-installation

After installation, you should be able to point your browser to the right hostname:port http://localhost:8088, login using the credential you entered while creating the admin account, and navigate to Menu -> Admin -> Refresh Metadata. This action should bring in all of your datasources for Superset to be aware of, and they should show up in Menu -> Datasources, from where you can start playing with your data!

In the virtual environment created above, go to the lib folder. In the lib folder there will exist a folder called pythonX where X is the python version for example the folder could be python2.7 or another example would be python3.5. From there run this command:
`cd site-packages/superset`
Replace this folder with the one present in src, i.e., the superset folder.