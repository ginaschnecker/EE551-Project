from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

transcriptList = [' ------------------------2015 Fall--------------------------\r\n',
                  'Class: CAL-105-H Grade: A-', 'Class: E-101-A Grade: P', 'Class: E-115-LF Grade: A',
                  'Class: E-120-K Grade: A', 'Class: E-121-C Grade: A', 'Class: MA-124-C Grade: A',
                  'Class: MA-461-CC Grade: A', 'Class: PEP-112-RF Grade: A',
                  ' -----------------------2016 Spring-------------------------\r\n',
                  'Class: CAL-103-A Grade: A-', 'Class: E-122-D Grade: A', 'Class: E-126-A Grade: A',
                  'Class: E-245-C Grade: A', 'Class: MA-221-F Grade: A', 'Class: MGT-103-R Grade: A',
                  ' ------------------------2016 Fall--------------------------\r\n',
                  'Class: CPE-360-A Grade: A', 'Class: CPE-390-A Grade: A', 'Class: E-231-D Grade: A',
                  'Class: E-234-RB Grade: A', 'Class: HHS-125-A Grade: A', 'Class: MA-134-A Grade: A-',
                  'Class: MA-462-A Grade: A', 'Class: PE-200-G7 Grade: P',
                  ' -----------------------2018 Spring-------------------------\r\n',
                  'Class: CPE-322-A Grade: ', 'Class: CPE-345-A Grade: ', 'Class: CPE-462-A Grade: ',
                  'Class: E-355-B Grade: ', 'Class: EE-551-A Grade: ', 'Class: EN-250-W1 Grade: ',
                  'Class: PE-200-G4 Grade: ']

classList = [[],
             ['General:MA 461', 'CH 115', 'CH 117', 'E 101', 'E 121', 'E 120', 'E 115', 'MA 121', 'CAL 103'],
             ['Science:CH 116', 'ScienceLab:CH 118', 'E 122', 'MA 123', 'PEP 111', 'CAL 105', 'MGT 103'],
             ['Humanity:HHS 125', 'General:MA 462', 'MA 221', 'MA 221R', 'PEP 112', 'PEP 112R', 'E 126', 'E 245', 'E 245L', 'E 231'],
             ['Humanity:HUM2', 'MA 134', 'E 232', 'E 232L', 'E 234', 'E 234R', 'CPE 360', 'CPE 390L', 'CPE 390'],
             ['Humanity:HUM3', 'Extra:EXTRA1', 'EE 471', 'E 344', 'E 321', 'E 243', 'E 243R', 'CPE 487'],
             ['Science:PEP 151', 'EE 345', 'E 355', 'CPE 322', 'CPE 462', 'IDE 400'],
             ['Technical:TECH1', 'Technical:TECH2', 'CPE 490', 'CPE 423', 'IDE 401'],
             ['Humanity:HUM4', 'Technical:TECH3', 'Technical:TECH4', 'CPE 424', 'IDE 402']

            ]

for semester in classList:
	counter = 0
	for clss in semester:
		if ((clss[-1:] == "L") or (clss[-1:] == "R")):
			del semester[counter]
		counter = counter+1
print classList

#Change the data structure for each course to [type, course, grade]
for semester in classList:
    counter = 0
    for clss in semester:
        tempList = ["Core", " ", " "]
        if ":" in clss:
            clssSplit = clss.split(":")
            tempList[0] = clssSplit[0]
            tempList[1] = " " + clssSplit[1].replace(" ", "-")
        else:
            tempList[1] = " " + clss.replace(" ", "-")
        semester[counter] = tempList
        counter = counter + 1

#Get the grade from transcript if available
for semester in classList:
    for clss in semester:
        for line in transcriptList:
            if clss[1] in line:
                gradeArray = line.split("Grade: ")
                if len(gradeArray) > 1:
                    clss[2] = gradeArray[1]

##print classList

def writeTerm(term, firstTerm):
	if term%2==1:
		firstChar="F"	
	else:
		firstChar="S"
	currentTerm=firstTerm
	for x in xrange(0,term,+2):
		currentTerm=currentTerm+1
	return firstChar + str(currentTerm)	

CH115_term=" "
CH115_grade=" "
CH117_term=" "
CH117_grade=" "
E101_term=" "
E101_grade=" "
E115_term=" "
E115_grade=" "
E120_term=" "
E120_grade=" "
E121_term=" "
E121_grade=" "
MA121_term=" "
MA121_grade=" "
MA122_term=" "
MA122_grade=" "
CAL103_term=" "
CAL103_grade=" "
E122_term=" "
E122_grade=" "
MA123_term=" "
MA123_grade=" "
MA124_term=" "
MA124_grade=" "
MGT103_term=" "
MGT103_grade=" "
PEP111_term=" "
PEP111_grade=" "
CAL105_term=" "
CAL105_grade=" "
E126_term=" "
E126_grade=" "
E231_term=" "
E231_grade=" "
E245_term=" "
E245_grade=" "
MA221_term=" "
MA221_grade=" "
PEP112_term=" "
PEP112_grade=" "
EE250_term=" "
EE250_grade=" "
EE359_term=" "
EE359_grade=" "
E232_term=" "
E232_grade=" "
E234_term=" "
E234_grade=" "
CPE390_term=" "
CPE390_grade=" "
EE471_term=" "
EE471_grade=" "
EE348_term=" "
EE348_grade=" "
E312_term=" "
E312_grade=" "
E243_term=" "
E243_grade=" "
E344_term=" "
E344_grade=" "
EE322_term=" "
EE322_grade=" "
EE345_term=" "
EE345_grade=" "
EE448_term=" "
EE448_grade=" "
E355_term=" "
E355_grade=" "
IDE400_term=" "
IDE400_grade=" "
EE423_term=" "
EE423_grade=" "
EE465_term=" "
EE465_grade=" "
IDE401_term=" "
IDE401_grade=" "
EE424_term=" "
EE424_grade=" "
IDE402_term=" "
IDE402_grade=" "
MA134_term=" "
MA134_grade=" "
CPE360_term=" "
CPE360_grade=" "
CPE487_term=" "
CPE487_grade=" "
CPE462_term=" "
CPE462_grade=" "
CPE345_term=" "
CPE345_grade=" "
CPE322_term=" "
CPE322_grade=" "
CPE423_term=" "
CPE423_grade=" "
CPE490_term=" "
CPE490_grade=" "
CPE424_term=" "
CPE424_grade=" "
General1=" "
General1_grade=" "
gen1=False
General2=" "
General2_grade=" "
General3_grade=" "
General3=" "
gen2=False
gen3=False
Technical1=" "
Technical1_grade=" "
tech1=False
Technical2=" "
Technical2_grade=" "
tech2=False
Technical3=" "
Technical3_grade=" "
tech3=False
Technical4=" "
Technical4_grade=" "
tech4=False
Humanity1=" "
Humanity1_grade=" "
hum1=False
Humanity2=" "
Humanity2_grade=" "
hum2=False
Humanity3=" "
Humanity3_grade=" "
hum3=False
Humanity4=" "
Humanity4_grade=" "
hum4=False
Science1=" "
Science1_grade=" "
sci1=False
Science2=" "
Science2_grade=" "
sci2=False
ScienceLab1=" "
ScienceLab1_grade=" "
scil1=False
Extra1=" "
Extra1_grade=" "
ext1=False
Extra2=" "
Extra2_grade=" "
ext2=False
Extra3=" "
Extra3_grade=" "
ext3=False
Extra4=" "
Extra4_grade=" "
ext4=False
General1_term=" "
General2_term=" "
General3_term=" "
Technical1_term=" "
Technical2_term=" "
Technical3_term=" "
Technical4_term=" "
Humanity1_term=" "
Humanity2_term=" "
Humanity3_term=" "
Humanity4_term=" "
Science1_term=" "
Science2_term=" "
ScienceLab1_term=" "
Extra1_term=" "
Extra2_term=" "
Extra3_term=" "
Extra4_term=" "


counter =0
for semester in classList:
	  
	for clss in semester:
		#print clss[1]
		if " CAL-105" in clss[1]:
			CAL105_grade =clss[2]
			#print CAL105_grade
			CAL105_term=writeTerm(counter,18)
			#print CAL105_term
		if " CH-117" in clss[1]:
			CH117_grade =clss[2]
			#print CH117_grade
			CH117_term=writeTerm(counter,18)
			#print CH117_term
		if " CH-115" in clss[1]:
			CH115_grade =clss[2]
			#print CH115_grade
			CH115_term=writeTerm(counter,18)
			#print CH115_term
		if " E-101" in clss[1]:
			E101_grade =clss[2]
			#print E101_grade
			E101_term=writeTerm(counter,18)
			#print E101_term
		if " E-115" in clss[1]:
			E115_grade =clss[2]
			#print E115_grade
			E115_term=writeTerm(counter,18)
			#print E115_term
		if " E-121" in clss[1]:
			E121_grade =clss[2]
			#print E121_grade
			E121_term=writeTerm(counter,18)
			#print E121_term
		if " E-120" in clss[1]:
			E120_grade =clss[2]
			#print E120_grade
			E120_term=writeTerm(counter,18)
			#print E120_term
		if " MA-121" in clss[1]:
			MA121_grade =clss[2]
			#print MA121_grade
			MA121_term=writeTerm(counter,18)
			#print MA121_term
		if " MA-122" in clss[1]:
			MA122_grade =clss[2]
			#print MA122_grade
			MA122_term=writeTerm(counter,18)
			#print MA122_term
		if " CAL-103" in clss[1]:
			CAL103_grade =clss[2]
			#print CAL103_grade
			CAL103_term=writeTerm(counter,18)
			#print CAL103_term	
		if " E-122" in clss[1]:
			E122_grade =clss[2]
			#print E122_grade
			E122_term=writeTerm(counter,18)
			#print E121_term
		if " MA-123" in clss[1]:
			MA123_grade =clss[2]
			#print MA123_grade
			MA123_term=writeTerm(counter,18)
			#print MA123_term
		if " MA-124" in clss[1]:
			MA124_grade =clss[2]
			#print MA124_grade
			MA124_term=writeTerm(counter,18)
			#print MA124_term
		if " MGT-103" in clss[1]:
			MGT103_grade =clss[2]
			#print MGT103_grade
			MGT103_term=writeTerm(counter,18)
			#print MGT103_term
		if " PEP-111" in clss[1]:
			PEP111_grade =clss[2]
			#print PEP111_grade
			PEP111_term=writeTerm(counter,18)
			#print PEP111_term
		if " E-126" in clss[1]:
			E126_grade =clss[2]
			#print E126_grade
			E126_term=writeTerm(counter,18)
			#print E126_term
		if " E-231" in clss[1]:
			E231_grade =clss[2]
			#print E231_grade
			E231_term=writeTerm(counter,18)
			#print E231_term
		if " E-245" in clss[1]:
			E245_grade =clss[2]
			#print E245_grade
			E245_term=writeTerm(counter,18)
			#print E245_term
		if " MA-221" in clss[1]:
			MA221_grade =clss[2]
			#print MA221_grade
			MA221_term=writeTerm(counter,18)
			#print MA221_term
		if " PEP-112" in clss[1]:
			PEP112_grade =clss[2]
			#print PEP112_grade
			PEP112_term=writeTerm(counter,18)
			#print PEP112_term
		if " EE-250" in clss[1]:
			EE250_grade =clss[2]
			#print EE250_grade
			EE250_term=writeTerm(counter,18)
			#print EE250_term
		if " EE-359" in clss[1]:
			EE359_grade =clss[2]
			#print EE359_grade
			EE359_term=writeTerm(counter,18)
			#print EE359_term
		if " E-234" in clss[1]:
			E234_grade =clss[2]
			#print E234_grade
			E234_term=writeTerm(counter,18)
			#print E234_term
		if " E-321" in clss[1]:
			E321_grade =clss[2]
			#print E231_grade
			E321_term=writeTerm(counter,18)
			#print E321_term
		if " E-232" in clss[1]:
			E232_grade =clss[2]
			#print E232_grade
			E232_term=writeTerm(counter,18)
			#print E232_term
		if " CPE-390" in clss[1]:
			CPE390_grade =clss[2]
			#print CPE390_grade
			CPE390_term=writeTerm(counter,18)
			#print CPE390_term
		if " EE-471" in clss[1]:
			EE471_grade =clss[2]
			#print E126_grade
			EE471_term=writeTerm(counter,18)
			#print EE471_term
		if " EE-348" in clss[1]:
			EE348_grade =clss[2]
			#print EE348_grade
			EE348_term=writeTerm(counter,18)
			#print EE348_term
		if " E-355" in clss[1]:
			EE355_grade =clss[2]
			#print EE355_grade
			E355_term=writeTerm(counter,18)
			#print E355_term
		if " IDE-400" in clss[1]:
			IDE400_grade =clss[2]
			#print IDE400_grade
			IDE400_term=writeTerm(counter,18)
			#print IDE400_term
		if " EE-423" in clss[1]:
			EE423_grade =clss[2]
			#print EE423_grade
			EE423_term=writeTerm(counter,18)
			#print EE423_term
		if " EE-465" in clss[1]:
			EE465_grade =clss[2]
			#print EE465_grade
			EE465_term=writeTerm(counter,18)
			#print EE465_term
		if " IDE-401" in clss[1]:
			IDE401_grade =clss[2]
			#print IDE401_grade
			IDE401_term=writeTerm(counter,18)
			#print IDE401_term
		if " EE-424" in clss[1]:
			EE424_grade =clss[2]
			#print EE424_grade
			EE424_term=writeTerm(counter,18)
			#print EE424_term
		if " IDE-402" in clss[1]:
			IDE402_grade =clss[2]
			#print IDE402_grade
			IDE402_term=writeTerm(counter,18)
			#print IDE402_term
		if " MA-134" in clss[1]:
		    	MA134_grade =clss[2]
		    	#print MA134_grade
		    	MA134_term=writeTerm(counter,18)
		    	#print MA134_term
		if " CPE-360" in clss[1]:
		    	CPE360_grade =clss[2]
		    	#print CPE360_grade
		    	CPE360_term=writeTerm(counter,18)
		    	#print CPE360_term
		if " CPE-487" in clss[1]:
		    	CPE487_grade =clss[2]
		    	#print CPE487_grade
		    	CPE487_term=writeTerm(counter,18)
		    	#print CPE487_term
		if " CPE-462" in clss[1]:
		    	CPE462_grade =clss[2]
		    	#print CPE462_grade
		    	CPE462_term=writeTerm(counter,18)
		    	#print CPE462_term
		if " CPE-345" in clss[1]:
		    	CPE345_grade =clss[2]
		    	#print CPE345_grade
		    	CPE345_term=writeTerm(counter,18)
		    	#print CPE345_term
		if " CPE-322" in clss[1]:
		    	CPE322_grade =clss[2]
		    	#print CPE322_grade
		    	CPE322_term=writeTerm(counter,18)
		    	#print CPE322_term
		if " CPE-423" in clss[1]:
		    	CPE423_grade =clss[2]
		    	#print CPE423_grade
		    	CPE423_term=writeTerm(counter,18)
		    	#print CPE423_term
		if " CPE-490" in clss[1]:
		    	CPE490_grade =clss[2]
		    	#print CPE490_grade
		    	CPE490_term=writeTerm(counter,18)
		    	#print CPE490_term
		if " CPE-424" in clss[1]:
		    	CPE424_grade =clss[2]
		    	#print CPE424_grade
		    	CPE424_term=writeTerm(counter,18)
		    	#print CPE424_term

		if clss[0] == "Humanity" and hum1 is False:
			Humanity1 = clss[1]
			Humanity1_grade = clss[2]
			Humanity1_term=writeTerm(counter,18)
			hum1=True
		elif clss[0] == "Humanity" and hum2 is False:
			Humanity2 = clss[1]
			Humanity2_grade = clss[2]
			Humanity2_term=writeTerm(counter,18)
			hum2=True
		elif clss[0] == "Humanity" and hum3 is False:
			Humanity3 = clss[1]
			Humanity3_grade = clss[2]
			Humanity3_term=writeTerm(counter,18)
			hum3=True
		elif clss[0] == "Humanity" and hum4 is False:
			Humanity4 = clss[1]
			Humanity4_grade = clss[2]
			Humanity4_term=writeTerm(counter,18)
			hum4=True

		if clss[0] == "Technical" and tech1 == True:
			Technical1 =clss[1]
			Technical1_grade = clss[2]
			Technical1_term=writeTerm(counter,18)
			tech1=False
		elif clss[0] == "Technical" and tech2 == True:
			Technical2 =clss[1]
			Technical2_grade = clss[2]
			Technical2_term=writeTerm(counter,18)
			tech2 == False
		elif clss[0] == "Technical" and tech3 == True:
			Technical3 =clss[1]
			Technical3_grade = clss[2]
			Technical3_term=writeTerm(counter,18)
			tech3 == False
		elif clss[0] == "Technical" and tech4 == True:
			Technical4 =clss[1]
			Technical4_grade = clss[2]
			Technical4_term=writeTerm(counter,18)
			tech4 == False

		if clss[0] == "General" and gen1 == True:
			General1 = clss[1]
			General1_grade = clss[2]
			General1_term=writeTerm(counter,18)
			gen1 == False
		elif clss[0] == "General" and gen2 == True:
			General2 = clss[1]
			General2_grade = clss[2]
			General2_term=writeTerm(counter,18)
			gen2 == False
		elif clss[0] == "General" and gen3 == True:
			General3 = clss[1]
			General3_grade = clss[2]
			General3_term=writeTerm(counter,18)
			gen3 == False

		if clss[0] == "Science" and sci1 is False:
			Science1 = clss[1]
			Science1_grade = clss[2]
			Science1_term=writeTerm(counter,18)
			sci1 = True	
		elif clss[0] == "Science" and sci2 is False:
			Science2 = clss[1]
			Science2_grade = clss[2]
			Science2_term=writeTerm(counter,18)
			sci2 = True

		if clss[0] == "ScienceLab" and scil1 is False:
			ScienceLab1 = clss[1]
			ScienceLab1_grade = clss[2]
			ScienceLab1_term=writeTerm(counter,18)
			scil1 = True	


		if clss[0] == "Extra" and ext1 == False:
			Extra1 = clss[1]
			Extra1_grade = clss[2]
			Extra1_term=writeTerm(counter,18)
			ext1 = True
		elif clss[0] == "Extra" and ext2 == False:
			Extra2 = clss[1]
			Extra2_grade = clss[2]
			Extra2_term=writeTerm(counter,18)
			ext2 = True

		elif clss[0] == "Extra" and ext3 == False:
			Extra3 = clss[1]
			Extra3_grade = clss[2]
			Extra3_term=writeTerm(counter,18)
			ext3=True
		elif clss[0] == "Extra" and ext4 == False:
			Extra4 = clss[1]
			Extra4_grade = clss[2]
			Extra4_term=writeTerm(counter,18)
			ext4=True
	counter =counter+1


packet = StringIO.StringIO()

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
can.drawString(40,414, EE471_term)
can.drawString(40,402, CPE487_term)
can.drawString(40,390, Humanity3_term)
can.drawString(40,378, E321_term)
can.drawString(40,364, E243_term)
can.drawString(40,352, E344_term)

#term5 grades
can.drawString(295,414, EE471_grade)
can.drawString(295,402, CPE487_grade)
can.drawString(295,390, Humanity3_grade)
can.drawString(295,378, E321_grade)
can.drawString(295,364, E243_grade)
can.drawString(295,352, E344_grade)

#term6
can.drawString(40,332, CPE322_term)
can.drawString(40,320, CPE345_term)
can.drawString(40,308, CPE462_term)
can.drawString(40,296, E355_term)
can.drawString(40,284, Science2_term)
can.drawString(40,272, General1_term)
can.drawString(40,260, IDE400_term)

#term6 grades
can.drawString(295,332, EE322_grade)
can.drawString(295,320, EE345_grade)
can.drawString(295,308, CPE462_grade)
can.drawString(295,296, E355_grade)
can.drawString(295,284, Science2_grade)
can.drawString(295,272, General1_grade)
can.drawString(295,260, IDE400_grade)

#term7
can.drawString(360,414, CPE423_term)
can.drawString(360,402, CPE490_term)
can.drawString(360,390, IDE401_term)
can.drawString(360,378, General2_term)
can.drawString(360,364, Technical1_term)
can.drawString(360,352, Technical2_term)

#term7 grades
can.drawString(620,414, CPE423_grade)
can.drawString(620,402, CPE490_grade)
can.drawString(620,390, IDE401_grade)
can.drawString(620,378, General2_grade)
can.drawString(620,364, Technical1_grade)
can.drawString(620,352, Technical2_grade)

#term8
can.drawString(360,332, EE424_term)
can.drawString(360,320, Technical3_term)
can.drawString(360,308, Technical4_term)
can.drawString(360,296, Humanity4_term)
can.drawString(360,284, General3_term)
can.drawString(360,272, IDE402_term)

#term8 grades
can.drawString(620,332, EE424_grade)
can.drawString(620,320, Technical3_grade)
can.drawString(620,308, Technical4_grade)
can.drawString(620,296, Humanity4_grade)
can.drawString(620,284, General3_grade)
can.drawString(620,272, IDE402_grade)

#classes
can.drawString(125,390, Humanity3)
can.drawString(150,284, Science2)
can.drawString(110,272, General1)
can.drawString(420,378, General2)
can.drawString(475,364, Technical1)
can.drawString(475,352, Technical2)
can.drawString(475,320, Technical3)
can.drawString(475,308, Technical4)
can.drawString(450,296, Humanity4)
can.drawString(420,284, General3)

#extra courses
can.drawString(435,242, Extra1)
can.drawString(435,232, Extra2)
can.drawString(435,222, Extra3)
can.drawString(435,212, Extra4)

#extra courses grades
can.drawString(615,242,Extra1_grade)
can.drawString(615,232,Extra2_grade)
can.drawString(615,222,Extra3_grade)
can.drawString(615,212,Extra4_grade)

#extra course terms
can.drawString(360,242,Extra1_term)
can.drawString(360,232,Extra2_term)
can.drawString(360,222,Extra3_term)
can.drawString(360,212,Extra4_term)


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
