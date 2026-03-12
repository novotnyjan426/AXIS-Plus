from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/fish_farm_1.png"
CLASS_ID = "AXPP"
CLASS_NAME = "STR_OBJECT_CLASS_PORT_EXPANSIONS"

warehouse = ExpansionObject(
    id="fish_farm_exp_warehouse",
    numeric_id=270,
    name_string="STR_OBJECT_FISH_FARM_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[80, 10, 64, 39, -31, -16],
    ground_sprite="GROUNDSPRITE_CONCRETE",
    height=4,
)

fish_tank = ExpansionObject(
    id="fish_farm_exp_tank",
    numeric_id=271,
    name_string="STR_OBJECT_FISH_FARM_TANK",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 110, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)

fish_tank_full = ExpansionObject(
    id="fish_farm_exp_tank_full",
    numeric_id=272,
    name_string="STR_OBJECT_FISH_FARM_TANK_FULL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 110, 64, 31, -31, 0],
    ground_sprite="GROUNDSPRITE_WATER",
    allow_on_water=True,
)
