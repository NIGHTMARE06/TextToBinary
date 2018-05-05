#!/usr/bin/env python3.5
import sys

print("\033[1;32m" + "Que tipo de traduccion necesitas?")
print("\033[1;37m" + "Binario a texto(0)\nTexto a binario(1)\n")
type = input("> " + "\033[1;37m")

if type == "1":
    print("\n" + "\033[1;31m" + "Ingresa un texto:")
    text = input("> " + "\033[1;37m")
    print("\033[1;36m")
    print(bin(int.from_bytes(text.encode(), 'big')).replace("b",""))
elif type == "0":
    print("\n" + "\033[1;36m" + "Ingresa un texto(Binario):")
    text = input("> " + "\033[1;37m")
    print("\033[1;31m")
    bin = int(text,2)
    print(bin.to_bytes((bin.bit_length() + 7) // 8,'big').decode())
else:
    print("Elige uno de los dos tipos de traduccion")
    sys.exit(0)
