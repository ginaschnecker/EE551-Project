from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from transcript_to_variables_list import *
from input_to_variables import *
from find_term import *

#edits the second page of the study plan

packet = StringIO.StringIO()
# taking in inputs
grade1= "  "
course1="   "
extra_grade1= "   "
can = canvas.Canvas(packet, pagesize=letter)


#personal info
#can.drawString(70,498, name)
#can.drawString(275,498, ID)
#can.drawString(420,498, classyear)
#can.drawString(510,498, mailbox)
#can.drawString(575,498, email)

#term5
can.drawString(40,414, terms[4])
can.drawString(40,402, terms[4])
can.drawString(40,390, terms[4])
can.drawString(40,378, terms[4])
can.drawString(40,364, terms[4])
can.drawString(40,352, terms[4])

#term5 grades
can.drawString(295,414, EE471_grade)
can.drawString(295,402, CPE487_grade)
can.drawString(295,390, humanity2_grade)
can.drawString(295,378, E321_grade)
can.drawString(295,364, E243_grade)
can.drawString(295,352, E344_grade)

#term6
can.drawString(40,332, terms[5])
can.drawString(40,320, terms[5])
can.drawString(40,308, terms[5])
can.drawString(40,296, terms[5])
can.drawString(40,284, terms[5])
can.drawString(40,272, terms[5])
can.drawString(40,260, terms[5])

#term6 grades
can.drawString(295,332, EE322_grade)
can.drawString(295,320, EE345_grade)
can.drawString(295,308, CPE462_grade)
can.drawString(295,296, E355_grade)
can.drawString(295,284, science1_grade)
can.drawString(295,272, general0_grade)
can.drawString(295,260, grade1)#IDE400_grade)

#term7
can.drawString(360,414, terms[6])
can.drawString(360,402, terms[6])
can.drawString(360,390, terms[6])
can.drawString(360,378, terms[6])
can.drawString(360,364, terms[6])
can.drawString(360,352, terms[6])

#term7 grades
can.drawString(620,414, EE423_grade)
can.drawString(620,402, CPE490_grade)
can.drawString(620,390, IDE401_grade)
can.drawString(620,378, general1_grade)
can.drawString(620,364, technical0_grade)
can.drawString(620,352, technical1_grade)

#term8
can.drawString(360,332, terms[7])
can.drawString(360,320, terms[7])
can.drawString(360,308, terms[7])
can.drawString(360,296, terms[7])
can.drawString(360,284, terms[7])
can.drawString(360,272, terms[7])

#term8 grades
can.drawString(620,332, EE424_grade)
can.drawString(620,320, technical2_grade)
can.drawString(620,308, technical3_grade)
can.drawString(620,296, humanity3_grade)
can.drawString(620,284, general2_grade)
can.drawString(620,272, IDE402_grade)

#classes
can.drawString(125,390, Humanity[2])
can.drawString(150,284, Science[1])
can.drawString(110,272, General[0])
can.drawString(420,378, General[1])
can.drawString(475,364, Technical[0])
can.drawString(475,352, Technical[1])
can.drawString(475,320, Technical[2])
can.drawString(475,308, Technical[3])
can.drawString(450,296, Humanity[3])
can.drawString(420,284, General[2])

#extra courses
can.drawString(435,242, course1)
can.drawString(435,232, course1)
can.drawString(435,222, course1)
can.drawString(435,212, course1)

#extra courses grades
can.drawString(615,242,extra_grade1)
can.drawString(615,232,extra_grade1)
can.drawString(615,222,extra_grade1)
can.drawString(615,212,extra_grade1)

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf_p2 = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("Computer_Engineering_2017.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(1)
page.mergePage(new_pdf_p2.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("/home/gschneck/projectPractice/CPE_StudyPlan/newpdf_p2.pdf", "wb")
output.write(outputStream)
outputStream.close()
