
import sys
import glob
from PyPDF2 import PdfFileMerger

"""
    Name:
    --------
    merge_pdf.py
	
    Author:
    ---------
    Dr Michael GUEDJ

    Description:
    -------------
    This program is part of: prog__my_scripts
    It merges the PDF files:
    -- presents in the working directory;
    -- named: tp0.pdf, tp1.pdf, tp2.pdf, ...
    The resulting file is named: "_tp_.pdf"
"""

def merger(sorted_pdf_to_merge, pdf_resulting):
    pdf_merger = PdfFileMerger()
 
    for path in sorted_pdf_to_merge:
        pdf_merger.append(path)
 
    with open(pdf_resulting, 'wb') as fileobj:
        pdf_merger.write(fileobj)

		
if __name__ == "__main__":
    pdf_resulting = "_tp_.pdf"
    pdf_to_merge = glob.glob('tp*.pdf')
	
    # -- Sorting Stage
    # knowing that the PDF files are named:
    # tp0.pdf, tp1.pdf, ...
    sorted_pdf_to_merge = []
    n = len(pdf_to_merge) # number of the input PDF files
    for i in range(n):
        sorted_pdf_to_merge.append(\
            "tp"+str(i)+".pdf")

    # -- Verification
    # that the list sorted_pdf_to_merge contains
    # the actual files put in pdf_to_merge
    intersection = set(sorted_pdf_to_merge) & set(pdf_to_merge)
    if len(intersection) != n:
        print("Error: the PDF files presents in the working", end=" ")
        print("directory do not follow the naming:")
        print("tp0.pdf, tp1.pdf, tp2.pdf, ...")
        sys.exit("Abort of the running.")
        
    merger(sorted_pdf_to_merge, pdf_resulting)
