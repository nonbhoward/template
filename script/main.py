from pathlib import Path
import os
import sys

# add content roots
print(f'PYTHON PATH SETUP')
sys.path.append(str(Path(os.getcwd()).parent))
print(f'\tcwd is {os.getcwd()}')
for path in sys.path:
    print(f'\tsys.path contains {path}')
