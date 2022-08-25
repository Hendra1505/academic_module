from odoo import api, models, fields


class Course(models.Model):
    _name = "academic.course"

    name = fields.Char("Name", required=True, size=100)
    description = fields.Text("Description")

    # cara Mengisi fields Many2one dan relasi lainnya dapat menambahkan comodel_name = "nama model"
    # sedangkan cara lainnya yaitu dengan langsung menuliskan "nama model" lalu atribut lain
    # responsible_id = fields.Many2one( "res.users" string="Responsible",required=True )

    responsible_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        required=True)
