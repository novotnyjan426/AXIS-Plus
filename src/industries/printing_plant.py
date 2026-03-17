from industry import IndustrySecondary, TileLocationChecks


industry = IndustrySecondary(
    id="printing_plant",
    accept_cargos_with_input_ratios=[
        ("PAPR", 6),
        ("COAT", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("GOOD", 5), ("MAIL", 5), ("RCYC", 1)],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="166",
    name="string(STR_IND_PRINTING_PLANT)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="95",
    base_processing_cap=32,
    required_input_cargos=["PAPR"],
    scale_bonus_cargos=[("RCYC", {"low": 1, "high": 2})],
)

industry.economy_variations['BASIC_TEMPERATE'].enabled = True



industry.add_tile(
    id="printing_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 94, -31, -63)],
)

spriteset_ground_anim = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay_anim = industry.add_spriteset(
    type="empty",
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 94, -31, -63)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 94, -31, -62)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 94, -31, -43)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 94, -31, -43)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 94, -31, -43)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 94, -31, -43)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 94, -31, -63)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(10, 120, 64, 64, -31, -33)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(80, 120, 64, 64, -31, -33)],
)



industry.add_spritelayout(
    id="printing_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_2",
    ground_sprite=spriteset_ground_anim,
    ground_overlay=spriteset_ground_overlay_anim,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)
industry.add_spritelayout(
    id="printing_plant_spritelayout_10",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
)

industry.add_industry_layout(
    id="printing_plant_industry_layout_1",
    layout=[
        (0, 0, "printing_plant_tile_1", "printing_plant_spritelayout_7"),
        (0, 1, "printing_plant_tile_1", "printing_plant_spritelayout_5"),
        (0, 2, "printing_plant_tile_1", "printing_plant_spritelayout_7"),
        (0, 3, "printing_plant_tile_1", "printing_plant_spritelayout_5"),
        (1, 0, "printing_plant_tile_1", "printing_plant_spritelayout_6"),
        (1, 1, "printing_plant_tile_1", "printing_plant_spritelayout_4"),
        (1, 2, "printing_plant_tile_1", "printing_plant_spritelayout_6"),
        (1, 3, "printing_plant_tile_1", "printing_plant_spritelayout_4"),
        (2, 0, "printing_plant_tile_1", "printing_plant_spritelayout_8"),
        (2, 1, "printing_plant_tile_1", "printing_plant_spritelayout_3"),
        (2, 2, "printing_plant_tile_1", "printing_plant_spritelayout_9"),
        (2, 3, "printing_plant_tile_1", "printing_plant_spritelayout_10"),
        (3, 0, "printing_plant_tile_1", "printing_plant_spritelayout_1"),
        (3, 1, "printing_plant_tile_1", "printing_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="printing_plant_industry_layout_2",
    layout=[
        (0, 1, "printing_plant_tile_1", "printing_plant_spritelayout_7"),
        (0, 2, "printing_plant_tile_1", "printing_plant_spritelayout_5"),
        (1, 1, "printing_plant_tile_1", "printing_plant_spritelayout_6"),
        (1, 2, "printing_plant_tile_1", "printing_plant_spritelayout_4"),
        (2, 0, "printing_plant_tile_1", "printing_plant_spritelayout_8"),
        (2, 1, "printing_plant_tile_1", "printing_plant_spritelayout_3"),
        (2, 2, "printing_plant_tile_1", "printing_plant_spritelayout_9"),
        (3, 0, "printing_plant_tile_1", "printing_plant_spritelayout_1"),
        (3, 1, "printing_plant_tile_1", "printing_plant_spritelayout_2"),
        (3, 2, "printing_plant_tile_1", "printing_plant_spritelayout_10"),
    ],
)
industry.add_industry_layout(
    id="printing_plant_industry_layout_3",
    layout=[
        (0, 0, "printing_plant_tile_1", "printing_plant_spritelayout_7"),
        (0, 1, "printing_plant_tile_1", "printing_plant_spritelayout_5"),
        (0, 2, "printing_plant_tile_1", "printing_plant_spritelayout_9"),
        (1, 0, "printing_plant_tile_1", "printing_plant_spritelayout_6"),
        (1, 1, "printing_plant_tile_1", "printing_plant_spritelayout_4"),
        (1, 2, "printing_plant_tile_1", "printing_plant_spritelayout_8"),
        (2, 0, "printing_plant_tile_1", "printing_plant_spritelayout_10"),
        (2, 1, "printing_plant_tile_1", "printing_plant_spritelayout_8"),
        (2, 2, "printing_plant_tile_1", "printing_plant_spritelayout_3"),
        (3, 1, "printing_plant_tile_1", "printing_plant_spritelayout_1"),
        (3, 2, "printing_plant_tile_1", "printing_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="printing_plant_industry_layout_4",
    layout=[
        (0, 0, "printing_plant_tile_1", "printing_plant_spritelayout_7"),
        (0, 1, "printing_plant_tile_1", "printing_plant_spritelayout_5"),
        (0, 2, "printing_plant_tile_1", "printing_plant_spritelayout_7"),
        (0, 3, "printing_plant_tile_1", "printing_plant_spritelayout_5"),
        (1, 0, "printing_plant_tile_1", "printing_plant_spritelayout_6"),
        (1, 1, "printing_plant_tile_1", "printing_plant_spritelayout_4"),
        (1, 2, "printing_plant_tile_1", "printing_plant_spritelayout_6"),
        (1, 3, "printing_plant_tile_1", "printing_plant_spritelayout_4"),
        (2, 0, "printing_plant_tile_1", "printing_plant_spritelayout_9"),
        (2, 1, "printing_plant_tile_1", "printing_plant_spritelayout_8"),
        (2, 2, "printing_plant_tile_1", "printing_plant_spritelayout_3"),
        (2, 3, "printing_plant_tile_1", "printing_plant_spritelayout_10"),
        (3, 1, "printing_plant_tile_1", "printing_plant_spritelayout_1"),
        (3, 2, "printing_plant_tile_1", "printing_plant_spritelayout_2"),
    ],
)
