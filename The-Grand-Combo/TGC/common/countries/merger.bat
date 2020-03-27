@echo off

set "src=C:\mod\TGC\common\countries"

for /r "%src%" %%A in (*.txt) do (
    echo insert text >> "%%~fA"
)