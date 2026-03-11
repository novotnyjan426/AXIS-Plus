from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/tar_sands_mine_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"

# Complete tar sands open pit — 5x3 multi-tile object
# Replicates industry layout_1 pit section (y=1..3)
# Ground overlays are childsprites on GROUNDSPRITE_NORMAL
# Building sprites (conveyors, crane, pile, bulldozer) on top where applicable
pit = ExpansionObject(
    id="tar_sands_exp_pit",
    numeric_id=203,
    name_string="STR_OBJECT_TAR_SANDS_PIT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[5, 3],
    ground_sprite="GROUNDSPRITE_NORMAL",
    height=2,
    tile_grid=[
        # Row y=0: top edge of pit (industry y=1)
        {"x": 0, "y": 0, "sprite": [290, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [290, 130, 64, 64, -31, -22]}]},      # pit_conveyor_4
        {"x": 1, "y": 0, "sprite": [220, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [220, 130, 64, 64, -31, -22]}]},      # pit_conveyor_3
        {"x": 2, "y": 0, "sprite": [150, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [150, 130, 64, 64, -31, -22]}]},      # pit_conveyor_2
        {"x": 3, "y": 0, "sprite": [80, 10, 64, 31, -31, 0],
         "buildings": [{"coords": [80, 130, 64, 64, -31, -22]}]},       # pit_conveyor_1
        {"x": 4, "y": 0, "sprite": [10, 10, 64, 31, -31, 0]},

        # Row y=1: middle of pit (industry y=2)
        {"x": 0, "y": 1, "sprite": [290, 50, 64, 31, -31, 0]},
        {"x": 1, "y": 1, "sprite": [220, 50, 64, 31, -31, 0]},
        {"x": 2, "y": 1, "sprite": [150, 50, 64, 31, -31, 0]},
        {"x": 3, "y": 1, "sprite": [80, 50, 64, 31, -31, 0],
         "buildings": [{"coords": [440, 90, 64, 31, -31, 0]}]},         # bulldozer
        {"x": 4, "y": 1, "sprite": [10, 50, 64, 31, -31, 0]},

        # Row y=2: bottom of pit (industry y=3)
        {"x": 0, "y": 2, "sprite": [290, 90, 64, 31, -31, 0]},
        {"x": 1, "y": 2, "sprite": [220, 90, 64, 31, -31, 0],
         "buildings": [                                                   # crane + pile
             {"coords": [440, 10, 64, 71, -48, -55]},
             {"coords": [360, 50, 64, 31, -63, -16]},
         ]},
        {"x": 2, "y": 2, "sprite": [150, 90, 64, 31, -31, 0]},
        {"x": 3, "y": 2, "sprite": [80, 90, 64, 31, -31, 0],
         "buildings": [{"coords": [10, 130, 64, 64, -31, -22]}]},       # pit_conveyor_0
        {"x": 4, "y": 2, "sprite": [10, 90, 64, 31, -31, 0]},
    ],
)
