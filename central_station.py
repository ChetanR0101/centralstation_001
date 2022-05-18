from xmlrpc.client import Boolean
from odoo import models,fields,api
from odoo.exceptions import ValidationError


class CentralStation_substation(models.Model):
    _name= "central.substation"
    _description="Central Station - SubStation"
    name= fields.Char("SubStation Name")
    price=fields.Float("Fuel Price")
    manager= fields.Char("Manager Name")
    sub_add=fields.Char("Sub Station Address")


class CentralStation_transaction_in(models.Model):
    _name= "central.transaction_in"
    name= fields.Char("Recived By")
    date= fields.Datetime("Date")
    fuel_type= fields.Many2one(string="Fuel Type", comodel_name="central.data")
    sub_station=fields.Many2one(string="SubStation Name", comodel_name="central.substation")
    instock_qut=fields.Float("Fuel Quantity")
    tanker_rec_id=fields.Integer("Tanker Record Id")

class CentralStation_transaction_out(models.Model):
    _name= "central.transaction_out"
    name=fields.Char("Customer Name")
    date=fields.Datetime("Date")
    fuel_type=fields.Many2one(string="Fuel Type", comodel_name="central.data")
    sub_station=fields.Many2one(string="SubStation Name", comodel_name="central.substation")
    order_qut=fields.Float("Fuel Quantity")
    price=fields.Float("Fuel Price")
    total_price=fields.Float("Total Cost")

    

class CentralStation_data(models.Model):
    _name= "central.data"
    name=fields.Char("Fuel Type")
    substation_name=fields.Many2one(string="SubStation Name", comodel_name="central.substation")
    fuel_qut= fields.Float("Fuel Quantity")
    price=fields.Float("Fuel Price")

class CentralStation_tanker(models.Model):
    _name="central.tanker"
    name= fields.Many2one(string="Tanker No.",comodel_name="central.tanker_details")
    starting_pt= fields.Char(string="Source", default="Central Station")
    dest= fields.Many2one(string="Destination", comodel_name="central.substation")
    fuel_type= fields.Many2one(string="Fuel Type", comodel_name="central.data")
    vol=fields.Float("Volume Carried")
    status=fields.Selection([("dispatch", "Dispatched"),("on_way","On the Way"),("delivered","Delivered"),("late","Delayed")] ,string="Tanker Status", default="dispatch" ,required=True)
    tanker_rec_id=fields.Integer(string="Tanker Record Id")
    
    # To generate tanker record id
    @api.model
    def create(self, vals_list):
        res= super(CentralStation_tanker,self).create(vals_list)
        res.tanker_rec_id=res.id
        return res

# for tanker details
class CentralStation_tanker_details(models.Model):
    _name="central.tanker_details"
    name=fields.Char("Tanker NO.")
    tanker_reg_no=fields.Char("Tanker Registration  NO.")
    tanker_cap=fields.Float("Tanker Capacity")
    driver_name= fields.Char("Driver Name")
    driver_add= fields.Char("Driver Address")
    driver_contact_no= fields.Integer("Driver Contact No.")

#  SubStation Models
# class CentralStation_substation1(models.Model):
#     _name= "central.substation1"
#     name= fields.Char("Manager Name")
#     sub_add=fields.Char("Sub Station Address")
    

# class CentralStation_substation1(models.Model):
#     _name= "central.substation2"
#     name= fields.Char("Manager Name")
#     sub_add=fields.Char("Sub Station Address")


# class CentralStation_substation1(models.Model):
#     _name= "central.substation3"
#     name= fields.Char("Manager Name")
#     sub_add=fields.Char("Sub Station Address")
