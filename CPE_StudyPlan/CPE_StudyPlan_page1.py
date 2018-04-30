from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from transcript_to_variables_list import *
from input_to_variables import *
from find_term import *

#edits the first page of the study plan


packet = StringIO.StringIO()
# taking in inputs
name="Gina Schnecker"
ID="10300000"
classyear="2018"
mailbox="18-16"
email= "gschneck@stevens.edu"
spring1= "S17"
term3_hum="first elective"
term4_hum="second elective"
scienceelective="science"
sciencelab="laboratory"
grade1="A"
#term1="S17"

can = canvas.Canvas(packet, pagesize=letter)


#personal info
#can.drawString(70,505, name)
#can.drawString(255,505, ID)
#can.drawString(385,505, classyear)
#can.drawString(460,505, mailbox)
#can.drawString(525,505, email)

#term1 terms
can.drawString(40,390, terms[0])
can.drawString(40,376, terms[0])
can.drawString(40,362, terms[0]) 
can.drawString(40,348, terms[0])
can.drawString(40,334, terms[0])
can.drawString(40,320, terms[0])
can.drawString(40,308, terms[0])
can.drawString(40,296, terms[0])
can.drawString(40,284, terms[0])

#term1 grades
can.drawString(295,390, CH115_grade)
can.drawString(295,376, CH117_grade)
can.drawString(295,362, E101_grade) 
can.drawString(295,348, E115_grade)
can.drawString(295,334, E120_grade)
can.drawString(295,320, E121_grade)
can.drawString(295,308, MA121_grade)
can.drawString(295,296, MA122_grade)
can.drawString(295,284, CAL103_grade)

#term2 terms
can.drawString(40,230, terms[1])
can.drawString(40,218, terms[1])
can.drawString(40,204, terms[1]) 
can.drawString(40,190, terms[1])
can.drawString(40,176, terms[1])
can.drawString(40,162, terms[1])
can.drawString(40,146, terms[1])
can.drawString(40,132, terms[1])

#term2 grades
can.drawString(295,230, science0_grade)
can.drawString(295,218, sciencelab0_grade)
can.drawString(295,204, E122_grade) 
can.drawString(295,190, MA123_grade)
can.drawString(295,176, MA124_grade)
can.drawString(295,162, MGT103_grade)
can.drawString(295,146, PEP111_grade)
can.drawString(295,132, CAL105_grade)

#term3 terms
can.drawString(360,390, terms[2])
can.drawString(360,376, terms[2])
can.drawString(360,362, terms[2]) 
can.drawString(360,348, terms[2])
can.drawString(360,334, terms[2])
can.drawString(360,320, terms[2])

#term3 grades
can.drawString(625,390, E126_grade)
can.drawString(625,376, E231_grade)
can.drawString(625,362, E245_grade) 
can.drawString(625,348, MA221_grade)
can.drawString(625,334, PEP112_grade)
can.drawString(625,320, humanity0_grade)

#term4 term
can.drawString(360,230, terms[3])
can.drawString(360,218, terms[3])
can.drawString(360,204, terms[3]) 
can.drawString(360,190, terms[3])
can.drawString(360,176, terms[3])
can.drawString(360,162, terms[3])

#term4 grades
can.drawString(625,230, CPE360_grade)
can.drawString(625,218, CPE390_grade)
can.drawString(625,204, E232_grade) 
can.drawString(625,190, E234_grade)
can.drawString(625,176, MA134_grade)
can.drawString(625,162, humanity1_grade)

#humanities
can.drawString(450,320, Humanity[0])
can.drawString(450,162, Humanity[1])

#science elective/lab
can.drawString(150,230, Science[0])
can.drawString(185,218, ScienceLab[0])

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("Computer_Engineering_2017.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("/home/gschneck/projectPractice/CPE_StudyPlan/newpdf.pdf", "wb")
output.write(outputStream)
outputStream.close()
