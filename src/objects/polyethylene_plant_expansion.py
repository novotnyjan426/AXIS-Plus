from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/polyethylene_plant_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"

# sp1: tall tower
tower = ExpansionObject(
    id="polyethylene_plant_exp_tower",
    numeric_id=375,
    name_string="STR_OBJECT_POLYETHYLENE_PLANT_TOWER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 114, -31, -88],
    ground_sprite=GROUND,
    height=14,
)
