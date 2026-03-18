from objects.base_object import ExpansionObject

SPRITE_FILE = "src/graphics/industries/food_processor_1.png"
CLASS_ID = "AXSF"
CLASS_NAME = "STR_OBJECT_CLASS_FOOD_PROCESSING"
GROUND = "GROUNDSPRITE_CONCRETE"

# Food Processor / Cannery expansion objects
# sprite coords from food_processor.py spritesets

factory = ExpansionObject(
    id="food_processor_exp_factory",
    numeric_id=312,
    name_string="STR_OBJECT_FOOD_PROCESSOR_FACTORY",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[10, 10, 64, 87, -31, -56],
    ground_sprite=GROUND,
    height=12,
)

tanks = ExpansionObject(
    id="food_processor_exp_tanks",
    numeric_id=313,
    name_string="STR_OBJECT_FOOD_PROCESSOR_TANKS",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[150, 10, 64, 87, -31, -56],
    ground_sprite=GROUND,
    height=12,
)

loading_dock = ExpansionObject(
    id="food_processor_exp_loading",
    numeric_id=314,
    name_string="STR_OBJECT_FOOD_PROCESSOR_LOADING",
    class_id=CLASS_ID,
    class_name_string=CLASS_NAME,
    sprite_file=SPRITE_FILE,
    sprite_coords=[220, 10, 64, 87, -31, -56],
    ground_sprite=GROUND,
    height=12,
)
