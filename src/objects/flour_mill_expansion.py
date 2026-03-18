from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/flour_mill_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# Flour Mill expansion objects
# Row 2 buildings from flour_mill_1.png

# spriteset_building_small [10,60]: small chapel/kiln building
shed = ExpansionObject(
    id="flour_mill_exp_shed",
    numeric_id=308,
    name_string="STR_OBJECT_FLOUR_MILL_SHED",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 60, 64, 82, -31, -52],
    ground_sprite=GROUND,
    height=10,
)

# spriteset_building_big [80,60]: multi-story mill building
mill_building = ExpansionObject(
    id="flour_mill_exp_building",
    numeric_id=309,
    name_string="STR_OBJECT_FLOUR_MILL_BUILDING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 60, 64, 82, -31, -52],
    ground_sprite=GROUND,
    height=10,
)

# spriteset_3 [150,60]: tall grain silos
grain_silo = ExpansionObject(
    id="flour_mill_exp_silo",
    numeric_id=310,
    name_string="STR_OBJECT_FLOUR_MILL_SILO",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 60, 64, 82, -31, -51],
    ground_sprite=GROUND,
    height=10,
)

# spriteset_4 [220,60]: silo with equipment/machinery
silo_equipment = ExpansionObject(
    id="flour_mill_exp_silo_equipment",
    numeric_id=311,
    name_string="STR_OBJECT_FLOUR_MILL_SILO_EQUIPMENT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 60, 64, 82, -31, -51],
    ground_sprite=GROUND,
    height=10,
)
