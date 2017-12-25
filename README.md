# What's this
This is a repo based on https://github.com/nseinlet/OdooLocust


# How to use it
Params:
* ODOO_LOGIN = odoo user
* ODOO_PASSWORD = odoo user password
* ODOO_HOST = odoo host
* ODOO_DATABASE = odoo database
* ODOO_PORT = odoo port

In case you want to run it with odoo not using a docker-compose, use --link
* > docker run -e ODOO_login=user -e ODOO_PASSWORD=odoo \
    -e ODOO_HOST="odoo" -e ODOO_DATABASE="dev" -e ODOO_PORT=8069 \
    --rm --name pylocust --link odoo:odoo -p 8089:8089 -t odoolocust:1.0

Else, if you are using docker-compose just add it to the network (--network network_id)
