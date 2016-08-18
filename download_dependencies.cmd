pushd ..\%1

cd %1
dir

IF EXIST dependencies RMDIR /q /s dependencies
MKDIR dependencies

%programdata%\qualisystems\qspython27\Scripts\pip download -r requirements.txt -d dependencies -p https://testpypi.python.org
del dependencies\cloudshell*


popd