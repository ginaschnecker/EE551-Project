from PyPDF2 import PdfFileMerger


#combines first two pages

pdfs = ['newpdf.pdf', 'newpdf_p2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
	merger.append(open(pdf, 'rb'))
with open('FinalStudyPlan.pdf','wb') as fout:
	merger.write(fout)



