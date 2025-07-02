{
    'name': 'Dog Registration Portal',
    'version': '18.0.1.0.21',
    'category': 'Website',
    'summary': 'Add dog registration fields to portal signup and user profile',
    'description': """
        This module extends the portal signup and user profile pages to include
        dog registration information such as name, breed, age, and weight.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'base',
        'portal',
        'website',
        'auth_signup',
    ],
    'data': [
        'views/portal_templates.xml',
        'views/auth_signup_templates.xml',
        'views/dog_portal_templates.xml',
        'views/test_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}