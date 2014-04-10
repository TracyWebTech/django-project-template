{{ project_name }}
=================


Installation (dev environment)
======================

Before getting started you should install the following softwares:

* Vagrant (tested with version 1.5.2)

* Virtualbox (version >= 4.3)

* fabric (tested with version 1.8.2)

### Usage

Firstly, run the following commands:

    vagrant up
    fab bootstrap
    fab deploy

Done.

To run the server, run the following commands:

    vagrant ssh
    sudo su - {{ project_name }}
    cd {{ project_name }}/src && workon {{ project_name }}
    python manage.py runserver 0.0.0.0:8000

Now you can access on your machine with `http://localhost:8000`
