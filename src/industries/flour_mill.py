from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="flour_mill",
    accept_cargos_with_input_ratios=[("GRAI", 6), ("MNSP", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("FOOD", 6)],
    prob_map_gen="10",
    prob_in_game="10",
    map_colour="49",
    name="string(STR_IND_FLOUR_MILL)",
    nearby_station_name="string(STR_STATION_MILL)",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["arable_farm", "farm"],
            72,
        ]
    ),
    fund_cost_multiplier="50",
    base_processing_cap=32,
    required_input_cargos=["GRAI"],
    scale_bonus_cargos=[("EOIL", {"low": 2, "medium": 3, "high": 4})],
)

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].accept_cargos_with_input_ratios = [
    ("GRAI", 6),
    ("MNSP", 2),
]
industry.economy_variations["BASIC_TROPIC"].prod_cargo_types_with_output_ratios = [
    ("BAKE", 6),
]

industry.economy_variations["STEELTOWN"].enabled = True


industry.economy_variations["BASIC_TEMPERATE"].enabled = True
industry.economy_variations["BASIC_TEMPERATE"].prod_cargo_types_with_output_ratios = [
    ("FOOD", 6),
    ("EOIL", 4),
]


industry.add_tile(
    id="flour_mill_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground_bakery = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(sprites=[(80, 10, 64, 31, -31, 0)])
spriteset_ground_overlay_3 = industry.add_spriteset(sprites=[(150, 10, 64, 31, -31, 0)])
spriteset_ground_overlay_4 = industry.add_spriteset(sprites=[(220, 10, 64, 31, -31, 0)])
spriteset_1 = industry.add_spriteset(sprites=[(10, 10, 64, 31, -31, 0)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 10, 64, 31, -31, 0)])
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 82, -31, -51)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 82, -31, -51)],
)
# animated spriteset defined first so others can copy num. frames
spriteset_windmill_anim = industry.add_spriteset(
    sprites=[
        (10, 200, 64, 82, -31, -52),
        (80, 200, 64, 82, -31, -52),
        (150, 200, 64, 82, -31, -52),
        (220, 200, 64, 82, -31, -52),
        (290, 200, 64, 82, -31, -52),
        (360, 200, 64, 82, -31, -52),
    ],
    animation_rate=1,
)
spriteset_ground_windmill = industry.add_spriteset(
    type="dirty_concrete",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_windmill = industry.add_spriteset(
    sprites=[(150, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_building_big = industry.add_spriteset(
    sprites=[(80, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_building_big = industry.add_spriteset(
    sprites=[(80, 60, 64, 82, -31, -52)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_building_small = industry.add_spriteset(
    sprites=[(10, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_building_small = industry.add_spriteset(
    sprites=[(10, 60, 64, 82, -31, -52)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_windmill_greeble = industry.add_spriteset(
    sprites=[(220, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)

industry.add_spritelayout(
    id="flour_mill_spritelayout_empty",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_1,
    building_sprites=[],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_silos_2",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_2,
    building_sprites=[],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_silos_3",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_3,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_silos_4",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_4,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_windmill_anim",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_windmill,
    building_sprites=[spriteset_windmill_anim],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_building_big",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_building_big,
    building_sprites=[spriteset_building_big],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_building_small",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_building_small,
    building_sprites=[spriteset_building_small],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_windmill_greeble",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_windmill_greeble,
    building_sprites=[spriteset_ground_overlay_windmill_greeble],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_1",
    layout=[
        (0, 0, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (0, 1, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
        (1, 0, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (1, 1, "flour_mill_tile_1", "flour_mill_spritelayout_building_big"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_2",
    layout=[
        (0, 0, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (0, 1, "flour_mill_tile_1", "flour_mill_spritelayout_building_big"),
        (1, 0, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (1, 1, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_3",
    layout=[
        (0, 0, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (0, 1, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
        (0, 2, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (0, 3, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
        (1, 0, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (1, 1, "flour_mill_tile_1", "flour_mill_spritelayout_building_small"),
        (1, 2, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (1, 3, "flour_mill_tile_1", "flour_mill_spritelayout_building_big"),
    ],
)

industry.add_industry_layout(
    id="flour_mill_industry_layout_4",
    layout=[
        (0, 0, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (0, 1, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
        (0, 2, "flour_mill_tile_1", "flour_mill_spritelayout_building_big"),
        (1, 1, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (1, 2, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_5",
    layout=[
        (0, 0, "flour_mill_tile_1", "flour_mill_spritelayout_building_small"),
        (0, 1, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (0, 2, "flour_mill_tile_1", "flour_mill_spritelayout_building_big"),

        (1, 0, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (1, 1, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (1, 2, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
    ],
)

industry.add_industry_layout(
    id="flour_mill_industry_layout_6",
    layout=[
        (0, 0, "flour_mill_tile_1", "flour_mill_spritelayout_empty"),
        (0, 1, "flour_mill_tile_1", "flour_mill_spritelayout_building_big"),
        (1, 0, "flour_mill_tile_1", "flour_mill_spritelayout_silos_3"),
        (1, 1, "flour_mill_tile_1", "flour_mill_spritelayout_silos_4"),
    ],
)