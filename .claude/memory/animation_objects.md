# FEAT_OBJECTS Animation in NML (OpenTTD)

## Working recipe (verified in AXIS+)

1. **OBJ_FLAG_ANIMATED** flag in `object_flags: bitmask(..., OBJ_FLAG_ANIMATED)`
2. **animation_info**: `[ANIMATION_LOOPING, N]` where N = frame count
3. **animation_speed**: `2^speed` ticks between frames. Speed 2 = 4 ticks ≈ 120ms/frame (good for conveyor belts). Speed 0 = every tick (too fast).
4. **animation_triggers**: `bitmask(ANIM_TRIGGER_OBJ_BUILT)` — triggers on placement
5. **CRITICAL: `anim_control` callback** in the graphics block:
   ```nml
   graphics {
       anim_control: return CB_RESULT_NEXT_FRAME;
       default: my_spritelayout;
   }
   ```
   Without this, animation frames never advance!

6. **Spriteset**: Define multi-frame spriteset, reference with `animation_frame % N` in spritelayout:
   ```nml
   spriteset(my_spriteset, "file.png") {
       [frame0_coords]
       [frame1_coords]
       ...
   }
   spritelayout my_layout {
       ground { sprite: GROUND; }
       building { sprite: my_spriteset(animation_frame % N); ... }
   }
   ```

## Gotchas
- `ANIM_TRIGGER_OBJ_TILELOOP` without anim_control resets frame to 0 every tile loop
- `animation_triggers: 0` (no triggers) = animation never starts
- Must demolish and re-place objects after GRF update to pick up new animation state
- Industry animation speed reference: iron_ore_mine conveyor uses speed=3 (industry tiles)

## Multi-tile ground overlay rendering (FEAT_OBJECTS)
- **childsprite** with `always_draw: 1` on GROUNDSPRITE_NORMAL = WORKS (no artifacts)
- Custom spriteset as ground sprite = artifacts (transparent pixels have no terrain underneath, highlights bleed through)
- Building with zoffset=0 as ground overlay = also caused issues
- Industries use childsprite on LOAD_TEMP(0) — same approach works for objects with GROUNDSPRITE_NORMAL

## Known Bugs (multi-tile objects)
- **Green grass under pit overlay**: GROUNDSPRITE_NORMAL shows grass even though childsprite overlay covers it. The overlay sprites have transparent edges so grass peeks through. Need to investigate using a dirt/brown ground sprite instead of GROUNDSPRITE_NORMAL.
- **Empty preview**: Multi-tile object preview (in build menu) shows only an empty tile — no pit sprites visible in the thumbnail.

## Multi-tile objects (var[0x40])
- **FEAT_OBJECTS**: Bits 0-7 = relative X, Bits 8-15 = relative Y (full bytes!)
- **FEAT_INDUSTRYTILES**: Bits 0-3 = X, Bits 4-7 = Y (nibbles)
- Switch expression: `var[0x40]` (full value)
- Switch value: `(y << 8) | x`
- OLD BUGS:
  - `(var[0x40] / 256) % 256` = only Y, X ignored
  - `var[0x40] % 256` = only X, Y ignored
  - `(y << 4) | x` = wrong shift, must be `(y << 8) | x`
