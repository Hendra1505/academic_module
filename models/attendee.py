from odoo import api, models, fields


class Attendee(models.Model):
    _name = "academic.attendee"

    name = fields.Char("Reg Number", required=True, size=100)

    # cara Mendefinisikan fields Many2one dan relasi lainnya dapat menambahkan comodel_name = "nama model"
    # sedangkan cara lainnya yaitu dengan langsung menuliskan "nama model" lalu atribut lain
    # contoh_nama_fieldnya = fields.Many2one( "res.users" string="Responsible", required=True, dan seterusnya )
    session_id = fields.Many2one(
        comodel_name="academic.session", string="Session")

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner")

    # Constraint atau validasi dengan cara sql constraint
    _sql_constraints = [('sql_cek_attendee', 'UNIQUE(session_id, partner_id)',
                         'Attendee tidak boleh double dalam 1 session!')]
