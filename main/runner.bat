set /p name= Copy-paste the root path of the repo here:  
copy renameEntities.exe %name%
pushd %name%
renameEntities.exe
del /f renameEntities.exe