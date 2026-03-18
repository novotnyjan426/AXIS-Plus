from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/junk_yard_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"

# Shed
shed = ExpansionObject(
    id="junk_yard_exp_shed",
    numeric_id=429,
    name_string="STR_OBJECT_JUNK_YARD_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 55, -31, -24],
    ground_sprite=GROUND,
    height=6,
)

# Scrap pile
scrap = ExpansionObject(
    id="junk_yard_exp_scrap",
    numeric_id=430,
    name_string="STR_OBJECT_JUNK_YARD_SCRAP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 55, -31, -24],
    ground_sprite=GROUND,
    height=6,
)
