# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

import openerp
from openerp import tools

from openerp.osv import fields, osv
from openerp.tools.translate import _

import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request


class res_partner(osv.osv):
    _inherit = "res.partner"
    
    _columns = {
        'partner_product_recently_viewed_rel': fields.many2many('product.product', 'recently_viewed_partner_product_relation', 'user_id', 'product_id', 'Recently Viewed'),
    }
res_partner()
    
class recently_viewed_product(osv.osv):
    _name = "recently.viewed.product"
    
    _columns = {
        'name': fields.char('Name')
    }
    
recently_viewed_product()


class website(osv.osv):
    _inherit = 'website'
    
    def get_recently_viewed_product(self, cr, uid, context=None):
        """To get product list of recent viewed product"""
        
        new_product_ids = []
        reversed_product_ids = []
        cr.execute("select count(*) from recently_viewed_partner_product_relation")
        count_for_product = cr.fetchall()
        
        ## Only 5 product can display on website
        if count_for_product[0][0] >5:
            cr.execute("select product_id from recently_viewed_partner_product_relation limit 1")
            product_id = cr.fetchall()
            cr.execute("delete from recently_viewed_partner_product_relation where product_id=%s"%(product_id[0][0]))
            
        cr.execute("select product_id from recently_viewed_partner_product_relation where user_id = %s"%(uid))
        product_ids = [ i[0] for i in cr.fetchall()]
        ## Fetched product from recent viewed and pass product ids to display on website
        for p_id in product_ids:
            product_id = self.pool.get('product.product').browse(cr,uid,p_id)
            if product_id:
                new_product_ids.append(product_id)
        for new_product_id in reversed(new_product_ids):
            reversed_product_ids.append(new_product_id)
        ## return reversed product ids
        return reversed_product_ids
    
website()
