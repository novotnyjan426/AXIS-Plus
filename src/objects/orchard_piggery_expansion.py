from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/orchard_piggery_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# Single sprite: 64x59, offsets -31, -28

piggery = ExpansionObject(
    id="piggery_exp_building",
    numeric_id=130,
    name_string="STR_OBJECT_PIGGERY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 59, -31, -28],
    ground_sprite=GROUND,
    height=6,
)
