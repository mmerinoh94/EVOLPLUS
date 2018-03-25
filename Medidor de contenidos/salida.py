#-*- coding: utf8 -*-

import shlex,subprocess
command_line='convert -density 300 nombrePDF.pdf -depth 8 -strip -background white -alpha off salida.tiff'
args=shlex.split(command_line)
subprocess.call(args)

command='tesseract salida.tiff output'
argument=shlex.split(command)
subprocess.call(argument)

archivo=open('output.txt','r')
cad=archivo.read()
#print(cad)

archivo.close()
