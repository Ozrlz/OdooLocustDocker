# How to use it
* > docker run -e ODOO_login=user -e ODOO_PASSWORD=odoo \
    -e ODOO_HOST="odoo" -e ODOO_DATABASE="dev" -e ODOO_PORT=8069 \
    --rm --name pylocust --link odoo:odoo -p 8089:8089 -t odoolocust:1.0
