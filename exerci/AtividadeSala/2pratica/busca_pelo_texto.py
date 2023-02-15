import sys

arquivo=sys.argv[1]
maior=0
with open (arquivo,'r') as f:
    for linha in f:
        num=int(linha)