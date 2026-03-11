from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/farm_1.png"
CLASS_ID = "AXPA"
CLASS_NAME = "STR_OBJECT_CLASS_AGRICULTURE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# All farm building sprites are 64x52, offsets -31, -21

barn = ExpansionObject(
    id="farm_exp_barn",
    numeric_id=75,
    name_string="STR_OBJECT_FARM_BARN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

silos = ExpansionObject(
    id="farm_exp_silos",
    numeric_id=76,
    name_string="STR_OBJECT_FARM_SILOS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=10,
)

farmhouse = ExpansionObject(
    id="farm_exp_farmhouse",
    numeric_id=77,
    name_string="STR_OBJECT_FARM_FARMHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

large_barn = ExpansionObject(
    id="farm_exp_large_barn",
    numeric_id=78,
    name_string="STR_OBJECT_FARM_LARGE_BARN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=8,
)

equipment_yard = ExpansionObject(
    id="farm_exp_equipment",
    numeric_id=79,
    name_string="STR_OBJECT_FARM_EQUIPMENT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[290, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=4,
)

farm_tools = ExpansionObject(
    id="farm_exp_tools",
    numeric_id=80,
    name_string="STR_OBJECT_FARM_TOOLS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=4,
)

livestock_pen = ExpansionObject(
    id="farm_exp_pen",
    numeric_id=81,
    name_string="STR_OBJECT_FARM_PEN",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[430, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=4,
)

farm_vehicles = ExpansionObject(
    id="farm_exp_vehicles",
    numeric_id=82,
    name_string="STR_OBJECT_FARM_VEHICLES",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[500, 10, 64, 52, -31, -21],
    ground_sprite=GROUND,
    height=4,
)
