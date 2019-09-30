from odoo import fields, models

class HrEmployee(models.Model):
    _inherit='hr.employee'

    def toggle_active(self):
        self.user_id.toggle_active()
        return super(HrEmployee, self).toggle_active()
class ok(models.Model):
    _inherit='res.users'

    def toggle_active(self):
        self.user_id.write({'active': not self.active})
        return super(ok, self).toggle_active()
