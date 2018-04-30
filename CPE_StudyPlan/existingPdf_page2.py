from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from file_to_variables import *

#edits the second page of the study plan

packet = StringIO.StringIO()
# taking in inputs
name="Gina Schnecker"
ID="10300000"
classyear="2018"
mailbox="18-16"
email= "gschneck@stevens.edu"
spring2= "S18"
grade1="A"

#classes
term5hum="third elective"
term8hum="fourth elective"
scielect2="science elective"
genelec1="gen elective1"
genelec2="gen elective2"
genelec3="gen elective3"
techelec1="tech elective1"
techelec2="tech elective2"
techelec3="tech elective3"
techelec4="tech elective4"
course1="course1"
course2="course2"
course3="course3"
course4="course4"
extra_grade1="A"
extra_grade2="A"
extra_grade3="A"
extra_grade4="A"

can = canvas.Canvas(packet, pagesize=letter)


#personal info
can.drawString(70,498, name)
can.drawString(275,498, ID)
can.drawString(420,498, classyear)
can.drawString(510,498, mailbox)
can.drawString(575,498, email)

#term5
can.drawString(40,432, spring2)
can.drawString(40,422, spring2)
can.drawString(40,410, spring2)
can.drawString(40,398, spring2)
can.drawString(40,386, spring2)
can.drawString(40,374, spring2)

#term5 grades
can.drawString(295,432, EE471_grade)
can.drawString(295,422, EE348_grade)
can.drawString(295,410, grade1)
can.drawString(295,398, E321_grade)
can.drawString(295,386, E243_grade)
can.drawString(295,374, E344_grade)

#term6
can.drawString(40,340, spring2)
can.drawString(40,325, spring2)
can.drawString(40,312, spring2)
can.drawString(40,300, spring2)
can.drawString(40,288, spring2)
can.drawString(40,276, spring2)
can.drawString(40,264, spring2)

#term6 grades
can.drawString(295,340, EE322_grade)
can.drawString(295,325, EE345_grade)
can.drawString(295,312, EE448_grade)
can.drawString(295,300, E355_grade)
can.drawString(295,288, grade1)
can.drawString(295,276, grade1)
can.drawString(295,264, grade1)#IDE400_grade)

#term7
can.drawString(360,432, spring2)
can.drawString(360,422, spring2)
can.drawString(360,410, spring2)
can.drawString(360,398, spring2)
can.drawString(360,386, spring2)
can.drawString(360,374, spring2)

#term7 grades
can.drawString(620,432, EE423_grade)
can.drawString(620,422, EE465_grade)
can.drawString(620,410, IDE401_grade)
can.drawString(620,398, grade1)
can.drawString(620,386, grade1)
can.drawString(620,374, grade1)

#term8
can.drawString(360,340, spring2)
can.drawString(360,325, spring2)
can.drawString(360,312, spring2)
can.drawString(360,300, spring2)
can.drawString(360,288, spring2)
can.drawString(360,276, spring2)

#term8 grades
can.drawString(620,340, EE424_grade)
can.drawString(620,325, grade1)
can.drawString(620,312, grade1)
can.drawString(620,300, grade1)
can.drawString(620,288, grade1)
can.drawString(620,276, IDE402_grade)

#classes
can.drawString(125,410, term5hum)
can.drawString(150,288, scielect2)
can.drawString(110,276, genelec1)
can.drawString(420,398, genelec2)
can.drawString(475,386, techelec1)
can.drawString(475,374, techelec2)
can.drawString(475,325, techelec3)
can.drawString(475,312, techelec4)
can.drawString(450,300, term8hum)
can.drawString(420,288, genelec3)

#extra courses
can.drawString(435,233, course1)
can.drawString(435,223, course2)
can.drawString(435,214, course3)
can.drawString(435,205, course2)

#extra courses grades
can.drawString(615,233,extra_grade1)
can.drawString(615,223,extra_grade2)
can.drawString(615,214,extra_grade3)
can.drawString(615,205,extra_grade4)

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
