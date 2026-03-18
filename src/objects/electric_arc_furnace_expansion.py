from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/electric_arc_furnace_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"

# shed
shed = ExpansionObject(
    id="electric_arc_furnace_exp_shed",
    numeric_id=395,
    name_string="STR_OBJECT_EAF_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=14,
)

# tanks
tanks = ExpansionObject(
    id="electric_arc_furnace_exp_tanks",
    numeric_id=396,
    name_string="STR_OBJECT_EAF_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 122, -31, -90],
    ground_sprite=GROUND,
    height=14,
)
