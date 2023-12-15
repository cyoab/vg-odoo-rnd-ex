from odoo import models, fields, api

from datetime import timedelta


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
        related="contact_id.name",
        store=True,
        readonly=True,
        string="Name",
        default="New Skydiver",
    )

    # contact_id is a many2one field to the contact model
    contact_id = fields.Many2one(
        "res.partner", string="Contact", required=True, ondelete="restrict"
    )
    emergency_contact = fields.Many2one(
        "res.partner", string="Emergency Contact", ondelete="restrict", required=True
    )
    license = fields.Selection(
        [
            ("aff", "AFF"),
            ("student", "Student"),
            ("a", "A"),
            ("b", "B"),
            ("c", "C"),
            ("d", "D"),
        ],
        string="License",
        required=True,
    )
    license_number = fields.Char(string="License Number")
    license_expiration = fields.Date(string="License Expiration")
    # ratings should be a category field and disable creation
    skydiver_ratings = fields.Many2many(
        "skydiver.rating",
        string="Ratings",
    )
    # ratings = fields.Many2many("skydiver.rating", string="Ratings")
    jump_number = fields.Integer(string="Jump Number", required=True)

    # Rig info
    container = fields.Char(string="Container")
    main_canopy = fields.Char(string="Main Canopy")
    main_canopy_size = fields.Integer(string="Main Canopy Size")
    reserve_canopy = fields.Char(string="Reserve Canopy")
    reserve_canopy_size = fields.Integer(string="Reserve Canopy Size")
    aad = fields.Char(string="AAD")
    reserve_packed = fields.Date(string="Last Reserve Packed")
    reserve_expiration = fields.Date(
        string="Reserve expiration",
        read_only=True,
        compute="_compute_reserve_expiration",
    )

    @api.constrains("reserve_packed")
    def _check_reserve_packed(self):
        for record in self.filtered(lambda r: r.reserve_packed):
            if record.reserve_packed > fields.Date.today():
                raise models.ValidationError(
                    "Reserve packed date cannot be in the future"
                )

    @api.depends("reserve_packed")
    def _compute_reserve_expiration(self):
        with_reserves = self.filtered(lambda r: r.reserve_packed)
        for record in with_reserves:
            record.reserve_expiration = record.reserve_packed + timedelta(days=180)

        for record in self - with_reserves:
            record.reserve_expiration = False
