#!/bin/bash

source="../prog_c__tp"

#  Name:
#  --------
#  repatrier_pdf.py
#
#  Description:
#  -------------
#  This program is part of: prog__my_scripts
#  It pastes the PDF files presents
#  in the $source directory
#  into the working (current) directory

here=$(pwd)

cd "$source"

for x in $( ls )
do 
	cd $x
	for y in $( ls *.pdf)
	do
		cp $y $here
	done 
	cd ..
done
