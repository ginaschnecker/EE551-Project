from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from file_to_variables import *
from input_to_variables import *

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
#scienceelective="science"
sciencelab="laboratory"
grade1="A"
term1="S17"

can = canvas.Canvas(packet, pagesize=letter)


#personal info
can.drawString(70,505, name)
can.drawString(255,505, ID)
can.drawString(385,505, classyear)
can.drawString(460,505, mailbox)
can.drawString(525,505, email)

#term1 terms
can.drawString(40,400, term1)
can.drawString(40,388, term1)
can.drawString(40,376, term1) 
can.drawString(40,364, term1)
can.drawString(40,352, term1)
can.drawString(40,340, term1)
can.drawString(40,328, term1)
can.drawString(40,316, term1)
can.drawString(40,304, term1)

#term1 grades
can.drawString(295,400, CH115_grade)
can.drawString(295,388, CH117_grade)
can.drawString(295,376, E101_grade) 
can.drawString(295,364, E115_grade)
can.drawString(295,352, E120_grade)
can.drawString(295,340, E121_grade)
can.drawString(295,328, MA121_grade)
can.drawString(295,316, MA122_grade)
can.drawString(295,304, CAL103_grade)

#term2 terms
can.drawString(40,260, spring1)
can.drawString(40,248, spring1)
can.drawString(40,236, spring1) 
can.drawString(40,222, spring1)
can.drawString(40,210, spring1)
can.drawString(40,198, spring1)
can.drawString(40,186, spring1)
can.drawString(40,172, spring1)

#term2 grades
can.drawString(295,260, grade1)
can.drawString(295,248, grade1)
can.drawString(295,236, E122_grade) 
can.drawString(295,222, MA123_grade)
can.drawString(295,210, MA124_grade)
can.drawString(295,198, MGT103_grade)
can.drawString(295,186, PEP111_grade)
can.drawString(295,172, CAL105_grade)

#term3 terms
can.drawString(360,400, spring1)
can.drawString(360,388, spring1)
can.drawString(360,376, spring1) 
can.drawString(360,364, spring1)
can.drawString(360,352, spring1)
can.drawString(360,340, spring1)

#term3 grades
can.drawString(625,400, E126_grade)
can.drawString(625,388, E231_grade)
can.drawString(625,376, E245_grade) 
can.drawString(625,364, MA221_grade)
can.drawString(625,352, PEP112_grade)
can.drawString(625,340, grade1)

#term4 term
can.drawString(360,260, spring1)
can.drawString(360,248, spring1)
can.drawString(360,236, spring1) 
can.drawString(360,222, spring1)
can.drawString(360,210, spring1)
can.drawString(360,198, spring1)

#term4 grades
can.drawString(625,260, EE250_grade)
can.drawString(625,248, EE359_grade)
can.drawString(625,236, E232_grade) 
can.drawString(625,222, E234_grade)
can.drawString(625,210, CPE390_grade)
can.drawString(625,198, grade1)

#humanities
can.drawString(450,342, term3_hum)
can.drawString(450,198, term4_hum)

#science elective/lab
can.drawString(150,260, scienceelective)
can.drawString(175,248, sciencelab)

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("StudyPlanElectrical.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("/home/gschneck/projectPractice/newpdf.pdf", "wb")
output.write(outputStream)
outputStream.close()
