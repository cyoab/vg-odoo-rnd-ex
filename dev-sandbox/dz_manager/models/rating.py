from odoo import models, fields


class SkydiveRating(models.Model):
    _name = "skydive.rating"
    _description = "Skydive Rating Model"
    _rec_name = "rating_name"
    rating_name = fields.Char(string="Rating", required=True)
    rating_type = fields.Selection(
        [
            ("coach", "Coach"),
            ("instructor", "Instructor"),
            ("examiner", "Examiner"),
            ("pro", "PRO"),
        ],
        string="Rating Type",
    )
