from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/recycling_depot_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "GROUNDSPRITE_CONCRETE"

shed = ExpansionObject(
    id="recycling_depot_exp_shed",
    numeric_id=290,
    name_string="STR_OBJECT_RECYCLING_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 31, -31, 0],
    ground_sprite=GROUND,
    height=4,
)

containers = ExpansionObject(
    id="recycling_depot_exp_containers",
    numeric_id=291,
    name_string="STR_OBJECT_RECYCLING_CONTAINERS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 31, -31, 0],
    ground_sprite=GROUND,
    height=4,
)
