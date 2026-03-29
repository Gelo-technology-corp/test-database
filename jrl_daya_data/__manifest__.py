{
    'name': 'Aviniva Client Demon Data',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Pre-loaded master data for JRL & Daya operations: contacts, products, locations, pricelists',
    'description': """
JRL & Daya Master Data Module
==============================

This module pre-loads the following master data for JRL & Daya business operations:

* **Suppliers**: CDO FoodSphere and related vendor records
* **Customers**: Alphamart, Asari Asari Store, Easy Mart, Tambayan Store
* **Product Categories**: Frozen Processed Food and sub-categories
* **Products**: Cheese Dog and other CDO FoodSphere product lines
* **Warehouse Locations**: JRL Daya warehouse with hierarchical sub-locations
  (Receiving, Storage zones, Shipping, Cold Storage)
* **Pricelists**: Dealer pricelist with bulk-discount rules (e.g. 10% off ≥100 units for Alphamart)
* **Departments**: Operations Support, Accounting, Warehouse, Management

Designed for the Philippine localization with PHP currency.
    """,
    'author': 'AvinivA Technology',
    'website': 'https://www.aviniva.com',
    'license': 'LGPL-3',
    'depends': [
        'contacts',
        'product',
        'stock',
        'sale_management',
        'purchase',
        'hr',
        'product_expiry',
    ],
    'data': [
        'data/res_partner_data.xml',
        'data/hr_department_data.xml',
        'data/product_category_data.xml',
        'data/product_template_data.xml',
        'data/product_supplierinfo_data.xml',
        'data/stock_location_data.xml',
        'data/product_pricelist_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
