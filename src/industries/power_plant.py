from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="power_plant",
    accept_cargo_types=["COAL", "PETR"],
    prod_cargo_types=[],
    prob_in_game="3",
    prob_map_gen="5",
    prod_multiplier="[0, 0]",
    map_colour="168",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    town_industry_for_cargoflow=False,
    prospect_chance="0.75",
    name="string(STR_IND_POWER_PLANT)",
    nearby_station_name="string(STR_STATION_POWERHUNGRY)",
    fund_cost_multiplier="15",
)


industry.economy_variations["STEELTOWN"].enabled = True

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].accept_cargo_types = [
    "COAL",
    "PETR",
    "BIOM",
]

industry.economy_variations["BASIC_TEMPERATE"].enabled = True
industry.economy_variations["BASIC_TEMPERATE"].accept_cargo_types = [
    "COAL",
    "PETR",
    "BIOM",
]


industry.add_tile(
    id="power_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, 
        disallow_industry_adjacent=True,
        require_houses_nearby=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_boiler = industry.add_spriteset(
    sprites=[(10, 10, 64, 114, -31, -83)],
)
spriteset_chimneys = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -83)],
)
spriteset_tanks_group = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_silos = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_silos_with_office = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)

sprite_transformer = industry.add_sprite(
    sprite_number=2054,
)

sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=81,
)


industry.add_spritelayout(
    id="power_plant_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="power_plant_spritelayout_boiler",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_boiler],
)
industry.add_spritelayout(
    id="power_plant_spritelayout_chimneys",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_chimneys],
    smoke_sprites=[sprite_smoke_1],
)
industry.add_spritelayout(
    id="power_plant_spritelayout_tanks_group",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_transformer],
)
industry.add_spritelayout(
    id="power_plant_spritelayout_silos",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos],
)
industry.add_spritelayout(
    id="power_plant_spritelayout_silos_with_office",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos_with_office],
)

industry.add_industry_layout(
    id="power_plant_industry_layout_1",
    layout=[
        (0, 0, "power_plant_tile_1", "power_plant_spritelayout_chimneys"),
        (0, 1, "power_plant_tile_1", "power_plant_spritelayout_boiler"),
        (
            0,
            2,
            "power_plant_tile_1",
            "power_plant_spritelayout_tanks_group",
        ),
        (1, 0, "power_plant_tile_1", "power_plant_spritelayout_chimneys"),
        (1, 1, "power_plant_tile_1", "power_plant_spritelayout_boiler"),
        (
            1,
            2,
            "power_plant_tile_1",
            "power_plant_spritelayout_tanks_group",
        ),
        (
            2,
            0,
            "power_plant_tile_1",
            "power_plant_spritelayout_silos_with_office",
        ),
        (2, 1, "power_plant_tile_1", "power_plant_spritelayout_silos"),
        (2, 2, "power_plant_tile_1", "power_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="power_plant_industry_layout_2",
    layout=[
        (0, 0, "power_plant_tile_1", "power_plant_spritelayout_boiler"),
        (
            0,
            1,
            "power_plant_tile_1",
            "power_plant_spritelayout_tanks_group",
        ),
        (1, 0, "power_plant_tile_1", "power_plant_spritelayout_boiler"),
        (
            1,
            1,
            "power_plant_tile_1",
            "power_plant_spritelayout_tanks_group",
        ),
        (2, 0, "power_plant_tile_1", "power_plant_spritelayout_chimneys"),
        (2, 1, "power_plant_tile_1", "power_plant_spritelayout_silos"),
        (
            3,
            0,
            "power_plant_tile_1",
            "power_plant_spritelayout_silos_with_office",
        ),
        (3, 1, "power_plant_tile_1", "power_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="power_plant_industry_layout_3",
    layout=[
        (0, 0, "power_plant_tile_1", "power_plant_spritelayout_boiler"),
        (
            0,
            1,
            "power_plant_tile_1",
            "power_plant_spritelayout_tanks_group",
        ),
        (0, 2, "power_plant_tile_1", "power_plant_spritelayout_chimneys"),
        (0, 3, "power_plant_tile_1", "power_plant_spritelayout_silos"),
        (1, 0, "power_plant_tile_1", "power_plant_spritelayout_boiler"),
        (
            1,
            1,
            "power_plant_tile_1",
            "power_plant_spritelayout_tanks_group",
        ),
        (
            1,
            2,
            "power_plant_tile_1",
            "power_plant_spritelayout_silos_with_office",
        ),
        (1, 3, "power_plant_tile_1", "power_plant_spritelayout_empty"),
    ],
)


