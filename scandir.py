import os

for entry in os.scandir('/Library/Extensions'):
    if not entry.name.startswith('.'):
        print(entry.name)
