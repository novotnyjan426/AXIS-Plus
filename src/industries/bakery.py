from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="bakery",
    accept_cargos_with_input_ratios=[
        ("BAKE", 3),
        ("SUGR", 2),
        ("ENUM", 1),
        ("EOIL", 1),
        ("MNSP", 1),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("FOOD", 8)],
    prob_map_gen="10",
    prob_in_game="10",
    map_colour="49",
    location_checks=dict(bakery_layouts_by_date=True),
    name="string(STR_IND_BAKERY)",
    nearby_station_name="string(STR_STATION_MILL)",
    fund_cost_multiplier="50",
    base_processing_cap=32,
    required_input_cargos=["BAKE", "SUGR"],
    scale_bonus_cargos=[("BIOM", {"low": 1, "medium": 2, "high": 3})],
)

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].prod_cargo_types_with_output_ratios = [
    ("FOOD", 8),
    ("BIOM", 1),
]




industry.add_tile(
    id="bakery_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        require_houses_nearby=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground_bakery = industry.add_spriteset(
    type="cobble",
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


industry.add_spritelayout(
    id="bakery_spritelayout_brickbakery_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_1,
    building_sprites=[],
)
industry.add_spritelayout(
    id="bakery_spritelayout_brickbakery_2",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_2,
    building_sprites=[],
)
industry.add_spritelayout(
    id="bakery_spritelayout_brickbakery_3",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_3,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="bakery_spritelayout_brickbakery_4",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_4,
    building_sprites=[spriteset_4],
)

industry.add_industry_layout(
    id="bakery_industry_layout_1",
    layout=[
        (0, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_3"),
        (0, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_4"),
        (1, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_1"),
        (1, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="bakery_industry_layout_2",
    layout=[
        (0, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_3"),
        (0, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_4"),
        (1, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_3"),
        (1, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_4"),
        (2, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_1"),
        (2, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="bakery_industry_layout_3",
    layout=[
        (0, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_3"),
        (0, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_4"),
        (0, 2, "bakery_tile_1", "bakery_spritelayout_brickbakery_3"),
        (0, 3, "bakery_tile_1", "bakery_spritelayout_brickbakery_4"),
        (1, 0, "bakery_tile_1", "bakery_spritelayout_brickbakery_1"),
        (1, 1, "bakery_tile_1", "bakery_spritelayout_brickbakery_2"),
        (1, 2, "bakery_tile_1", "bakery_spritelayout_brickbakery_1"),
        (1, 3, "bakery_tile_1", "bakery_spritelayout_brickbakery_2"),
    ],
)
