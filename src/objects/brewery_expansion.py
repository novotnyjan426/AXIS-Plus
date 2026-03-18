from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/brewery_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"
SMOKE = "3701 + (animation_frame % 8)"

# Chimney building (sp1) with fast smoke
chimney_building = ExpansionObject(
    id="brewery_exp_chimney",
    numeric_id=328,
    name_string="STR_OBJECT_BREWERY_CHIMNEY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[1, 1],
    ground_sprite=GROUND,
    height=12,
    animation_length=8,
    animation_speed=3,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [
            {"coords": [10, 60, 64, 91, -31, -60]},
            {"sprite_expr": SMOKE, "xoffset": 8, "yoffset": 0, "zoffset": 55,
             "xextent": 15, "yextent": 7, "zextent": 7},
        ]},
    ],
)

# 2x1 brewery hall: sp3 (back) + sp2 frame 1 (front)
# sp2 is animated in original but we use static frame for expansion
hall = ExpansionObject(
    id="brewery_exp_hall",
    numeric_id=329,
    name_string="STR_OBJECT_BREWERY_HALL",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 1],
    ground_sprite=GROUND,
    height=12,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [150, 60, 64, 91, -31, -60]}]},  # sp3 back
        {"x": 1, "y": 0, "buildings": [{"coords": [80, 60, 64, 91, -31, -60]}]},   # sp2 front
    ],
)
