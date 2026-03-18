from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/builders_yard_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"

# Shed
shed = ExpansionObject(
    id="builders_yard_exp_shed",
    numeric_id=423,
    name_string="STR_OBJECT_BUILDERS_YARD_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 56, -31, -26],
    ground_sprite=GROUND,
    height=6,
)

# Silo
silo = ExpansionObject(
    id="builders_yard_exp_silo",
    numeric_id=424,
    name_string="STR_OBJECT_BUILDERS_YARD_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 64, -31, -34],
    ground_sprite=GROUND,
    height=8,
)
