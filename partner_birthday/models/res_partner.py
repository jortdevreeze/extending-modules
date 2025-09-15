from datetime import date

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=False)
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        """Calculate age based on date of birth"""
        today = date.today()
        for partner in self:
            if partner.date_of_birth:
                # Calculate age
                born = partner.date_of_birth
                age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                partner.age = age
            else:
                partner.age = 0
    
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        """Ensure date of birth is not in the future"""
        today = date.today()
        for partner in self:
            if partner.date_of_birth and partner.date_of_birth > today:
                raise ValidationError(_("Date of birth cannot be in the future."))
    
    def check_birthdays_today(self):
        """Check for partners with birthdays today and notify the responsible salesperson"""
        today = date.today()
        domain = [
            ('date_of_birth', '!=', False),
            ('user_id', '!=', False),  # Has a salesperson assigned
            ('type', '=', 'contact'),  # Only contacts, not addresses
        ]
        partners = self.search(domain)
        
        for partner in partners:
            dob = partner.date_of_birth
            if dob.day == today.day and dob.month == today.month:
                # It's this partner's birthday!
                salesperson = partner.user_id
                age = partner.age
                
                # Create a note/activity for the salesperson
                partner.activity_schedule(
                    'mail.mail_activity_data_todo',
                    summary=_("Birthday Reminder"),
                    note=_("Today is %s's birthday! They are turning %s years old. Don't forget to congratulate them!") 
                         % (partner.name, age),
                    user_id=salesperson.id,
                )
