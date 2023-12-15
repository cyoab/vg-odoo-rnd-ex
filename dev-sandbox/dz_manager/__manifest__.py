{
    "name": "DZ Manager",
    "version": "1.0",
    "category": "Skydiving/DZ Manager",
    "description": """
    Skydiving Dropzone Manager
    """,
    "author": "cyoab",
    "website": "http://odoo.com",
    "depends": ["sale"],
    "data": [
        "security/dzm_groups.xml",
        "security/ir.model.access.csv",
        "views/dz_manager_menu.xml",
        "views/skydiver_views.xml",
        "views/rating_view.xml",
    ],
    "demo": ["data/ratings_data.xml"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
