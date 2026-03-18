from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/aluminium_plant_1.png"
CLASS_ID = "AXSH"
CLASS_NAME = "STR_OBJECT_CLASS_HEAVY_INDUSTRY"
GROUND = "GROUNDSPRITE_CONCRETE"

# building
building = ExpansionObject(
    id="aluminium_plant_exp_building",
    numeric_id=385,
    name_string="STR_OBJECT_ALUMINIUM_PLANT_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[570, 10, 64, 110, -31, -61],
    ground_sprite=GROUND,
    height=14,
)

# tower
tower = ExpansionObject(
    id="aluminium_plant_exp_tower",
    numeric_id=386,
    name_string="STR_OBJECT_ALUMINIUM_PLANT_TOWER",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 100, -31, -61],
    ground_sprite=GROUND,
    height=12,
)
