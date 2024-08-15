del build
del dist
del main.spec
del __pycache__
pyinstaller --noconfirm --onefile --windowed --icon "D:/FlappyAmogus/Icons/icon.ico" --key "turipipipipturrip" --add-data "D:/FlappyAmogus/Graphics;Graphics/" --add-data "D:/FlappyAmogus/Sounds;Sounds/"  "D:/FlappyAmogus/main.py"
ren dist/main.exe Flappy Amongus.exe