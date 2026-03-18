from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/wire_and_section_mill_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"

# factory
factory = ExpansionObject(
    id="wire_section_mill_exp_factory",
    numeric_id=411,
    name_string="STR_OBJECT_WIRE_SECTION_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
    height=8,
)

# workshop
workshop = ExpansionObject(
    id="wire_section_mill_exp_workshop",
    numeric_id=412,
    name_string="STR_OBJECT_WIRE_SECTION_WORKSHOP",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 64, -31, -33],
    ground_sprite=GROUND,
    height=8,
)
