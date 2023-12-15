from odoo import models, fields

class Estate(models.Model):
    _name = "estate.estate"
    _description = "Real Estate model"

    name = fields.Char(string="Estate name", default="New", required=True)
    salesperson_id = fields.Many2one(comodel_name="res.users", string="Salesperson", required=True)
    estate_type = fields.Selection(selection=[('house', 'House'), ('land', 'Land'), ('apartment', 'Apartment')],
                                   string="Type", required=True) 
    price = fields.Float(string="Price", required=True)
    status = fields.Selection(selection=[('new', 'New'), ('offer_received', 'Offer Received'), 
                                        ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), 
                                        ('canceled', 'Canceled')], string="Status", 
                                        default="new", required=True)
    
    buyer_id = fields.Many2one(comodel_name="res.partner", string="Buyer")

    # Estate details, common to all estate types
    street = fields.Char(string="Street")
    zip = fields.Char(string="Zip", size=24)
    city = fields.Char(string="City")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State")
    country_id = fields.Many2one(comodel_name="res.country", string="Country")
    house_number = fields.Char(string="House Number")

    # House details
    description = fields.Text(string="Description")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (m²)")
    garden_area = fields.Integer(string="Garden Area (m²)")
    garden_orientation = fields.Selection(selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Garden Orientation")
    active = fields.Boolean(string="Active", default=True)

    # Land details
    land_area = fields.Integer(string="Land Area (m²)")
    land_type = fields.Selection(selection=[('building', 'Building'), ('agricultural', 'Agricultural')], string="Land Type")
