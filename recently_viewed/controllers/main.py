
# -*- coding: utf-8 -*-
import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp import http

PPG = 20 # Products Per Page
PPR = 4  # Products Per Row



class MyController(http.Controller):
    
    ## Code to add current selected product in recently viewed
    @http.route(['/shop/add_product_to_recently_viewed'], type='http', auth="public", website=True)
    def add_product_to_recently_viewed(self, product_id=False):
        cr, uid, context = request.cr, request.uid, request.context
        ## To check product is alredy present in recent view 
        cr.execute('select product_id,user_id from recently_viewed_partner_product_relation where product_id =%s and user_id=%s'%(product_id, uid))
        record_fetched = cr.fetchall()
        
        ## If product is not present then insert product into recent view
        if not record_fetched:
            cr.execute('insert into recently_viewed_partner_product_relation (product_id,user_id) values (%s,%s)', (product_id, uid))
        return request.redirect("#")
    
    ## Code to view  product in recent viewed
    @http.route(['/shop/view_my_recent_product_list'], type='http', auth="public", website=True)
    def view_my_recent_product_list(self, product_id=False):
        cr, uid, context = request.cr, request.uid, request.context
        
        ## Select product from recent view to display on website
        cr.execute("select product_id from recently_viewed_partner_product_relation where user_id = %s"%(uid))
        product_ids = cr.fetchall()
        values ={
                 'product_id': product_id,
                 'uid': uid,
                 }
        ## redirect selected product values to recent view 
        return request.website.render("recently_viewed.recently_viewed_product_id",values)
    
