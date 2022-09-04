from email.policy import default
from xml.parsers.expat import model
from odoo import models, fields, api
import time


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
    start_date = fields.Date(
        "Start Date", default=lambda self: time.strftime("%Y-%m-%d"))
    duration = fields.Integer("Duration")
    seats = fields.Integer("Seats")
    active = fields.Boolean("Is Active", default=True)

    attendee_ids = fields.One2many(
        comodel_name="academic.attendee", string="Attendees", inverse_name="session_id")

    taken_seats = fields.Float(
        string="Taken Seats", compute="_compute_taken_seats")

    def _compute_taken_seats(self):
        for i in self:
            if i.seats > 0:
                i.taken_seats = 100.0 * len(i.attendee_ids) / i.seats
            else:
                i.taken_seats = 0.0

    @api.onchange("seats")
    def onchange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
        else:
            self.taken_seats = 0.0

    # Field dan fungsi constraint
    # cara 1
    # @api.multi
    # def _cek_instructor(self):
    #     for session in self:

    #         x = []

    #         for attendee in session.attendee_ids:
    #             x.append(attendee.partner_id.id)

    #         if session.instructor_id.id in x:
    #             return False

    #     return True

    # Cara 2 - Lebih efisien
    @api.multi
    def _cek_instructor(self):
        for session in self:

            # Cara penulisannya dimulai dari perulangan ke kanan, lalu kita tangkap record id yang kita inginkan
            x = [attendee.partner_id.id for attendee in session.attendee_ids]

            if session.instructor_id.id in x:
                return False

        return True

    _constraints = [(_cek_instructor,
                     "Instruktur tidak boleh merangkap menjadi attendee - Disini Error message dari validasi constraint",
                     ["instructor_id", "attendee_ids"])]

    @api.multi
    def copy(self, default=None):

        default = dict(default or {}, name=self.name + " (copy)")
        return super(Session, self).copy(default=default)
