from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/clay_pit_1.png"
CLASS_ID = "AXPM"
CLASS_NAME = "STR_OBJECT_CLASS_MINE_EXPANSIONS"
GROUND = "GROUNDSPRITE_NORMAL"

# Complete clay open pit — 5x3 multi-tile object
# Replicates industry layout_1 pit area (rows 1-3):
#   Row y=0: top edge of pit with conveyor buildings
#   Row y=1: middle of pit, excavator at (3,1)
#   Row y=2: bottom of pit, crane+pile at (1,2), conveyor at (3,2)
# Ground overlays are childsprites on GROUNDSPRITE_NORMAL
# Building sprites (conveyors, crane, pile, excavator) on top where applicable
pit = ExpansionObject(
    id="clay_exp_pit",
    numeric_id=40,
    name_string="STR_OBJECT_CLAY_PIT",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[5, 3],
    ground_sprite=GROUND,
    height=2,
    tile_grid=[
        # Row y=0: top edge of pit
        {"x": 0, "y": 0, "sprite": [290, 10, 64, 31, -31, 0],          # ground overlay
         "buildings": [{"coords": [290, 130, 64, 64, -31, -22]}]},      # conveyor (same as industry)
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
         "buildings": [{"coords": [440, 90, 64, 31, -31, 0]}]},         # excavator
        {"x": 4, "y": 1, "sprite": [10, 50, 64, 31, -31, 0]},

        # Row y=2: bottom of pit
        {"x": 0, "y": 2, "sprite": [290, 90, 64, 31, -31, 0]},
        {"x": 1, "y": 2, "sprite": [220, 90, 64, 31, -31, 0],
         "buildings": [                                                   # crane + pile
             {"coords": [440, 10, 64, 71, -48, -55]},
             {"coords": [360, 50, 64, 31, -63, -16]},
         ]},
        {"x": 2, "y": 2, "sprite": [150, 90, 64, 31, -31, 0]},
        {"x": 3, "y": 2, "sprite": [80, 90, 64, 31, -31, 0],
         "buildings": [{"coords": [10, 130, 64, 64, -31, -22]}]},       # conveyor
        {"x": 4, "y": 2, "sprite": [10, 90, 64, 31, -31, 0]},
    ],
)
