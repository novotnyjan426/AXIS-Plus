from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="meat_packing_plant",
    accept_cargos_with_input_ratios=[("FISH", 6), ("MNSP", 2), ("SALT", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("FOOD", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="38",
    name="string(STR_IND_MEAT_PACKING_PLANT)",
    nearby_station_name="string(STR_STATION_MEAT)",
    fund_cost_multiplier="120",
    base_processing_cap=32,
    required_input_cargos=["FISH", "MEAT"],
    scale_bonus_cargos=[("EOIL", {"low": 2, "high": 3}), ("BIOM", {"medium": 2})],
)


industry.economy_variations["STEELTOWN"].enabled = True

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].accept_cargos_with_input_ratios = [
    ("MEAT", 5),
    ("MNSP", 2),
    ("SALT", 2),
    ("ENUM", 1),
]
industry.economy_variations["BASIC_TROPIC"].prod_cargo_types_with_output_ratios = [
    ("FOOD", 7),
    ("EOIL", 2),
    ("BIOM", 2),
]


industry.add_tile(
    id="meat_packing_plant_tile_1",
    animation_length=40,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="dirty_concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 50, -31, -23)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 50, -31, -25)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 88, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 88, -31, -58)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 88, -31, -58)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 88, -31, -58)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 88, -31, -58)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=8,
    zoffset=72,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=12,
    zoffset=72,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="meat_packing_plant_big_tank",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="meat_packing_plant_silo",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="meat_packing_plant_building_tall",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="meat_packing_plant_building_middle",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="meat_packing_plant_building_front",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="meat_packing_plant_building_chimneys",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
)
industry.add_spritelayout(
    id="meat_packing_plant_building_back",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=[],
)
industry.add_spritelayout(
    id="meat_packing_plant_small_tank",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id="meat_packing_plant_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)

industry.add_industry_layout(
    id="meat_packing_plant_industry_layout_1",
    layout=[
        (0, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_back"),
        (0, 1, "meat_packing_plant_tile_1", "meat_packing_plant_small_tank"),
        (1, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_middle"),
        (1, 1, "meat_packing_plant_tile_1", "meat_packing_plant_silo"),
        (2, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_tall"),
        (2, 1, "meat_packing_plant_tile_1", "meat_packing_plant_building_chimneys"),
        (3, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_front"),
        (3, 1, "meat_packing_plant_tile_1", "meat_packing_plant_building_middle"),
        (4, 0, "meat_packing_plant_tile_1", "meat_packing_plant_empty"),
        (4, 1, "meat_packing_plant_tile_1", "meat_packing_plant_big_tank"),
    ],
)

industry.add_industry_layout(
    id="meat_packing_plant_industry_layout_2",
    layout=[
        (0, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_chimneys"),
        (0, 1, "meat_packing_plant_tile_1", "meat_packing_plant_silo"),
        (1, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_middle"),
        (1, 1, "meat_packing_plant_tile_1", "meat_packing_plant_building_back"),
        (2, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_tall"),
        (2, 1, "meat_packing_plant_tile_1", "meat_packing_plant_building_front"),
        (3, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_middle"),
        (3, 1, "meat_packing_plant_tile_1", "meat_packing_plant_small_tank"),
    ],
)

industry.add_industry_layout(
    id="meat_packing_plant_industry_layout_3",
    layout=[
        (0, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_back"),
        (0, 1, "meat_packing_plant_tile_1", "meat_packing_plant_building_chimneys"),
        (0, 2, "meat_packing_plant_tile_1", "meat_packing_plant_big_tank"),
        (1, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_middle"),
        (1, 1, "meat_packing_plant_tile_1", "meat_packing_plant_building_front"),
        (1, 2, "meat_packing_plant_tile_1", "meat_packing_plant_silo"),
        (2, 0, "meat_packing_plant_tile_1", "meat_packing_plant_building_tall"),
        (2, 1, "meat_packing_plant_tile_1", "meat_packing_plant_small_tank"),
        (2, 2, "meat_packing_plant_tile_1", "meat_packing_plant_empty"),
    ],
)