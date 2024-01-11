# Generacja parsera
antlr4 -Dlanguage=Python3 -no-listener -visitor generated/Graphs.g4
# Uruchom program
python Driver.py input.txt
