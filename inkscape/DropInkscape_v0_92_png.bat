@echo off
for %%f in (%*) do (
    echo %%~f
    "C:\Program Files\Inkscape\inkscape.exe" ^
      -z ^
      --export-background-opacity=0 ^
      --export-dpi=300 ^
      --export-png="%%~dpnf.png" ^
      --file="%%~f"

)