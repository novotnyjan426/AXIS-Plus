# AXIS+ Auto Memory

## Project
- OpenTTD NewGRF industry set forked from FIRS, ~128 industries
- Build: `python src/render_nml.py` then `nmlc generated/firs.nml --grf=axis_plus_test.grf --lang-dir=generated/lang`
- Test GRF goes to: `C:/Users/novot/Documents/OpenTTD/content_download/newgrf/`
- See `CLAUDE.md` in repo root for full project context

## User Preferences
- Language: Czech (messages often in Czech, "ano" = yes)
- Prefers direct action over lengthy explanations
- Comfortable with OpenTTD/NewGRF internals

## Key Learnings
- Chameleon TAL text-format templates: string literals in `${}` don't evaluate — precompute in Python
- NML switches: callee must be defined before caller (no forward refs)
- FEAT_INDUSTRIES signed_offsets=false — can't scan north/west. Use FEAT_INDUSTRYTILES instead.
- STORE_PERM from tile context: must use FEAT_INDUSTRYTILES PARENT scope, not SELF
- STORE_PERM_ALT is project wrapper, only works from FEAT_INDUSTRIES SELF
- TEMP registers bridge SELF→PARENT scope (persist across scope changes in resolver)

## Current Work (as of 2026-03-13)
- Phase 1 scanner mesh: 41 primary industries wired
- Phase 2 expansion objects: 43/44 primaries covered (see [expansion_objects_status.md](expansion_objects_status.md))
- Template supports 7 modes: plain, single sprite, multi-building, animated, multi-tile grid, base_sprite, slope-aware trees
- Known bugs: asymmetric scan for mixed tile_type industries (see EXPANSION_PLAN.md #11-12)
- Known bugs: see `memory/animation_objects.md` for object animation issues

## Reference Files
- [slope_aware_objects.md](slope_aware_objects.md) — How to make slope-aware FEAT_OBJECTS (from AuzObjects GRF reverse-engineering)
- [industry_catalog.md](industry_catalog.md) — Quick-reference cargo/type summary (memory version, less detailed)
- [expansion_objects_status.md](expansion_objects_status.md) — Which primaries have expansion objects (44/44 after bulk_terminal)
- **INDUSTRY_CATALOG.md** (repo root) — Full user-friendly catalog: all 129 industries with per-economy inputs/outputs, arrows (<-/->), multipliers, production formulas, display names. THE canonical reference for industry data.
