from email.policy import default
from xml.parsers.expat import model
from odoo import models, fields, api


class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)
    course_id = fields.Many2one(
        comodel_name="academic.course", string="Course")

    # cara Mengisi fields Many2one dan relasi lainnya dapat menambahkan comodel_name = "nama model"
    # sedangkan cara lainnya yaitu dengan langsung menuliskan "nama model" lalu atribut lain
    # instructor_id = fields.Many2one("res.partner", string="instructor")

    instructor_id = fields.Many2one("res.partner", string="instructor")
    start_date = fields.Date("Start Date")
    duration = fields.Integer("Duration")
    seats = fields.Integer("Seats")
    active = fields.Boolean("Is Active", default=True)
