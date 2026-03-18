from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/furniture_factory_1.png"
CLASS_ID = "AXSM"
CLASS_NAME = "STR_OBJECT_CLASS_MANUFACTURING"
GROUND = "GROUNDSPRITE_CONCRETE"

# sp2: workshop building
workshop = ExpansionObject(
    id="furniture_factory_exp_workshop",
    numeric_id=345,
    name_string="STR_OBJECT_FURNITURE_FACTORY_WORKSHOP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 60, 64, 88, -31, -44],
    ground_sprite=GROUND,
    height=10,
)

# sp5: warehouse
warehouse = ExpansionObject(
    id="furniture_factory_exp_warehouse",
    numeric_id=346,
    name_string="STR_OBJECT_FURNITURE_FACTORY_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 60, 64, 88, -31, -42],
    ground_sprite=GROUND,
    height=10,
)
