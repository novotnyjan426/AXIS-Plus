from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/edible_oil_refinery_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# 2x1 warehouse matching layout positions (0,0)=sp2 + (1,0)=sp1
warehouse = ExpansionObject(
    id="edible_oil_exp_warehouse",
    numeric_id=326,
    name_string="STR_OBJECT_EDIBLE_OIL_WAREHOUSE",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 1],
    ground_sprite=GROUND,
    height=10,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [80, 10, 64, 76, -31, -45]}]},   # sp2
        {"x": 1, "y": 0, "buildings": [{"coords": [10, 10, 64, 76, -31, -45]}]},   # sp1
    ],
)

# sp4: wooden crates/loading area (tile 1,1 from original layout)
loading_yard = ExpansionObject(
    id="edible_oil_exp_loading",
    numeric_id=327,
    name_string="STR_OBJECT_EDIBLE_OIL_LOADING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 63, -31, -32],
    ground_sprite=GROUND,
    height=8,
)

# sp6: storage tanks
tanks = ExpansionObject(
    id="edible_oil_exp_tanks",
    numeric_id=332,
    name_string="STR_OBJECT_EDIBLE_OIL_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[360, 10, 64, 63, -31, -32],
    ground_sprite=GROUND,
    height=8,
)
