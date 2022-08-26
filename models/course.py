from odoo import api, models, fields


class Course(models.Model):
    _name = "academic.course"

    name = fields.Char("Name", required=True, size=100)
    description = fields.Text("Description")

    # cara Mendefinisikan fields Many2one dan relasi lainnya dapat menambahkan comodel_name = "nama model"
    # sedangkan cara lainnya yaitu dengan langsung menuliskan "nama model" lalu atribut lain
    # responsible_id = fields.Many2one( "res.users" string="Responsible",required=True )
    responsible_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        required=True)

    # cara Mendefinisikan fields One2many dan relasi lainnya dapat menambahkan comodel_name = "nama model" atau langsung dengan menuliskan "nama model nya"
    # namun bedanya pada One2many di perlukan juga field atau atribut inverse_name = "nama foreign key atau field yang menghubungkan antara academic.course dengan academic.session"
    # dan juga berikut penulisan lainnya untuk One2many
    # session_ids = fields.One2many( "academic.session" string="Session", inverse_name="course_id", dan atribut seterusnya )
    session_ids = fields.One2many(
        comodel_name="academic.session",
        string="Session",
        inverse_name="course_id")
