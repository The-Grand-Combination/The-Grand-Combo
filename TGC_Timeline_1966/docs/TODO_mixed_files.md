# TODO mixed files for phase 4

## Completed in phase 3

- `TGC/decisions/00_Setup.txt` was split manually: core is back to the base end-game year, while `TGC_Timeline_1966/decisions/00_Setup.txt` carries the 1966 override.
- `TGC/inventions/navy_inventions.txt` was split manually: core keeps generic key-renaming fixes, while `TGC_Timeline_1966/inventions/navy_inventions.txt` carries the submarine timeline effects as an override carrier file.
- Timeline-only runtime files and assets were removed from `TGC/` after confirming they are staged in `TGC_Timeline_1966/`.
- Mixed UI files with demonstrated timeline dependencies were moved to submod override/carrier files: `buildunit.gui`, `combat.gfx`, `province_interface.gfx`, and `unitpanel.gfx`, plus their directly referenced DDS assets.
- Duplicate non-timeline localisation rows for core commerce inventions were removed from `TGC_Timeline_1966/localisation/1966_other_tech.csv`; `TGC/localisation/00_tech-invent.csv` remains the source for those vanilla/core invention names and descriptions.

## Left intentionally in core

- Generic localisation/encoding/typo fixes in `TGC/localisation/00_tech-invent.csv` and `TGC/localisation/00_technology.csv`. Phase 3 found no remaining lines in those files matching the new 1966 tech/invention key set that were not already carried by the dedicated submod localisation files.
- Historical/flavour references to submarines, province id `1966`, and `submarine_warfare` remain in core because they are not the 1966 runtime timeline extension.

## Remaining follow-up after phase 4

- Re-check localisation duplicate-key behavior with the submod active when doing future content changes.
- Review whether full override carrier files should be minimized further if a safer loader strategy becomes available.
- Keep the submod-aware validator/audit scope in sync whenever timeline runtime files move or new override carrier files are added.
