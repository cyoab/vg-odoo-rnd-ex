from odoo import models, fields, api


class Skydiver(models.Model):
    _name = "skydiver"
    _description = "Skydiver Model"

    _rec_name = "skydiver_name"
    _sql_constraints = [
        (
            "unique_license_number",
            "unique(license_number)",
            "License number must be unique",
        )
    ]

    # name is a related field to the contact model
    skydiver_name = fields.Char(
        related="contact_id.name", store=True, readonly=True, string="Name"
    )

    # contact_id is a many2one field to the contact model
    contact_id = fields.Many2one("res.partner", string="Contact", required=True)
    emergency_contact = fields.Many2one("res.partner", string="Emergency Contact")
    license = fields.Selection(
        [("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")], string="License"
    )
    license_number = fields.Char(string="License Number")
    license_expiration = fields.Date(string="License Expiration")
    # ratings = fields.Many2many("skydiver.rating", string="Ratings")
    jump_number = fields.Integer(string="Jump Number")

    # Rig info
    container = fields.Char(string="Container")
    main_canopy = fields.Char(string="Main Canopy")
    main_canopy_size = fields.Integer(string="Main Canopy Size")
    reserve_canopy = fields.Char(string="Reserve Canopy")
    reserve_canopy_size = fields.Integer(string="Reserve Canopy Size")
    aad = fields.Char(string="AAD")
    reserve_packed = fields.Date(string="Last Reserve Packed")
    reserve_expiration = fields.Date(string="Reserve expiration")
