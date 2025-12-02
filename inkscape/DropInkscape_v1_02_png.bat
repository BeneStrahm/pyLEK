@echo off
for %%f in (%*) do (
    echo "%%~f"
    inkscape ^
      --export-area-page ^
      --export-background-opacity=0 ^
      --export-dpi=300 ^
      --export-type="png" ^
      --export-filename="%%~dpnf.png" ^
      "%%~f"
)
pause