# AXIS+ Expansion System — Implementation Plan v2

## Overview

AXIS+ adds an "expandable industries" mechanic: players place NewGRF objects
(expansion buildings) around industries to boost production. The number of
expansion-object tiles within range determines a production bonus at three
configurable thresholds.

**License:** GPL v2 (same as AXIS and ISR-DWE-Objects-II).

---

## Phase 0 — Technical Spike (DO THIS FIRST)

### Resolved: nearby_tile_class IS available for FEAT_INDUSTRIES

Verified via NML source code (`action2var_variables.py`): `nearby_tile_class`
is in the `varact2vars60x_industries` list. This means an industry production
callback (produce_256_ticks) CAN check `nearby_tile_class(x, y)` to detect
what type of tile is at a given offset.

This resolves the primary blocker — **the scan mechanism works**.

### Remaining Problem: Cannot distinguish object types from industry callbacks

**What works:**
- `nearby_tile_class(x, y) == TILE_CLASS_OBJECTS` — detects that ANY object
  is placed on a nearby tile. Available for FEAT_INDUSTRIES.

**What does NOT work:**
- `nearby_tile_object_type` — returns the specific object ID, but is
  **only available for FEAT_OBJECTS** (object querying another object).
  NOT available for FEAT_INDUSTRIES or FEAT_INDUSTRYTILES.
- `nearby_tile_grfid` — does not exist in NML at all.

**Consequence:** An industry can count how many object tiles are nearby, but
it **cannot tell which object** is placed there. A coal mine cannot distinguish
between a "Coal Mine Expansion" and a "Farm Expansion" or even a lighthouse
from a completely different NewGRF.

The reverse also doesn't help: `nearby_tile_object_type` works from FEAT_OBJECTS
(so an object CAN identify neighboring objects from the same GRF), but objects
cannot write to industry perm storage.

### Impact on Design

| Feature | Status |
|---------|--------|
| Count total object tiles near industry | **Works** |
| Count only AXIS+ objects (exclude other GRFs) | **Not possible** |
| Count only coal-specific objects at coal mine | **Not possible** |
| Per-industry object sets (Coal Expansion, Farm Expansion) | **Visual/UX only** — all count the same |

### Accepted MVP Behavior

Industry counts ALL objects nearby via `TILE_CLASS_OBJECTS`. Per-industry
object differentiation is handled through **UX, not code**:

1. Objects are organized in separate menu categories (Coal Expansion, Farm
   Expansion, etc.) so the player knows what "belongs" where
2. Objects visually match their intended industry type
3. Placing the "wrong" object type near an industry still gives a bonus —
   this is the player's choice and not mechanically enforced

This is acceptable for MVP. If OpenTTD adds `nearby_tile_object_type` for
FEAT_INDUSTRIES in the future, per-industry filtering can be retrofitted.

### Spike Steps (still needed for in-game verification)

1. Pick one industry (coal_mine) and add a minimal test to its 256-tick callback.
2. Add a single `nearby_tile_class(1, 0) == TILE_CLASS_OBJECTS` check in a
   FEAT_INDUSTRIES switch and store the result to perm storage.
3. Compile with nmlc — expected to succeed based on NML source analysis.
4. Load in OpenTTD, place an object next to the coal mine, and verify the
   perm storage value changes.

### Spike Files to Modify

- `src/templates/produce_primary.pynml` — add test switch before production
- `src/industry.py` — add one test perm storage register

### Success Criteria

nmlc compiles without errors AND the value is readable in-game.

---

## Phase 1 — Core Infrastructure

Only begin after Phase 0 confirms the scan mechanism.

### 1.1 GRF Parameters

Add parameters to `src/templates/header.pynml`. Use param numbers 10-17
(currently unused).

| Param | Variable | Default | Description |
|-------|----------|---------|-------------|
| 10 | `expansion_threshold_low` | 10 | Min tiles for Low bonus |
| 11 | `expansion_threshold_medium` | 20 | Min tiles for Medium bonus |
| 12 | `expansion_threshold_high` | 40 | Min tiles for High bonus |
| 13 | `primary_expansion_bonus_low` | 130 | Primary Low (130 = +30%) |
| 14 | `primary_expansion_bonus_medium` | 170 | Primary Medium (170 = +70%) |
| 15 | `primary_expansion_bonus_high` | 250 | Primary High (250 = +150%) |
| 16 | `secondary_expansion_penalty` | 75 | Secondary no-expansion (0.75x) |
| 17 | `secondary_expansion_bonus_high` | 200 | Secondary High (2.0x) |

All values are percentages where 100 = 1.0x (no change).

Secondary intermediate values (hardcoded, derived from params):
- 0 expansion tiles: param 16 (default 75 = 0.75x)
- Low threshold: 100 (1.0x)
- Medium threshold: 150 (1.5x)
- High threshold: param 17 (default 200 = 2.0x)

**Strings go in:**
- `src/lang/english.lng` — static strings (param names, descriptions)
- `src/lang_templates/english.pylng` — only if templated values are needed

### 1.2 Perm Storage Registers

Add two registers to each industry type that supports expansion.

**File:** `src/industry.py`

For `IndustryPrimary` (line ~1655), append to existing perm storage list:
```python
"expansion_tile_count",
"expansion_multiplier",
```

For `IndustrySecondary` (line ~1850), replace two existing `"unused"` slots:
```python
"expansion_tile_count",      # was "unused"
"expansion_multiplier",      # was "unused"
```

Using existing unused slots for secondary avoids breaking savegame register
positions.

### 1.3 Object Pipeline (Greenfield)

The current build pipeline only handles cargos and industries. There is **no
existing FEAT_OBJECTS path**. This is new subsystem work, not a small tweak.

#### New files to create:

```
src/objects/                    # Python object definitions
src/objects/__init__.py         # Registration, similar to src/industries/__init__.py
src/objects/test_expansion.py   # First test object (Phase 1 MVP)
src/templates/objects.pynml     # NML template for FEAT_OBJECTS items
src/graphics/objects/           # Sprite sheets (later phases)
```

#### Build pipeline changes:

**File:** `src/render_nml.py`

Currently renders: header items → industries (lines 84-113).

Add object rendering after industries:
```python
# After industry rendering loop
for obj in registered_objects:
    grf_nml.write(render_object_nml(obj))
```

This requires:
- New `render_object_nml()` function (similar to `render_industry_nml()`)
- Import registered_objects from `src/firs.py` (or a new registry)

**File:** `src/firs.py`

Add object registration alongside existing cargo/industry registration.

#### Minimal object definition (Phase 1 MVP):

One 1x1 object using an existing AXIS sprite (e.g. supply_yard coal pile).
No DWE import yet.

```nml
item(FEAT_OBJECTS, expansion_test_object, 0) {
    property {
        class: "AXP+";
        classname: string(STR_OBJECT_CLASS_AXIS_PLUS);
        name: string(STR_OBJECT_EXPANSION_TEST);
        size: [1, 1];
        build_cost_multiplier: 16;
        remove_cost_multiplier: 4;
        introduction_date: date(1900, 1, 1);
        end_of_life_date: 0xFFFFFFFF;
        object_flags: bitmask(OBJ_FLAG_ANYTHING_REMOVE);
        height: 4;
        num_views: 1;
    }
    graphics {
        default: expansion_test_spritelayout;
    }
}
```

### 1.4 Tile Scanning Template

**New file:** `src/templates/expansion_scan.pynml`

This template is included by both `produce_primary.pynml` and
`produce_secondary.pynml`.

#### Approach: Direct scan from FEAT_INDUSTRIES

Verified: `nearby_tile_class` is available for FEAT_INDUSTRIES. The scan
checks `nearby_tile_class(x, y) == TILE_CLASS_OBJECTS` (note: plural form)
at each offset.

```nml
switch(FEAT_INDUSTRIES, SELF, ${industry.id}_count_expansion_tiles,
    [
        STORE_TEMP(0, 0x10),
        // Check each offset. For each tile, check if tile class is
        // TILE_CLASS_OBJECTS (meaning any object is placed there).
        // Scan 3 tiles out from industry edges.
        STORE_TEMP(LOAD_TEMP(0x10)
            + (nearby_tile_class(-1, -1) == TILE_CLASS_OBJECTS ? 1 : 0)
            + (nearby_tile_class(-1,  0) == TILE_CLASS_OBJECTS ? 1 : 0)
            // ... all offsets in scan area ...
            , 0x10),
        STORE_PERM_ALT(${get_perm_num("expansion_tile_count")},
                       LOAD_TEMP(0x10)),
    ]) {
    return 0;
}
```

#### Known Limitation: Counts ALL objects, not just AXIS+ objects

`nearby_tile_class` only tells us "there is an object here", not which
object. `nearby_tile_object_type` exists but is only available for
FEAT_OBJECTS, not FEAT_INDUSTRIES.

This means:
- A lighthouse from base game placed near a mine = counts as expansion
- A DWE object from another loaded GRF = counts as expansion
- A "Farm Expansion" AXIS+ object near a coal mine = counts as expansion

**Accepted for MVP.** Per-industry filtering is enforced via UX only
(separate object categories, visual matching). See Phase 0 for full
analysis.

### 1.5 Expansion Multiplier Calculation

**New switch**, included from `expansion_scan.pynml`:

```nml
switch(FEAT_INDUSTRIES, SELF, ${industry.id}_calculate_expansion_multiplier,
    [
        STORE_PERM_ALT(
            ${get_perm_num("expansion_multiplier")},
            (LOAD_PERM(${get_perm_num("expansion_tile_count")})
                >= expansion_threshold_high)
            ? ${expansion_bonus_high}
            : (LOAD_PERM(${get_perm_num("expansion_tile_count")})
                >= expansion_threshold_medium)
            ? ${expansion_bonus_medium}
            : (LOAD_PERM(${get_perm_num("expansion_tile_count")})
                >= expansion_threshold_low)
            ? ${expansion_bonus_low}
            : ${expansion_no_bonus}
        ),
    ]) {
    return 0;
}
```

Where `${expansion_bonus_*}` and `${expansion_no_bonus}` are set differently
for primary vs secondary industries (passed as template variables).

---

## Phase 2 — Production Logic Changes

### 2.1 Primary Industries

**File:** `src/templates/produce_primary.pynml`

**256-tick callback** (`${industry.id}_produce_256_ticks`, line 142):
Add scan + multiplier calculation calls:

```nml
switch(FEAT_INDUSTRIES, SELF, ${industry.id}_produce_256_ticks,
    [
        ${industry.id}_count_expansion_tiles(),           // NEW
        ${industry.id}_calculate_expansion_multiplier(),  // NEW
        ${industry.id}_produce_calculate_current_production_level(),
        ${industry.id}_update_supplied_cycles_remaining_per_cargo(),
        ${industry.id}_produce_256_ticks_shift_supplies_delivered(),
    ]) {
    ${industry.id}_produce_256_ticks_switch_economy;
}
```

**Production formula** (line 96):
Current:
```nml
${cargo[0]}: (${cargo[1]} * production_level
    * LOAD_PERM(base_prod_factor) * LOAD_TEMP(9))
    / (16 * 16 * 100);
```

Modified — multiply by expansion_multiplier:
```nml
${cargo[0]}: (${cargo[1]} * production_level
    * LOAD_PERM(base_prod_factor) * LOAD_TEMP(9)
    * LOAD_PERM(${get_perm_num("expansion_multiplier")}))
    / (16 * 16 * 100 * 100);
```

**Important:** `expansion_multiplier` must be initialized to 100 on industry
construction, otherwise first production cycle multiplies by 0. Add init in
`randomise_primary_production_on_build.pynml` or equivalent.

### 2.2 Secondary Industries

**File:** `src/templates/produce_secondary.pynml`

**Critical difference from primary:** Secondary industries produce on
**cargo arrival** (`produce_cargo_arrival` callback, line 130), NOT on
256-tick. The 256-tick callback only updates supply cycle counters.

**Approach:** Scan expansion tiles on 256-tick (every ~10s), cache result in
perm storage. Read cached multiplier during cargo arrival production.
The multiplier may be up to ~10 seconds stale, which is acceptable.

**256-tick callback** (line 164):
Add scan calls:

```nml
switch(FEAT_INDUSTRIES, SELF, ${industry.id}_produce_256_ticks,
    [
        ${industry.id}_count_expansion_tiles(),           // NEW
        ${industry.id}_calculate_expansion_multiplier(),  // NEW
        ${industry.id}_update_supplied_cycles_remaining_per_cargo(),
    ]) {
    ${industry.id}_produce_256_ticks_produce;
}
```

**Production output** (line 21):
Current:
```nml
${cargo[0]}: (LOAD_PERM(total_cargo_to_distribute_this_cycle)
    * ${cargo[1]}) / 8;
```

Modified:
```nml
${cargo[0]}: (LOAD_PERM(${get_perm_num("total_cargo_to_distribute_this_cycle")})
    * ${cargo[1]}
    * LOAD_PERM(${get_perm_num("expansion_multiplier")}))
    / (8 * 100);
```

**Important:** `expansion_multiplier` must default to 100 (not 0) for secondary
industries too. Since secondary industries don't have a build_prod_change
callback like primaries, initialize this in the first 256-tick cycle by checking
if the value is 0 and setting it to `secondary_expansion_penalty` (75).

### 2.3 Multiplier Initialization

To prevent multiply-by-zero on first cycle, add an init check at the start of
the expansion multiplier calculation:

```nml
// If expansion_multiplier is 0 (uninitialized), set default
// For primary: 100 (no bonus, no penalty)
// For secondary: secondary_expansion_penalty (75 by default)
```

Or set it in the industry construction callback.

---

## Phase 3 — Content & DWE Import

Only after Phase 1+2 are working with the test object.

### 3.1 Object Categories & Structure

Each industry type gets its **own dedicated object set**, plus there is one
**generic set** usable near any industry. All are AXIS+ objects within one GRF.

#### Object sets:

| Object Set | Object Class | Example Objects | Works Near |
|------------|-------------|-----------------|------------|
| **Generic Industrial** | `"AXPG"` | Fences, concrete pads, pipes, clutter | Any industry |
| **Coal Mine Expansion** | `"AXPC"` | Coal storage, pit equipment, conveyor | Coal mine only |
| **Iron Mine Expansion** | `"AXPI"` | Ore crusher, rail loading, headframe | Iron ore mine only |
| **Farm Expansion** | `"AXPF"` | Grain silo, barn, workshop | Farms only |
| **Secondary Expansion** | `"AXPS"` | Warehouse, loading bay, chimney | Secondary industries |
| *(more per industry)* | `"AXP?"` | *(TBD per industry type)* | *(specific industry)* |

Each object class appears as a **separate category** in the Objects menu,
so the player can easily find the right expansion type.

#### Per-industry vs generic counting:

When scanning tiles, both generic AND industry-specific objects count toward
the tile total. A coal mine counts:
- Generic objects (`AXPG`) nearby → count toward total
- Coal-specific objects (`AXPC`) nearby → count toward total
- Farm objects (`AXPF`) nearby → **do NOT count** (wrong industry type)

### 3.2 Economy-Aware Object Visibility

Objects should only appear in the Objects menu when the corresponding industry
exists in the selected economy. E.g., "Coal Mine Expansion" should not appear
if the player selected an economy that has no coal mines.

**OpenTTD limitation:** Objects have no native economy awareness. The
`climate_availability` property only filters by climate (temperate/arctic/
tropical), not by GRF parameters.

**Workaround: `purchase` / `availability` callback:**

Each industry-specific object reads `param[0]` (economy_selection parameter)
and returns available/unavailable:

```nml
switch(FEAT_OBJECTS, SELF, coal_expansion_check_economy, economy_selection) {
    0: return 1;  // BASIC_TEMPERATE — coal mine exists here
    5: return 1;  // STEELTOWN — coal mine exists here
    return 0;     // other economies — hide this object
}

item(FEAT_OBJECTS, coal_expansion_depot, ...) {
    graphics {
        purchase: coal_expansion_check_economy;
        default: coal_expansion_spritelayout;
    }
}
```

**Note:** This mapping (which economy has which industry) must be maintained
manually. When industries are added/removed from economies, the object
availability switches must be updated too. Consider generating this mapping
from the Python industry/economy data during the build.

**Generic objects** (`AXPG`) are always available in all economies — no
economy check needed.

**This approach is unverified** — the exact callback for controlling object
availability in the purchase/build menu needs testing. If `purchase` doesn't
work, alternatives:
- `availability` callback (if it exists for objects)
- Always show all objects but display "(not available in this economy)" in name

### 3.3 Import DWE Sprites

1. Clone ISR-DWE-Objects-II repo
2. Copy sprite sheets from `src (clean concrete)/` to
   `src/graphics/objects/dwe/`
3. Catalog usable sprites (type, size, coordinates)
4. Add GPL v2 attribution in README

### 3.4 Create Object Definitions

**Generic industrial objects** (from DWE sprites):
- Fences, concrete pads, small warehouses, pipes, industrial clutter
- Always available in all economies
- 10-20 objects total

**Industry-specific expansion objects** (from existing AXIS sprites):
- Mining: use sprites from supply_yard, machine_shop, coal_mine
- Farming: use sprites from farm_supply_yard, builders_yard
- Secondary: use sprites from machine_shop, supply_yard
- Economy-filtered via availability callback

### 3.5 Object Numeric IDs

Store in `src/global_constants.py`:
```python
object_numeric_ids = {
    # Generic industrial — IDs 0-49
    "generic_fence_1": 0,
    "generic_concrete_pad": 1,
    "generic_warehouse_small": 2,
    ...
    # Coal mine specific — IDs 50-59
    "coal_storage_depot": 50,
    "coal_pit_equipment": 51,
    ...
    # Iron mine specific — IDs 60-69
    "iron_ore_crusher": 60,
    ...
    # Farm specific — IDs 70-79
    "farm_grain_silo": 70,
    "farm_workshop": 71,
    ...
    # Secondary specific — IDs 90-109
    "factory_warehouse": 90,
    "factory_loading_bay": 91,
    ...
}
```

### 3.6 Build Cost Tuning

Each object has its own `build_cost_multiplier`. Tune so that:
- Generic objects: cheap (~5-10M)
- Specific objects: moderate (~15-35M)
- Scale roughly with industry fund cost

---

## Phase 4 — Workforce System (Passenger Requirement for Expansion)

### Concept

When a primary industry is expanded (expansion tile count reaches Low threshold
or above), the industry **starts requiring passengers** to maintain the
expansion bonus. The idea: expanding a mine means more workers, expanding a
farm means more farmhands. No expansion = no workforce needed.

Additionally, expanded industries **produce passengers** (workers leaving after
their shift). The player must set up transport for both directions.

### Gameplay Flow

1. Player builds a Coal Mine. Normal operation, no passengers involved.
2. Player places expansion buildings around the mine (10+ tiles).
3. The mine reaches Low expansion threshold:
   - Nearby stations now display **"Accepts: Passengers"**
   - The mine starts **producing passengers** (workers needing rides home)
   - Expansion bonus is **only active if passengers are being delivered**
4. Player must set up a bus/train route bringing passengers to the mine.
5. If passengers stop being delivered, expansion bonus drops to 0% (but the
   expansion buildings remain, and the bonus returns when deliveries resume).

### Technical Approach

#### Dynamic cargo acceptance (PASS appears only when expanded)

Use `cargo_acceptance` callback on FEAT_INDUSTRYTILES (callback 0x2B/0x2C).
The callback checks PARENT scope perm storage (`expansion_tile_count`):

```
if expansion_tile_count >= expansion_threshold_low:
    accept PASS (return 8/8 acceptance)
else:
    don't accept PASS (return 0)
```

This affects station coverage display: nearby stations will dynamically show
or hide "Accepts: Passengers" based on the industry's expansion state.

**Note:** The industry's static `accepted_cargos` list (Action 0 property)
does NOT include PASS. The acceptance is purely callback-driven and dynamic.
Need to verify this approach works — if static cargo list is required for the
callback to fire, PASS may need to be in the list with a 0/8 base acceptance
that the callback overrides.

#### Dynamic cargo production (PASS produced only when expanded)

In the `produce_256_ticks` callback, conditionally produce PASS:

```nml
produce(...,
    [
        COAL: (normal_production_formula);
        PASS: (expansion_tile_count >= threshold_low) ? workforce_amount : 0;
    ],
0)
```

PASS must be in the industry's output cargo type list for the produce callback
to output it. Add PASS to output cargo types with base amount 0 — the callback
controls actual production.

The `workforce_amount` could scale with expansion tier:
- Low expansion: 10 passengers per cycle
- Medium expansion: 20 passengers per cycle
- High expansion: 40 passengers per cycle

#### Conditioning expansion bonus on PASS delivery

In `_calculate_expansion_multiplier`, add a check:

```nml
expansion_bonus = (tile_count >= threshold AND passengers_delivered_recently)
                  ? bonus_percent
                  : 100
```

Track passenger delivery using the same 27-cycle mechanism as supplies:
a perm register counting down from 27, reset on PASS delivery.

### New GRF Parameters

| Param | Variable | Default | Description |
|-------|----------|---------|-------------|
| TBD | `expansion_workforce_enabled` | 1 (On) | Toggle workforce requirement |
| TBD | `expansion_workforce_amount` | 10 | Base passengers produced per cycle |

### Files to Modify

| File | Change |
|------|--------|
| `src/industry.py` | Add PASS to output cargo types (conditional), perm register for PASS tracking |
| `src/templates/produce_primary.pynml` | PASS production in produce callback, PASS delivery tracking |
| `src/templates/properties_tile.pynml` | `cargo_acceptance` callback for dynamic PASS acceptance |
| `src/templates/extra_text_primary.pynml` | Show workforce status in industry window |
| `src/lang/english.lng` | Workforce-related strings |
| `src/templates/header.pynml` | New params for workforce toggle/amount |

### Open Questions

- Does `cargo_acceptance` callback work without PASS in the static accepted
  cargo list? If not, PASS must be statically listed with 0/8 base acceptance.
- How does adding PASS to output cargo types interact with economy variations?
  Some economies may not have PASS as a defined cargo.
- Should the workforce requirement apply to ALL primary industries, or only
  mines/industrial types? Farms hiring seasonal workers makes sense, but
  fishing grounds/oil rigs have different flavor.
- Should workforce passengers be separate from town passengers? (Not possible
  — PASS is PASS, no way to distinguish source in OpenTTD.)
- Performance: adding `cargo_acceptance` callback to every industry tile adds
  callback overhead. Profile if needed.

### Dependencies

- Phase 1 (expansion scanning) must be stable.
- Phase 1.3 (object pipeline) must be complete so expansion buildings exist.
- This is independent of Phase 3 (DWE sprites) — workforce works with any
  expansion objects.

---

## Phase 5 — Polish

### 5.1 Visual Feedback on Objects

Objects check `nearby_tile_class` for adjacent industry tiles. If found, show
"active" sprite variant; otherwise show "inactive" variant.

Implementation: object graphics callback with two spritelayouts.

### 5.2 Industry Window Text — Expansion Info Display

Update extra_text templates to display expansion status:
- `src/templates/extra_text_primary.pynml`
- `src/templates/extra_text_secondary.pynml`

**Problem:** There is no NewGRF mechanism to visually highlight a radius zone
around an industry (no overlay, no catchment-style display). The player has
no built-in way to see which tiles "count" toward expansion. Even JGRPP does
not add any such feature.

**Solution:** Clear, informative text in the industry window that tells the
player everything they need to know:

```
Expansion radius: 7 tiles
Expansion objects nearby: 12 / 20 (next: Medium +70%)
Current boost: Low (+30%)
```

The text shows:
1. **Radius** — constant reminder of the scan range (7 tiles from industry)
2. **Current count / next threshold** — how many object tiles found, and how
   many needed for the next tier
3. **Current boost level** — what bonus is currently active

For tiers at maximum level:
```
Expansion objects nearby: 45 / 40 (High +150%)
Current boost: High (+150%)
```

When no expansion objects are present:
```
Expansion radius: 7 tiles
Expansion objects nearby: 0 / 10 (next: Low +30%)
```

For secondary industries without expansion (penalty active):
```
Expansion radius: 7 tiles
Expansion objects nearby: 0 / 10 (next: Normal 1.0x)
Current output: Reduced (0.75x)
```

**Implementation:** Use temp registers to pass values to the string:
- `0x100` — supply thresholds (existing)
- `0x101` — expansion tile count (already added in spike)
- `0x102` — next threshold value
- `0x103` — current boost percentage

The switch block selects the appropriate string based on current tier.

**Strings in:** `src/lang/english.lng`

### 5.3 Snow Variants

Add snow-aware sprite selection for objects in snow climates.

---

## File Change Summary

### New files:
| File | Purpose |
|------|---------|
| `src/objects/__init__.py` | Object registration |
| `src/objects/test_expansion.py` | First test object (Phase 1) |
| `src/objects/*.py` | Additional objects (Phase 3) |
| `src/templates/expansion_scan.pynml` | Tile scan + multiplier calc |
| `src/templates/objects.pynml` | NML template for FEAT_OBJECTS |
| `src/graphics/objects/` | Object sprite sheets (Phase 3) |

### Modified files:
| File | Change |
|------|--------|
| `src/templates/header.pynml` | Add params 10-17 |
| `src/industry.py` | Add perm storage registers |
| `src/templates/produce_primary.pynml` | Scan call + multiplier in formula |
| `src/templates/produce_secondary.pynml` | Scan call + multiplier in formula |
| `src/templates/extra_text_primary.pynml` | Show expansion level (Phase 4) |
| `src/templates/extra_text_secondary.pynml` | Show expansion level (Phase 4) |
| `src/render_nml.py` | Add object rendering loop |
| `src/firs.py` | Register objects |
| `src/global_constants.py` | Object IDs, expansion constants |
| `src/lang/english.lng` | New strings |
| `src/lang_templates/english.pylng` | Templated strings (if needed) |

---

## Open Questions

### Resolved

1. ~~**Phase 0 outcome determines architecture.**~~ **RESOLVED.** `nearby_tile_class`
   is confirmed available for FEAT_INDUSTRIES via NML source code analysis.
   The scan mechanism works from industry production callbacks.

2. ~~**Count all objects or only AXIS+ objects?**~~ **RESOLVED — all objects count.**
   `nearby_tile_object_type` is only available for FEAT_OBJECTS, not for
   FEAT_INDUSTRIES. There is no way for an industry to identify which specific
   object is on a nearby tile. The industry can only detect `TILE_CLASS_OBJECTS`.
   This means ALL objects (AXIS+, other NewGRFs, base game lighthouses, etc.)
   count toward expansion. Accepted for MVP.

3. ~~**JGRPP extra variables?**~~ **RESOLVED — no help.** JGRPP's NewGRF
   additions (checked `newgrf-additions.html` and `newgrf-additions-nml.html`)
   add object properties (`edge_foundation_mode`, `flood_resistant`,
   `use_land_ground`, `map_tile_type`, `foundation_tile_slope`) but **no new
   industry variables** for nearby tile inspection. No `nearby_tile_object_type`
   for FEAT_INDUSTRIES. The limitation is the same in JGRPP and vanilla OpenTTD.

4. ~~**How does the player know the expansion radius?**~~ **RESOLVED — industry
   window text.** There is no NewGRF mechanism to visually highlight a zone
   around an industry (no overlay, no catchment display). Even JGRPP does not
   add this. Solution: clear text in the industry window showing radius (7 tiles),
   current object count, next threshold, and current boost level. See Phase 4.2.

### Known Bugs

**BUG: Scan area only covers south/east of industry, not north/west.**

**Root cause:** `nearby_tile_class` for FEAT_INDUSTRIES uses unsigned offsets
(0-15). Values 8-15 are treated as positive offsets 8-15 by OpenTTD, NOT as
negative offsets -8 to -1. This is a spec limitation: FEAT_INDUSTRIES only
supports unsigned tile offsets, regardless of GRF version.

**Status: NOT FIXED — approach needs decision (see below).**

The FEAT_INDUSTRYTILES approach (signed offsets, per-tile anim_control wrappers)
was implemented and tested in-game. It partially works but has multiple issues:

- **Asymmetric zone**: scan is centered on whichever tile claims the scanner
  role, giving different range in different directions (e.g. coal mine: 7 tiles
  down-left/down-right, 3 tiles up-right, 6 tiles up-left).
- **Non-deterministic**: which tile claims scanner depends on callback firing
  order, so the zone varies unpredictably.
- **Broken for some industries**: clay pit, quarry, and others with
  `ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE` (not `TILE_LOOP`) only scan once
  at construction, then never again.
- **Fluctuating counts**: before scanner lock was added, ALL tiles were scanning
  and overwriting the perm storage count every tick.

The scanner lock (first tile claims the role via `expansion_scanner_pos` perm
register) fixed the fluctuating count but NOT the asymmetry or broken industries.

### Decision Needed: Scan Approach

Three approaches are on the table. A decision is needed before further
implementation work.

**Option 1: FEAT_INDUSTRIES south/east only (simplest)**

Revert to FEAT_INDUSTRIES `nearby_tile_class` with unsigned offsets 0-15.
The scan runs in the 256-tick production callback — no tile animation wrappers,
no scanner lock, no TILE_LOOP patching needed.

- Zone: 16×16 tiles south/east of industry's north corner.
- Perfectly deterministic for all industries and all layout variants.
- Player learns "place expansion objects south/east of the industry."
- Downside: no north/west coverage. Feels arbitrary/directional.
- Works for all industry sizes including 1-tile industries (oil wells).

**Option 2: FEAT_INDUSTRYTILES with fixed scanner tile (all directions)**

Keep FEAT_INDUSTRYTILES signed offsets (-7 to +7) but fix the scanner selection:
at template time (Python), compute which tile is closest to the industry's
bounding box center across all layouts. Hardcode that tile as the scanner.
Fix `_ensure_expansion_tile_loop()` to also patch tiles that have
`ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE` (add `TILE_LOOP` to their trigger
bitmask).

- Zone: 15×15 tiles centered on the scanner tile, all directions.
- Deterministic per industry type (same scanner tile every time).
- Different industry sizes get different effective radius beyond their edge,
  but consistent within a type.
- Downside: complex implementation (per-tile wrappers, PARENT context switches,
  scanner selection logic). Different layout variants may shift the zone
  slightly.
- Edge case: oil wells and other sparse/1-tile industries — scanner tile
  may be in a non-obvious position.

**Option 3: Expansion as fundable industries (no objects/landmarks GRF)**

Instead of scanning for nearby objects, create a per-industry-type "expansion
industry" (e.g. "Coal Mine Expansion", "Arable Farm Expansion") that the player
funds via the industry menu. The expansion industry has a location check
requiring proximity to the parent type.

Two sub-variants:
- **3a — Parent detects expansion industry**: parent scans for the expansion
  industry using `nearby_tile_industry_type`. Same offset limitations as
  Option 1/2 apply.
- **3b — Expansion produces cargo directly**: the expansion industry produces
  the same output cargo as the parent. No inter-industry detection needed.
  The expansion IS the extra production. No scanning at all.

- No Objects/Landmarks GRF dependency.
- Intuitive UX: player funds expansion from industry menu.
- 3b completely avoids the scanning problem.
- Downside: burns industry type slots (limited ~64 per GRF). Each primary
  industry type needs its own expansion industry.
- Downside (3b): changes the design from "multiplier boost" to "separate
  producer" — different gameplay feel.
- Downside: more industry definitions to maintain.

**Option 4: FEAT_INDUSTRYTILES with layout-aware scanner mesh (recommended)**

Instead of choosing one scanner tile per industry, generate a **small fixed set
of scanner tiles per layout**. Each scanner covers only its assigned sub-area
of the industry's expanded bounding box, and the parent industry sums the
partial counts.

Template/build-time shape:

1. For each layout, compute the industry's bounding box.
2. Expand that box by the configured scan radius (currently 7 tiles).
3. Partition the expanded box into 15x15 chunks (or smaller edge chunks),
   because one `FEAT_INDUSTRYTILES` scan can only reach `-7..+7`.
4. For each chunk, choose one real industry tile as the scanner for that
   chunk, preferably the tile nearest the chunk center.
5. In the tileloop callback, each scanner counts only its own chunk and writes
   to its own perm register (e.g. `expansion_chunk_count_1..4`).
6. The industry's 256-tick callback sums the chunk registers into
   `expansion_tile_count`, then calculates `expansion_multiplier` as normal.

- Zone: matches the industry's full expanded footprint, not a circle around one
  arbitrary tile.
- Deterministic for every layout variant.
- Symmetric relative to industry edges, including sparse layouts such as oil
  wells.
- Keeps the original "place objects around the whole industry" design intent.
- More complex than Option 1, but mechanically cleaner than Option 2.
- Requires extra perm storage registers for partial counts; secondary
  industries may need a savegame-version bump if the current unused slots are
  insufficient.
- Requires codegen logic in Python/templates, but that complexity is centralised
  and reusable rather than hidden in per-industry hand patches.

### Preferred fix from current code analysis

The strongest current path is **Option 4: layout-aware scanner mesh using
FEAT_INDUSTRYTILES tileloop callbacks**.

Why this is currently the strongest option:

1. The existing implementation in `src/templates/produce_primary.pynml`
   already emits wrapped nibble offsets (`9..15,0..7`) into generated NML, and
   the generated GRF version is already well above 8. That makes "wrong GRF
   version" much less likely than "FEAT_INDUSTRIES does not actually give the
   signed behaviour we expected here".
2. `FEAT_INDUSTRYTILES` already uses normal signed `nearby_tile_class(x, y)`
   patterns elsewhere in the codebase, so north/west scanning is on much
   firmer ground there.
3. Several extractive industries already have
   `ANIM_TRIGGER_INDTILE_TILE_LOOP`, so there is already an engine-driven,
   periodic tile callback available in this project that can host the scan.
4. A single fixed scanner tile (Option 2) makes the effective radius depend too
   much on layout shape and sparse placement. A scanner mesh lets the scan
   follow the actual footprint of the industry instead of one arbitrary tile.
5. Each industry tile callback can identify its position inside the layout via
   `relative_pos`, which makes per-layout scanner assignment feasible in code
   generation.

#### Proposed implementation shape

1. Add `expansion_chunk_count_n` perm registers for a small fixed maximum
   number of scanner chunks.
2. At template time, compute per-layout expanded bounding boxes and partition
   them into chunk-sized scan regions.
3. Generate `FEAT_INDUSTRYTILES` tileloop switches that activate only on the
   designated scanner tiles for those chunks.
4. Each scanner counts only offsets inside its assigned chunk and stores the
   result into its own chunk register.
5. In the existing industry 256-tick callback, sum the chunk registers into
   `expansion_tile_count`.
6. Calculate `expansion_multiplier` from the summed count.
7. For industries without tileloop-enabled tiles, add a tiny hidden
   "heartbeat" animation to one shared tile type so the callback runs
   periodically without changing visible graphics.

#### Validation spike for this approach

Before broader rollout, test one industry such as `coal_mine`:

1. Reuse its existing tileloop-enabled tile(s).
2. Generate two to four scanner chunks for one known layout.
3. On the designated scanner tiles, scan only the assigned chunk offsets in
   `FEAT_INDUSTRYTILES`.
4. Store each partial count in its own chunk register.
5. Sum them in the industry callback and show the total in extra text or debug
   storage.
6. Verify in game that objects north/west count correctly and that the scan
   area tracks the whole footprint instead of one anchor tile.

If parent perm writes from `FEAT_INDUSTRYTILES, PARENT` prove impossible in
practice, the fallback is to keep the current `FEAT_INDUSTRIES` scan only as a
temporary spike and treat the expansion mechanic as blocked on engine
limitations rather than trying to ship the south/east-only behaviour.

#### Related implementation idea: extend an existing project pattern

This is probably not a completely new architectural direction for AXIS+.
It appears to be an **extension of patterns already used in the codebase**:

1. `FEAT_INDUSTRYTILES` already handles tile-local behaviour.
2. `relative_pos` is already used to make tile behaviour depend on layout
   position.
3. `PARENT` industry-tile switches already exist elsewhere in the project.
4. `ANIM_TRIGGER_INDTILE_TILE_LOOP` is already used by several extractive
   industries, including `oil_wells`.

That means the expansion scan idea is less "invent a new subsystem" and more
"reuse the existing industry-tile callback model for a new purpose".

**Implication:** if this is implemented, it should be designed as a small,
reusable helper/template that plugs into the existing industry-tile callback
flow, not as a one-off special case embedded only in primary production
templates.

**Oil Wells note:** `oil_wells` is not actually a 1x1 industry in this codebase;
it uses sparse multi-tile layouts with several pump tiles spread across the
footprint. That makes it a strong argument for Option 4: a sparse layout is
better represented by multiple scanner chunks following the bounding box than
by one anchor tile in an arbitrary corner or center.

### Still Open

5. **Industry-specific objects count the same as everything else.**
   Because the industry cannot distinguish object types, a "Coal Expansion"
   object has no mechanical advantage over a "Farm Expansion" object placed
   at a coal mine. Per-industry object sets exist only for UX/visual purposes.
   Consider whether this is acceptable long-term or if a workaround should
   be explored (e.g. feature request to OpenTTD for `nearby_tile_object_type`
   on FEAT_INDUSTRIES).

6. **Tertiary industries:** Not planned for expansion support. Confirm.

7. **Multiplier stacking with supplies:** For primary industries, does expansion
   multiply ON TOP of the supply bonus, or independently? Current plan:
   they multiply together (supplies give base boost, expansion multiplies that).

8. **Economy-aware object visibility:** The proposed `purchase` callback approach
   for hiding objects in wrong economies is unverified. Phase 0 spike should
   also test whether this callback works for FEAT_OBJECTS. If not, objects will
   be visible in all economies (cosmetic issue, not a blocker).

9. **Object class grouping:** Each industry type has its own object class
   (e.g. `"AXPC"` for coal). This means many categories in the Objects menu.
   Consider whether a simpler grouping (e.g. just `"AXPG"` generic + `"AXPE"`
   expansion) is better UX, given that all objects count the same anyway.

10. **Other players' objects / griefing in multiplayer.** Since all objects
    count, another player could place random objects near your industry to
    give you a free boost (or clutter your area). This is a minor concern
    for competitive multiplayer but irrelevant for single-player.

### Known Bugs (Phase 1 Spike)

11. **Asymmetric scan zone on industries with mixed tile types.**
    Industries like `clay_pit` have two tile types: `tile_1` (no animation)
    and `tile_2` (`random_first_frame` with `CONSTRUCTION_STATE` trigger).
    Only `tile_1` can act as a scanner (it gets the auto-added `TILE_LOOP`
    trigger). If `tile_1` positions are clustered (e.g. upper-left area),
    the scan reaches 7+ tiles in that direction but only 5-6 tiles in the
    opposite direction. Observed on clay_pit: down-left 5, up-left 8,
    up-right 6, down-right 6 tiles.
    **Fix**: Make `tile_2` (and other `random_first_frame` tiles) also usable
    as scanners by adding `TILE_LOOP` to their triggers and wrapping their
    `anim_control` to return `CB_RESULT_DO_NOTHING` for tile loop calls
    (so the animation isn't reset every ~256 ticks). This requires a
    per-tile-type wrapper switch that distinguishes tile loop from
    construction state triggers — tricky because `extra_callback_info1 = 0`
    is ambiguous between the two. Possible workaround: check
    `animation_frame > 0` (animation already running = tile loop, not
    construction).

12. **Merged quadrants reduce effective scan area for small industries.**
    When the industry footprint is small (e.g. seaweed_farm with 4 tiles),
    multiple quadrants map to the same scanner tile. Their scan areas are
    merged into one scanner, which works correctly but means the total
    scanned area is limited by one scanner's -7..+7 reach. For very small
    industries, the effective scan zone may be 14x14 instead of the full
    expanded bounding box. This is acceptable for gameplay but means the
    scan zone is smaller than intended for tiny industries.
