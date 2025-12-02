@echo off
for %%f in (%*) do (
    echo %%~f
    inkscape ^
      --export-type="pdf" ^
      --export-latex ^
      --export-filename="%%~dpnf.pdf" ^
      %%~f
)