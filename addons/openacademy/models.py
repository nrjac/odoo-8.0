
from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

class shif(models.Model):
    _name =  'openacademy.shift'
    name =fields.Char(string="title", required=True)
    shift = fields.Text(string="DayOrMorning", required=True)


