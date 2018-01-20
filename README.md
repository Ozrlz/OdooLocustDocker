# What's this
This is a repo based on https://github.com/nseinlet/OdooLocust


# How to use it
Params:
    * ODOO_LOGIN = odoo user
    * ODOO_PASSWORD = odoo user password
    * ODOO_HOST = odoo host
    * ODOO_DATABASE = odoo database
    * ODOO_PORT = odoo port

## First, build the image:

* > docker image build . -t odoolocust:1.0

## Then, just run the container:
* > docker run -e ODOO_LOGIN=user -e ODOO_PASSWORD=passwd \
    -e ODOO_HOST=my_hostname -e ODOO_DATABASE="dev" -e ODOO_PORT=8069 \
    --rm --name pylocust -p 8089:8089 -t odoolocust:1.0

# IMPORTANT NOTE !!!
If used for testing/dev purposes on o local env, do not use hosts like '127.0.0.1' of 'localhost', since the tests are going to be executed inside a container and localhost will refer to itself (the container) and will return a no conection issue.
