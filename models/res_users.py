from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    dog_name = fields.Char(
        string='Nome del cane',
        help='Nome del cane dell\'utente'
    )
    
    dog_breed = fields.Selection([
        ('akita', 'Akita'),
        ('alano', 'Alano'),
        ('barboncino', 'Barboncino'),
        ('bassethound', 'Basset Hound'),
        ('bassotto', 'Bassotto'),
        ('beagle', 'Beagle'),
        ('bergamasco', 'Pastore Bergamasco'),
        ('bichon', 'Bichon Frisé'),
        ('border_collie', 'Border Collie'),
        ('boston_terrier', 'Boston Terrier'),
        ('boxer', 'Boxer'),
        ('bracco', 'Bracco Italiano'),
        ('bulldog_francese', 'Bulldog Francese'),
        ('bulldog_inglese', 'Bulldog Inglese'),
        ('bull_terrier', 'Bull Terrier'),
        ('cane_corso', 'Cane Corso'),
        ('carlino', 'Carlino'),
        ('cavalier', 'Cavalier King Charles Spaniel'),
        ('chihuahua', 'Chihuahua'),
        ('chow_chow', 'Chow Chow'),
        ('cocker', 'Cocker Spaniel'),
        ('collie', 'Collie'),
        ('dalmata', 'Dalmata'),
        ('dobermann', 'Dobermann'),
        ('dogo_argentino', 'Dogo Argentino'),
        ('golden_retriever', 'Golden Retriever'),
        ('husky', 'Siberian Husky'),
        ('jack_russell', 'Jack Russell Terrier'),
        ('labrador', 'Labrador Retriever'),
        ('lagotto', 'Lagotto Romagnolo'),
        ('levriero', 'Levriero'),
        ('maltese', 'Maltese'),
        ('maremmano', 'Pastore Maremmano'),
        ('mastino', 'Mastino Napoletano'),
        ('meticcio', 'Meticcio'),
        ('pastore_australiano', 'Pastore Australiano'),
        ('pastore_tedesco', 'Pastore Tedesco'),
        ('pechinese', 'Pechinese'),
        ('pinscher', 'Pinscher'),
        ('pitbull', 'Pitbull'),
        ('pointer', 'Pointer'),
        ('pomerania', 'Volpino di Pomerania'),
        ('rottweiler', 'Rottweiler'),
        ('san_bernardo', 'San Bernardo'),
        ('schnauzer', 'Schnauzer'),
        ('setter', 'Setter'),
        ('shar_pei', 'Shar Pei'),
        ('shiba_inu', 'Shiba Inu'),
        ('shih_tzu', 'Shih Tzu'),
        ('spinone', 'Spinone Italiano'),
        ('springer_spaniel', 'Springer Spaniel'),
        ('staffordshire', 'Staffordshire Bull Terrier'),
        ('terranova', 'Terranova'),
        ('tibetan_terrier', 'Tibetan Terrier'),
        ('volpino', 'Volpino Italiano'),
        ('weimaraner', 'Weimaraner'),
        ('west_highland', 'West Highland White Terrier'),
        ('yorkshire', 'Yorkshire Terrier'),
        ('altro', 'Altra razza')
    ], string='Razza del cane', help='Razza del cane dell\'utente')
    
    dog_age = fields.Integer(
        string='Età del cane (anni)',
        help='Età del cane in anni'
    )
    
    dog_weight = fields.Float(
        string='Peso del cane (kg)',
        help='Peso del cane in chilogrammi',
        digits=(8, 2)
    )

    @api.model
    def create(self, vals):
        user = super(ResUsers, self).create(vals)
        if user.partner_id:
            partner_vals = {}
            if 'dog_name' in vals:
                partner_vals['dog_name'] = vals['dog_name']
            if 'dog_breed' in vals:
                partner_vals['dog_breed'] = vals['dog_breed']
            if 'dog_age' in vals:
                partner_vals['dog_age'] = vals['dog_age']
            if 'dog_weight' in vals:
                partner_vals['dog_weight'] = vals['dog_weight']
            
            if partner_vals:
                user.partner_id.write(partner_vals)
        
        return user

    def write(self, vals):
        res = super(ResUsers, self).write(vals)
        
        partner_vals = {}
        if 'dog_name' in vals:
            partner_vals['dog_name'] = vals['dog_name']
        if 'dog_breed' in vals:
            partner_vals['dog_breed'] = vals['dog_breed']
        if 'dog_age' in vals:
            partner_vals['dog_age'] = vals['dog_age']
        if 'dog_weight' in vals:
            partner_vals['dog_weight'] = vals['dog_weight']
        
        if partner_vals:
            for user in self:
                if user.partner_id:
                    user.partner_id.write(partner_vals)
        
        return res