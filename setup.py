# Instalar a biblioteca do cx_Freeze: pip install cx_Freeze
# Executar: python setup.py build

from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None

if sys.platform == 'win32':
    base = "Win32GUI"


setup(
    name="Meu App",
    version="0.1",
    description="Minha 1° Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("calculadora.py", base=base)]
)
