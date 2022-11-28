from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    school_category = fields.Selection([('student', 'Student'), ('teacher', 'Teacher')])
    courses = fields.Many2many("course.course")
    courses_taught = fields.One2many("course.course", "lecturer")
