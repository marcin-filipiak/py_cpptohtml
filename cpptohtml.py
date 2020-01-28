#!/usr/bin/python

import sys, getopt


def word_colorize(string, word, color):
	if string.find(""+word+" ")>-1:
		out = string[:(string.find(word))]+"<span style=\"color:"+color+";\"> "+word+"</span>"+string[(string.find(word)+len(word)):]
		return out
	else:
		return string

def line_colorize(string, word, color):
	if string.find(word)>-1:
		out = "<span style=\"color:"+color+";\">"+string+"</span>"
		return out
	else:
		return string




def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'cpptohtml.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'cpptohtml.py -i <inputfile> -o <outputfile>'
         		sys.exit()
		elif opt in ("-i", "--ifile"):
        		inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	if outputfile!="" and inputfile!="":
		#wczytanie pliku cpp
		f = open(inputfile, 'r')
		
		#zapis do pliku html
		o = open(outputfile,'w')
		
		o.write("<html>\n\n")

		for line in f:
		
			line = line.replace("&","&amp;")
			line = line.replace("<","&lt;")
			line = line.replace(">","&gt;")
			#line = line.replace("\"","&quot;")
			#line = line.replace(" ","&nbsp;")

			line = line_colorize(line,"#","purple")
			line = line_colorize(line,"//","gray")

			line = word_colorize(line,"if","red")
			line = word_colorize(line,"else","red")
			line = word_colorize(line,"while","red")
			line = word_colorize(line,"break","red")
			line = word_colorize(line,"return","red")
			line = word_colorize(line,"void","green")
			line = word_colorize(line,"int","green")
			line = word_colorize(line,"float","green")
			line = word_colorize(line,"char","green")
			line = word_colorize(line,"double","green")
			line = word_colorize(line,"long","green")
			line = word_colorize(line,"short","green")
			line = word_colorize(line,"bool","green")
			line = word_colorize(line,"const","green")
			line = word_colorize(line,"unsigned","green")

			line = line.replace("\n","<br/>")

			o.write(line)
			#print(line)

		o.write("\n\n </html>")
		o.close()
	else:
		print 'cpptohtml.py -i <inputfile> -o <outputfile>'

if __name__ == "__main__":
   main(sys.argv[1:])
