# AXIS+ Project Context

## What This Is

AXIS+ is an OpenTTD NewGRF industry set, forked from FIRS. It adds ~128 industries with custom production mechanics. The main new feature being developed is an **expansion system** where players place objects near industries to boost production.

License: GPL v2.

## Build Pipeline

1. **Python codegen** generates NML from Chameleon/TAL templates:
   ```
   python src/render_nml.py     # ~1.5s, outputs generated/nml/*.nml and generated/firs.nml
   ```
2. **nmlc** compiles the concatenated NML to GRF:
   ```
   nmlc generated/firs.nml --grf=axis_plus_test.grf --lang-dir=generated/lang
   ```
3. Copy GRF for testing:
   ```
   cp axis_plus_test.grf "C:/Users/novot/Documents/OpenTTD/content_download/newgrf/"
   ```

## Key Architecture

### File Layout
- `src/industry.py` — Core `Industry` class (line ~1163) and subclasses (`IndustryPrimary` ~1743, `IndustryPrimaryExtractive` ~1843, etc.)
- `src/industries/*.py` — Per-industry definitions (128 industries)
- `src/templates/*.pynml` — Chameleon TAL text-format templates generating NML
- `src/render_nml.py` — Template renderer, produces `generated/firs.nml`
- `src/firs.py` — Global config, paths
- `generated/nml/*.nml` — Per-industry generated NML (useful for debugging)
- `generated/firs.nml` — Concatenated NML fed to nmlc

### Template System (Chameleon TAL, text format)
- `${expression}` for inline Python expressions
- `<tal:block condition="python:...">` for conditionals
- `<tal:repeat repeat="item list">` for loops — `repeat.item.start`, `repeat.item.end`, `repeat.item.index`
- **Gotcha**: String literals inside `${}` in text-format templates don't evaluate properly. Precompute values in Python instead of doing string ops in templates.
- Templates loaded via `PageTemplateLoader` with `format="text"`

### NML/NewGRF Concepts
- **FEAT_INDUSTRIES** — Industry-level scope. `signed_offsets=false` for var 0x62 (nearby_tile_class). Can only see south/east with nibble offsets.
- **FEAT_INDUSTRYTILES** — Tile-level scope. `signed_offsets=true` for var 0x60. Can see all 4 directions with -7..+7 offsets.
- **PARENT scope** — From FEAT_INDUSTRYTILES, accesses parent industry's perm storage. Required for `STORE_PERM` from tile context.
- **SELF scope** — Direct scope. For FEAT_INDUSTRYTILES SELF, `has_persistent_storage=false` (no STORE_PERM).
- **TEMP registers** — Persist across scope changes within a single resolver chain. Bridge SELF→PARENT data flow.
- **STORE_PERM_ALT** — Project-specific wrapper (in `perm_storage_mappings.pynml`), only works from `FEAT_INDUSTRIES, SELF`. Use raw `STORE_PERM(value, register)` from PARENT scope.
- **NML switch order** — Callee must be defined before caller (no forward references).
- **relative_pos** — NML var 0x43 for FEAT_INDUSTRYTILES, returns `0xYYXX`. `relative_coord(x, y)` produces matching value.

### Perm Storage
- Registered via `register_perm_storage_mapping()` in `industry.py`
- `get_perm_num("name")` returns the register index (passed to templates)
- IndustryPrimary uses registers 0-44 (see `IndustryPrimary.__init__`)

## Expansion System (In Progress)

### Design: Option 4 — Layout-Aware Scanner Mesh
See `EXPANSION_PLAN.md` for full design document (especially lines 732-850).

### How It Works
1. `Industry.get_expansion_scanner_mesh()` (industry.py:1605) partitions expanded bounding box into 2x2 quadrant chunks
2. Each chunk gets a scanner tile (nearest industry tile to chunk center)
3. `expansion_scan_tile.pynml` generates FEAT_INDUSTRYTILES switch chains:
   - Store switch (PARENT scope, STORE_PERM) — defined first (NML ordering)
   - Row scan switches (SELF scope, signed offsets -7..+7) — chain first→last
   - Entry switch (zeros TEMP(0x10), chains to last row)
   - Layout dispatch (checks relative_pos to identify scanner tiles)
   - Layout selector (PARENT scope, checks layout_num)
4. `produce_primary.pynml` sums chunk registers in 256-tick callback (`_sum_expansion_chunks`)
5. `_calculate_expansion_multiplier` compares tile count to GRF parameter thresholds
6. Production formula multiplies supply boost by expansion multiplier

### Current Status (Phase 1 Spike)
- **Working**: 10 mine-type industries with `first_frame_is_0` animation tiles
- **Not yet wired**: Non-mine primaries (farms, forests, ports) — need `ANIM_TRIGGER_INDTILE_TILE_LOOP` added to at least one tile per industry
- **Scan direction bug**: FEAT_INDUSTRIES can't see north/west (signed_offsets=false in OpenTTD source). Option 4 fixes this by scanning from FEAT_INDUSTRYTILES instead.
- **Validated**: coal_mine generates correct signed offsets, PARENT scope STORE_PERM, 4-chunk summation. GRF compiles clean.

### Next Steps
- In-game test: place objects north/west of coal mine, verify expansion bonus
- Wire remaining primaries: add animation hook to non-mine industries
- Phase 2: Create expansion NewGRF objects (ISR-DWE-Objects-II based)

## Industry Class Hierarchy
```
Industry (line 1163)
  IndustryPrimary (1743) — produces cargo, optional supply boost + expansion scan
    IndustryPrimaryExtractive (1843) — mines, accepts ENSP
    IndustryPrimaryOrganic (1860) — farms, accepts FMSP
    IndustryPrimaryPort (1877) — ports, multiple accept cargos
    IndustryPrimaryNoSupplies (1893) — no supply input
  IndustrySecondary (1905+) — processes input cargo
  IndustryTertiary (further down) — town-related
```

## Useful Commands
```bash
# Quick check: which industries have expansion scan enabled
grep -l "expansion_scan_entry" generated/nml/*.nml

# Check specific industry's generated NML
cat generated/nml/coal_mine.nml | grep -A5 "scan_l1_c0"

# Full rebuild + compile
python src/render_nml.py && nmlc generated/firs.nml --grf=axis_plus_test.grf --lang-dir=generated/lang
```
