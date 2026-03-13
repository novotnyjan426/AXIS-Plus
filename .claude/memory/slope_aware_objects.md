---
name: slope_aware_objects
description: How to make slope-aware FEAT_OBJECTS (learned from AuzObjects Landscape GRF reverse-engineering)
type: reference
---

## Slope-Aware Objects — Required Setup

Learned by reverse-engineering AuzObjects-Landscape-v9 GRF (binary parsing of Action0 properties and callback flags).

### 3 things needed for objects to sit on slopes without flattening terrain:

1. **`OBJ_FLAG_NO_FOUNDATIONS`** (bit 5) — prevents foundation drawing on slopes
2. **`tile_check` callback** returning `CB_RESULT_LOCATION_ALLOW` — allows placement on ANY slope without terraforming. **This is the key** — without it, OpenTTD auto-levels the terrain when placing objects.
3. **`autoslope` callback** returning `CB_RESULT_AUTOSLOPE` — allows slope modification after object is placed

### NML pattern:
```nml
item(FEAT_OBJECTS, my_object, 123) {
    property {
        object_flags: bitmask(OBJ_FLAG_ANYTHING_REMOVE, OBJ_FLAG_REMOVE_IS_INCOME, OBJ_FLAG_NO_FOUNDATIONS);
        ...
    }
    graphics {
        tile_check: return CB_RESULT_LOCATION_ALLOW;
        autoslope: return CB_RESULT_AUTOSLOPE;
        default: my_slope_switch;
    }
}
```

### AuzObjects patterns observed:
- FRST (Forest) objects: `NO_FOUNDATIONS`, `autoslope`, many also have `tile_check`
- AUZT (Trees) objects: `NO_FOUNDATIONS`, `autoslope`
- All slope-aware objects use `height=0` and `views=4`
- Flag values commonly seen: `0x0834` (ANYTHING_REMOVE + REMOVE_IS_INCOME + NO_FOUNDATIONS) or `0x0c3c` (adds ON_WATER)

### Ground sprite — critical gotcha:
- **DO NOT use `GROUNDSPRITE_NORMAL`** in slope-aware spritelayouts — it doesn't auto-adapt for FEAT_OBJECTS with NO_FOUNDATIONS, causing artifact pixels in corners
- Instead use explicit slope calculation: `3981 + slope_to_sprite_offset(nearby_tile_slope(0, 0))` (3981 = flat grass sprite)
- For other ground types (e.g. farmland 3962): `3962 + slope_to_sprite_offset(nearby_tile_slope(0, 0))`
- This matches how industries do it in `MagicSpritelayoutSlopeAwareTrees` (industry.py:718)

### For tree position adjustment per slope:
- Use `nearby_tile_slope(0, 0)` in a switch to select per-slope spritelayout
- Positions come from `MagicSpritelayoutSlopeAwareTrees` in `industry.py` (slopes_4 for 4 trees, slopes_9 for 9 trees)
- Tree childsprites use `xextent: 4, yextent: 4, zextent: 32` (same as industry magic trees)
- Implementation: `slope_buildings` parameter on ExpansionObject → generates 19 spritelayouts + slope switch in `objects.pynml`

### Summary of ALL 4 things needed:
1. `OBJ_FLAG_NO_FOUNDATIONS` — no foundation plinth
2. `tile_check: CB_RESULT_LOCATION_ALLOW` — allow placement without terraforming
3. `autoslope: CB_RESULT_AUTOSLOPE` — allow slope change after placement
4. Ground sprite: `<base> + slope_to_sprite_offset(nearby_tile_slope(0, 0))` — correct sloped ground rendering

**Why:** Without #2 the game terraforms flat. Without #4 there are empty-pixel artifacts in tile corners.

**How to apply:** Any time we create objects that should follow terrain slopes (trees, ground overlays, landscape features), use all 4 elements above.
