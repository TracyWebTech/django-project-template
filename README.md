{{ project_name }}
=================


Installation (dev environment)
===============================

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


Installation (other environments)
=================================

The dependencies are the same as in dev environment (see above). 

### Configuration

Edit the file `project_cfg.py` and set the variable `repository_url`.

Now you can setup your deployment environments by editing the `environment` dict.
The `qa` and `prod` environments are just name examples, feel free to name your environments as you like.

### Usage

To deploy in an specific environment you have to run:

    fab environment:[env_name] bootstrap
    fab environment:[env_name] ssh_keygen # and copy the key to your github/gitlab repository
    fab environment:[env_name] deploy

That's it! You can also run any other fabric tasks on the remote server by using the same prefix (`environment:[env_name]`).
