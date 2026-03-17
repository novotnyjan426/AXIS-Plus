from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="edible_oil_refinery",
    accept_cargos_with_input_ratios=[("OLSD", 6), ("MNSP", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("EOIL", 4), ("BIOM", 2)],
    prob_in_game="7",
    prob_map_gen="7",
    map_colour="163",
    name="string(STR_IND_EDIBLE_OIL_REFINERY)",
    nearby_station_name="string(STR_STATION_OIL_PRESS)",
    fund_cost_multiplier="118",
    base_processing_cap=32,
    required_input_cargos=["OLSD"],
)

industry.economy_variations["BASIC_TROPIC"].enabled = True

industry.economy_variations["BASIC_TEMPERATE"].enabled = True


industry.add_tile(
    id="edible_oil_refinery_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 76, -31, -45)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 76, -31, -45)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 63, -31, -32)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 63, -31, -32)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 63, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 63, -31, -32)],
)


industry.add_spritelayout(
    id="edible_oil_refinery_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="edible_oil_refinery_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="edible_oil_refinery_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="edible_oil_refinery_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="edible_oil_refinery_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="edible_oil_refinery_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)

industry.add_industry_layout(
    id="edible_oil_refinery_industry_layout_1",
    layout=[
        (0, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_2"),
        (0, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_3"),
        (1, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_1"),
        (1, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_4"),
        (2, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_5"),
        (2, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_6"),
    ],
)

industry.add_industry_layout(
    id="edible_oil_refinery_industry_layout_2",
    layout=[
        (0, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_2"),
        (0, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_3"),
        (0, 2, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_5"),
        (1, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_1"),
        (1, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_4"),
        (1, 2, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_6"),
    ],
)

industry.add_industry_layout(
    id="edible_oil_refinery_industry_layout_3",
    layout=[
        (0, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_5"),
        (0, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_3"),
        (0, 2, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_2"),
        (1, 0, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_6"),
        (1, 1, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_4"),
        (1, 2, "edible_oil_refinery_tile_1", "edible_oil_refinery_spritelayout_1"),
    ],
)
