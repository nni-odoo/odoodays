# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Course(models.Model):
    _name = "course.course"

    name = fields.Char()
    code = fields.Char()
    seats = fields.Integer(default=60)

    start_date = fields.Datetime()
    duration = fields.Float()
    description = fields.Text()

    lecturer = fields.Many2one("res.partner")

    attendees = fields.Many2many("res.partner")
    seats_left = fields.Integer("Seats Left", compute="_compute_seats_left")

    @api.depends('seats', 'attendees')
    def _compute_seats_left(self):
        for record in self:
            record.seats_left = record.seats - len(record.attendees)

    def attend_course(self):
        # adding current user to list of a
        user = self.env.user
        self.attendees |= user.partner_id

    @api.model
    def create(self, vals):
        if not vals.get('description'):
            vals['description'] = "%s - %s" % (vals['code'], vals['name'])
        return super().create(vals)
