from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/printing_plant_1.png"
CLASS_ID = "AXSB"
CLASS_NAME = "STR_OBJECT_CLASS_BUILDING_MATERIALS"
GROUND = "GROUNDSPRITE_CONCRETE"

# Building
building = ExpansionObject(
    id="printing_plant_exp_building",
    numeric_id=435,
    name_string="STR_OBJECT_PRINTING_PLANT_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 94, -31, -63],
    ground_sprite=GROUND,
    height=12,
)

# Warehouse
warehouse = ExpansionObject(
    id="printing_plant_exp_warehouse",
    numeric_id=436,
    name_string="STR_OBJECT_PRINTING_PLANT_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[500, 10, 64, 94, -31, -63],
    ground_sprite=GROUND,
    height=12,
)
