# -*- coding: utf-8 -*-

# This script gives you a basic connection to the odoo server with the provided credentials
from os import environ
import openerplib

con = openerplib.get_connection(
    hostname=environ["ODOO_HOST"],
    database=environ["ODOO_DATABASE"],
    login=environ["ODOO_LOGIN"],
    password=environ["ODOO_PASSWORD"],
    port=int( environ["ODOO_PORT"] ),
)
