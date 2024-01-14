# Generacja parsera
antlr4 -Dlanguage=Python3 -no-listener -visitor generated/Graphs.g4

# Instalacja
pip install -r requirements.txt

# Translacja
python Driver.py input.txt

# Uruchomienie otrzymanego programu
python input.py
