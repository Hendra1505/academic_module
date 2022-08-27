from email.policy import default
from xml.parsers.expat import model
from odoo import models, fields, api


class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)

    # course_id ini berguna untuk foreign key atau sebagai link penghubung dari model course
    # tujuan pada saat ini untuk model course dapat ditampilkan pada session
    course_id = fields.Many2one(
        comodel_name="academic.course", string="Course")

    # cara Mendefinisikan fields Many2one dan relasi lainnya dapat menambahkan comodel_name = "nama model"
    # sedangkan cara lainnya yaitu dengan langsung menuliskan "nama model" lalu atribut lain
    # instructor_id = fields.Many2one("res.partner", string="instructor")

    instructor_id = fields.Many2one("res.partner", string="instructor")
    start_date = fields.Date("Start Date")
    duration = fields.Integer("Duration")
    seats = fields.Integer("Seats")
    active = fields.Boolean("Is Active", default=True)

    attendee_ids = fields.One2many(
        comodel_name="academic.attendee", string="Attendees", inverse_name="session_id")
