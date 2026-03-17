from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="cider_mill",
    accept_cargos_with_input_ratios=[("FRUT", 3), ("SGCN", 3), ("MNSP", 1), ("ENUM", 1)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("BEER", 6), ("ACET", 3), ("BIOM", 2)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["vineyard", "arable_farm"], 72],
        same_type_distance=72,
    ),
    name="string(STR_IND_DISTILLERY)",
    nearby_station_name="string(STR_STATION_BARREL_AND_KEG)",
    fund_cost_multiplier="50",
    pollution_and_squalor_factor=1,
    base_processing_cap=32,
    required_any_input_cargos=["FRUT", "SGCN"],
    scale_bonus_cargos=[("ACET", {"low": 2, "high": 3}), ("BIOM", {"low": 1, "high": 2})],
)


industry.economy_variations["BASIC_TROPIC"].enabled = True

industry.add_tile(
    id="cider_mill_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="cobble",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_building_a = industry.add_spriteset(
    sprites=[(10, 10, 64, 114, -31, -83)],
)
spriteset_chimneys = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -83)],
)
spriteset_produce_yard = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_building_b = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)

sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=0,
    yoffset=9,
    zoffset=50,
)


industry.add_spritelayout(
    id="cider_mill_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_building_a",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_building_a],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_chimneys",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_chimneys],
    smoke_sprites=[sprite_smoke],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_produce_yard",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_produce_yard],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_building_b",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_building_b],
)

industry.add_industry_layout(
    id="cider_mill_industry_layout_1",
    layout=[
        (0, 0, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),
        (1, 0, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),
        (2, 0, "cider_mill_tile_1", "cider_mill_spritelayout_empty"),
        (3, 0, "cider_mill_tile_1", "cider_mill_spritelayout_produce_yard"),

        (0, 1, "cider_mill_tile_1", "cider_mill_spritelayout_chimneys"),
        (1, 1, "cider_mill_tile_1", "cider_mill_spritelayout_building_a"),
        (2, 1, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),
        (3, 1, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),
    ],
)

industry.add_industry_layout(
    id="cider_mill_industry_layout_2",
    layout=[
        (0, 0, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),
        (1, 0, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),
        (2, 0, "cider_mill_tile_1", "cider_mill_spritelayout_empty"),
        (3, 0, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),

        (0, 1, "cider_mill_tile_1", "cider_mill_spritelayout_building_a"),
        (1, 1, "cider_mill_tile_1", "cider_mill_spritelayout_chimneys"),
        (2, 1, "cider_mill_tile_1", "cider_mill_spritelayout_produce_yard"),
        (3, 1, "cider_mill_tile_1", "cider_mill_spritelayout_produce_yard"),

        (0, 2, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),
        (1, 2, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),
        (2, 2, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),    
    ],
)

industry.add_industry_layout(
    id="cider_mill_industry_layout_3",
    layout=[
        (0, 0, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),
        (1, 0, "cider_mill_tile_1", "cider_mill_spritelayout_empty"),
        (2, 0, "cider_mill_tile_1", "cider_mill_spritelayout_produce_yard"),

        (0, 1, "cider_mill_tile_1", "cider_mill_spritelayout_tanks"),
        (1, 1, "cider_mill_tile_1", "cider_mill_spritelayout_building_a"),
        (2, 1, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),

        (0, 2, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),
        (1, 2, "cider_mill_tile_1", "cider_mill_spritelayout_chimneys"),
        (2, 2, "cider_mill_tile_1", "cider_mill_spritelayout_building_b"),    
    ],
)