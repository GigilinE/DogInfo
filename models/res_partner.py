from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_studio_dog_name = fields.Char(
        string='Nome del cane',
        help='Nome del cane del contatto'
    )
    
    x_studio_dog_breed = fields.Selection([
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
    ], string='Razza del cane', help='Razza del cane del contatto')
    
    x_studio_dog_age = fields.Integer(
        string='Età del cane (anni)',
        help='Età del cane in anni'
    )
    
    x_studio_dog_weight = fields.Float(
        string='Peso del cane (kg)',
        help='Peso del cane in chilogrammi',
        digits=(8, 2)
    )