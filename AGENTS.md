# AGENTS.md

## Validation trigger policy
Run validation from repository root only when the current task includes:

- changes to files covered by the 1966 extension ruleset/tooling, or
- analysis/review requests specifically about 1966 extension validity or balance.

In those cases, run:

- `python TGC/tools/validate_1966_extension.py`
- `python TGC/tools/audit_1966_balance.py`

If the task does **not** touch/assess 1966 extension validity or balance, skip these checks.

## TGC core / 1966 timeline submod synchronization
- `TGC/` is the non-1966 core mod; `TGC_Timeline_1966/` is the 1966 runtime submod.
- Some timeline files are full override/carrier files and can mask core fixes. Generic fixes made in the submod should not remain submod-only unless there is a clear reason.
- When changing a core `TGC/` file that may have a timeline override/carrier, run or explicitly consider `python TGC/tools/check_1966_submod_drift.py`; decide whether to port the change into the submod while preserving 1966 timeline hunks, or explain why not.
- When changing a `TGC_Timeline_1966/` file that is not clearly timeline-only, run or explicitly consider `python TGC/tools/check_1966_submod_drift.py --reverse`; decide whether to port the generic part back to core without bringing 1966 content into `TGC/`, or explain why not.
- Never transfer changes between core and submod automatically: porting must be intentional, drift WARN entries require manual review, and drift FAIL entries must be fixed before proceeding.
- After syncing from the original/upstream mod, treat core/submod drift verification as mandatory. If possible, use the pre-sync commit as `<pre-sync-ref>` and run or explicitly consider `python TGC/tools/check_1966_submod_drift.py --base-ref <pre-sync-ref>` and `python TGC/tools/check_1966_submod_drift.py --reverse --base-ref <pre-sync-ref>`; CI runs both with `--fail-on-warn` for pull requests, pushes, and manual dispatches, so WARNs must be resolved by porting/adapting the change to the counterpart or clearly explaining why it should not transfer.
- After changes affecting 1966 content or rules, continue to run `python TGC/tools/validate_1966_extension.py` and `python TGC/tools/audit_1966_balance.py`.

## If validation fails
Do not patch immediately.
First provide a diagnosis and classify the issue as:
- tool bug
- rules/doc issue
- gameplay/balance issue

## If validation passes
Proceed with the requested task.
Always report:
- validator result
- FAIL/WARN/INFO counts from the audit
- PRIORITY SUMMARY
- RECOMMENDED PLAYTEST FOCUS
