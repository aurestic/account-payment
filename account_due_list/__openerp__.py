# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Domsense srl (<http://www.domsense.com>)
#    Copyright (C) 2011-2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    @author Jordi Esteve <jesteve@zikzakmedia.com>
#    @author Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#    Ported to OpenERP 7.0 by Alex Comba <alex.comba@agilebg.com> and
#    Bruno Bottacini <bruno.bottacini@dorella.com>
#    Ported to Odoo by Andrea Cometa <info@andreacometa.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Payments Due list",
    'version': '8.0.1.0.0',
    'category': 'Generic Modules/Payment',
    'author': 'Odoo Community Association (OCA), '
              'Agile Business Group, '
              'Serv. Tecnol. Avanzados - Pedro M. Baeza,'
              'Zikzakmedia SL',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'account',
    ],
    "data": [
        'views/payment_view.xml',
    ],
    #'pre_init_hook': 'pre_init_hook',
    #'post_init_hook': 'post_init_hook',
    "installable": True,
}
