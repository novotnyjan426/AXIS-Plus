from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/salt_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"

# 5x3 open pit — same sprite layout as bauxite/phosphate, different PNG
pit = ExpansionObject(
    id="salt_mine_exp_pit",
    numeric_id=253,
    name_string="STR_OBJECT_SALT_MINE_PIT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[5, 3],
    ground_sprite="GROUNDSPRITE_NORMAL",
    height=2,
    tile_grid=[
        # Row y=0: top edge of pit
        {"x": 0, "y": 0, "sprite": [290, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [290, 130, 64, 64, -31, -22]}]},
        {"x": 1, "y": 0, "sprite": [220, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [220, 130, 64, 64, -31, -22]}]},
        {"x": 2, "y": 0, "sprite": [150, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [150, 130, 64, 64, -31, -22]}]},
        {"x": 3, "y": 0, "sprite": [80, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [80, 130, 64, 64, -31, -22]}]},
        {"x": 4, "y": 0, "sprite": [10, 10, 64, 31, -31, 0]},

        # Row y=1: middle of pit
        {"x": 0, "y": 1, "sprite": [290, 50, 64, 31, -31, 0]},
        {"x": 1, "y": 1, "sprite": [220, 50, 64, 31, -31, 0]},
        {"x": 2, "y": 1, "sprite": [150, 50, 64, 31, -31, 0]},
        {"x": 3, "y": 1, "sprite": [80, 50, 64, 31, -31, 0],
         "buildings": [{"coords": [440, 90, 64, 31, -31, 0]}]},
        {"x": 4, "y": 1, "sprite": [10, 50, 64, 31, -31, 0]},

        # Row y=2: bottom of pit
        {"x": 0, "y": 2, "sprite": [290, 90, 64, 31, -31, 0]},
        {"x": 1, "y": 2, "sprite": [220, 90, 64, 31, -31, 0],
         "buildings": [
             {"coords": [440, 10, 64, 71, -48, -55]},
             {"coords": [360, 50, 64, 31, -63, -16]},
         ]},
        {"x": 2, "y": 2, "sprite": [150, 90, 64, 31, -31, 0]},
        {"x": 3, "y": 2, "sprite": [80, 90, 64, 31, -31, 0],
         "buildings": [{"coords": [10, 130, 64, 64, -31, -22]}]},
        {"x": 4, "y": 2, "sprite": [10, 90, 64, 31, -31, 0]},
    ],
)
