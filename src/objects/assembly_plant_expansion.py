from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/assembly_plant_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"

# sp8: offices
offices = ExpansionObject(
    id="assembly_plant_exp_offices",
    numeric_id=336,
    name_string="STR_OBJECT_ASSEMBLY_PLANT_OFFICES",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[500, 10, 64, 80, -31, -49],
    ground_sprite=GROUND,
    height=10,
)

# sp3: central assembly hall
assembly_hall = ExpansionObject(
    id="assembly_plant_exp_hall",
    numeric_id=337,
    name_string="STR_OBJECT_ASSEMBLY_PLANT_HALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 80, -31, -49],
    ground_sprite=GROUND,
    height=10,
)

# sp10: finished vehicles lot
vehicles_lot = ExpansionObject(
    id="assembly_plant_exp_vehicles",
    numeric_id=338,
    name_string="STR_OBJECT_ASSEMBLY_PLANT_VEHICLES",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[640, 10, 64, 80, -31, -49],
    ground_sprite=GROUND,
    height=4,
)
