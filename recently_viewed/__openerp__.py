{
    'name': 'Recent Viewed Product List',
    'category': 'Website',
    'summary': 'View Your Recent Product List',
    'website': 'https://www.techhighway.co.in',
    'version': '1.0',
    'description': """
TechHighway E-Commerce
======================

        """,
    	'author'	: 'TechHighway System Pvt. Ltd.',
    	'depends'	: ['website', 'sale', 'payment','website_sale'],
    	'data'	: [
		'views/template.xml',
    		],
    	'qweb'	: ['static/src/xml/*.xml'],
	'images': ['static/description/recently_viewed_product_img.png'],
        'price': 10,
        'currency': 'EUR',
    	'installable': True,
    	'application': True,
}
