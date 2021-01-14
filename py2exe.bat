rem *** Used to create a Python exe 

rem ***** get rid of all the old files in the build folder
rd /S /Q dist

rem ***** create the exe
C:\Users\micah\PycharmProjects\MinecraftTextAdventure\venv\Scripts\python setup.py py2exe

rem **** creates sub in dist
mkdir dist\sub

rem **** copies sub into dist\sub
robocopy sub dist\sub /E

rem **** pause so we can see the exit codes
pause "done...hit a key to exit"