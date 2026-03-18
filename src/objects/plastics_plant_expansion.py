from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/plastics_plant_1.png"
CLASS_ID = "AXSC"
CLASS_NAME = "STR_OBJECT_CLASS_CHEMICAL"
GROUND = "GROUNDSPRITE_CONCRETE"

# 2x2 factory block: sp8+sp7 (top), sp8+sp6 (bottom)
factory = ExpansionObject(
    id="plastics_plant_exp_factory",
    numeric_id=373,
    name_string="STR_OBJECT_PLASTICS_PLANT_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    size=[2, 2],
    ground_sprite=GROUND,
    height=10,
    tile_grid=[
        {"x": 0, "y": 0, "buildings": [{"coords": [500, 10, 64, 87, -31, -56]}]},  # sp8
        {"x": 1, "y": 0, "buildings": [{"coords": [430, 10, 64, 87, -31, -56]}]},  # sp7
        {"x": 0, "y": 1, "buildings": [{"coords": [500, 10, 64, 87, -31, -56]}]},  # sp8
        {"x": 1, "y": 1, "buildings": [{"coords": [360, 10, 64, 87, -31, -56]}]},  # sp6
    ],
)
