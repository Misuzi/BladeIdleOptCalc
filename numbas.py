import numpy as np

# If you don't want to consider one of these for any reason, 
# I.E. PEN/ACU rolls, not acquired yet, etc., just comment
# out the line

option_matrix = np.array([
#    OPTION_ATK | SPR_OPTATK | CRITDMG___ | SPRCRITDMG | HYPCRITDMG
    [200,         0,           0,           800,         0         ], # G1 Weapon ALL IN ONE (4)
    [100,         0,           0,           800,         0         ], # G1 Gloves ALL IN ONE (4)
    [100,         0,           0,           800,         0         ], # G1 Armor  ALL IN ONE (4)
    [100,         0,           0,           800,         0         ], # G1 Helmet ALL IN ONE (4)
#    [400,         0,           0,           0,           0         ], # Skin - Celestial Guardian ALL IN ONE (5)
#    [450,         0,           0,           0,           0         ], # Skin - Black Blood Priest ALL IN ONE (5)
    [500,         40,          0,           0,           0         ], # Skin - The First Creator ALL IN ONE (5)
    [120,         0,           240,         0,           0         ], # Accessory - Ring 4 - Onyx Ring ALL IN ONE (3)
#    [45,          0,           80,          0,           0         ], # Accessory - Ring 7 - Erised Ring ALL IN ONE (3)
    [120,         0,           240,         0,           0         ], # Accessory - Ring 8 - Paladin Ring ALL IN ONE (3)
    [120,         0,           240,         0,           0         ], # Accessory - Earring 4 - Elifea Earring ALL IN ONE (3)
    [120,         0,           240,         0,           0         ], # Accessory - Earring 5 - Pentadium Earring ALL IN ONE (3)
    [120,         0,           240,         0,           0         ], # Accessory - Earring 8 - Amber Owl Earring ALL IN ONE (3)
    [120,         0,           240,         0,           0         ], # Accessory - Hairpin 4 - Dragon Pin ALL IN ONE (3)
    [45,          0,           80,          0,           0         ], # Accessory - Hairpin 6 - Peridot Pin ALL IN ONE (3)
    [120,         0,           240,         0,           0         ], # Accessory - Hairpin 8 - Gold Maharaja Pin ALL IN ONE (3)
    [450,         0,           0,           1000,        0         ], # Sword of Ego ALL IN ONE (5)
    #TODO
])

name_array = [
    "G1 Weapon ALL IN ONE (4)",
    "G1 Gloves ALL IN ONE (4)",
    "G1 Armor  ALL IN ONE (4)",
    "G1 Helmet ALL IN ONE (4)",
#    "Skin - Celestial Guardian ALL IN ONE (5)",
#    "Skin - Black Blood Priest ALL IN ONE (5)",
    "Skin - The First Creator ALL IN ONE (5)",
    "Accessory - Ring 4 - Onyx Ring ALL IN ONE (3)",
#    "Accessory - Ring 7 - Erised Ring ALL IN ONE (3)",
    "Accessory - Ring 8 - Paladin Ring ALL IN ONE (3)",
    "Accessory - Earring 4 - Elifea Earring ALL IN ONE (3)",
    "Accessory - Earring 5 - Pentadium Earring ALL IN ONE (3)",
    "Accessory - Earring 8 - Amber Owl Earring ALL IN ONE (3)",
    "Accessory - Hairpin 4 - Dragon Pin ALL IN ONE (3)",
    "Accessory - Hairpin 6 - Peridot Pin ALL IN ONE (3)",
    "Accessory - Hairpin 8 - Gold Maharaja Pin ALL IN ONE (3)",
    "Sword of Ego ALL IN ONE (5)",
]

# Precision version if you don't want to roll the same option on each roll for one piece of equipment
'''
option_matrix = np.array([
#    OPTION_ATK | SPR_OPTATK | CRITDMG___ | SPRCRITDMG | HYPCRITDMG
    [50,          0,           0,           200,         0         ], # G1 Weapon 1
    [50,          0,           0,           200,         0         ], # G1 Weapon 2
    [50,          0,           0,           200,         0         ], # G1 Weapon 3
    [50,          0,           0,           200,         0         ], # G1 Weapon 4
    [200,         0,           0,           800,         0         ], # G1 Weapon ALL IN ONE
    [25,          0,           0,           200,         0         ], # G1 Gloves 1
    [25,          0,           0,           200,         0         ], # G1 Gloves 2
    [25,          0,           0,           200,         0         ], # G1 Gloves 3
    [25,          0,           0,           200,         0         ], # G1 Gloves 4
    [25,          0,           0,           200,         0         ], # G1 Armor
    [25,          0,           0,           200,         0         ], # G1 Helmet
#    [80,          0,           0,           0,           0         ], # Skin - Celestial Guardian
#    [90,          0,           0,           0,           0         ], # Skin - Black Blood Priest
    [100,         8,           0,           0,           0         ], # Skin - The First Creator
    [40,          8,           80,          0,           0         ], # Accessory - Ring 4 - Onyx Ring
#    [15,          8,           26.67,       0,           0         ], # Accessory - Ring 5 - Erised Ring 
    [40,          8,           80,          0,           0         ], # Accessory - Ring 8 - Paladin Ring
    [40,          8,           80,          0,           0         ], # Accessory - Earring 4 - Elifea Earring
    [40,          8,           80,          0,           0         ], # Accessory - Earring 5 - Pentadium Earring
    [40,          8,           80,          0,           0         ], # Accessory - Earring 5 - Pentadium Earring
    [40,          8,           80,          0,           0         ], # Accessory - Earring 8 - Amber Owl Earring
    #TODO
])
'''