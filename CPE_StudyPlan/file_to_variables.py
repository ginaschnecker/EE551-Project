#writing classes, grades, and terms into variables
from input_to_variables import *
parseData= open("data.txt","r")

for line in parseData:

	#if "Fall" or "Spring" in line:
	#	column=line.split()
	#	if len(column)>1:
	#		term1=column[1][0]+column[0][-2]+column[0][-1]
	
	#Term I
	if "CAL-105" in line:
		column= line.split()
		if len(column)> 3:
			CAL105_grade= column[3]
	if "CH-115" in line:
		column=line.split()
		if len(column)>3:
			CH115_grade= column[3]
	if "CH-117" in line:
		column=line.split()
		if len(column)>3:
			CH117_grade= column[3]
	if "E-101" in line:
		column=line.split()
		if len(column)>3:
			E101_grade= column[3]
	if "E-115" in line:
		column=line.split()
		if len(column)>3:
			E115_grade= column[3]
	if "E-120" in line:
		column=line.split()
		if len(column)>3:
			E120_grade= column[3]
	if "E-121" in line:
		column=line.split()
		if len(column)>3:
			E121_grade= column[3]
	if "MA-121" in line:
		column=line.split()
		if len(column)>3:
			MA121_grade= column[3]
	if "MA-122" in line:
		column=line.split()
		if len(column)>3:
			MA122_grade= column[3]
	#Term II
	if "CAL-103" in line:
		column=line.split()
		if len(column)>3:
			CAL103_grade= column[3]
	if "E-122" in line:
		column=line.split()
		if len(column)>3:
			E122_grade= column[3]
	if "MA-123" in line:
		column=line.split()
		if len(column)>3:
			MA123_grade= column[3]
	if "MA-124" in line:
		column=line.split()
		if len(column)>3:
			MA124_grade= column[3]
	if "CH-116" in line:
		column=line.split()
		if len(column)>3:
			CH116_grade= column[3]
	if "CH-118" in line:
		column=line.split()
		if len(column)>3:
			CH116_grade= column[3]
	if "MGT-103" in line:
		column=line.split()
		if len(column)>3:
			MGT103_grade= column[3]
	if "PEP-111" in line:
		column=line.split()
		if len(column)>3:
			PEP111_grade= column[3]

	#Term III
	if "E-126" in line:
		column=line.split()
		if len(column)>3:
			E126_grade= column[3]
	if "E-231" in line:
		column=line.split()
		if len(column)>3:
			E231_grade= column[3]
	if "E-245" in line:
		column=line.split()
		if len(column)>3:
			E245_grade= column[3]
	if "MA-221" in line:
		column=line.split()
		if len(column)>3:
			MA221_grade= column[3]
	if "PEP-112" in line:
		column=line.split()
		if len(column)>3:
			PEP112_grade= column[3]
	#humanities 1

	#term IV
	if "EE-250" in line:
		column=line.split()
		if len(column)>3:
			EE250_grade= column[3]
	if "EE-359" in line:
		column=line.split()
		if len(column)>3:
			EE359_grade= column[3]
	if "E-232" in line:
		column=line.split()
		if len(column)>3:
			E232_grade= column[3]
	if "E-234" in line:
		column=line.split()
		if len(column)>3:
			E234_grade= column[3]
	if "CPE-390" in line:
		column=line.split()
		if len(column)>3:
			CPE390_grade= column[3]
	if "CPE-360" in line:
		column=line.split()
		if len(column)>3:
			CPE360_grade= column[3]
	if "MA-134" in line:
		column=line.split()
		if len(column)>3:
			MA134_grade= column[3]
	#humanities 2

	#term V
	if "EE-471" in line:
		column=line.split()
		if len(column)>3:
			EE471_grade= column[3]
	if "EE-348" in line:
		column=line.split()
		if len(column)>3:
			EE348_grade= column[3]
	#humanities 3

	if "E-321" in line:
		column=line.split()
		if len(column)>3:
			E321_grade= column[3]
	if "E-243" in line:
		column=line.split()
		if len(column)>3:
			E243_grade= column[3]
	if "E-344" in line:
		column=line.split()
		if len(column)>3:
			E344_grade= column[3]
	if "CPE-487" in line:
		column=line.split()
		if len(column)>3:
			CPE487_grade= column[3]
	#term VI

	if "EE-322" or "CPE-322" in line:
		column=line.split()
		if len(column)>3:
			EE322_grade= column[3]
	if "EE-345" or "CPE-345" in line:
		column=line.split()
		if len(column)>3:
			EE345_grade= column[3]
	if "EE-448" in line:
		column=line.split()
		if len(column)>3:
			EE448_grade= column[3]
	if "E-355" in line:
		column=line.split()
		if len(column)>3:
			E355_grade= column[3]
	if "CPE-390" in line:
		column=line.split()
		if len(column)>3:
			CPE390_grade= column[3]
	if "CPE-462" in line:
		column=line.split()
		if len(column)>3:
			CPE462_grade= column[3]
	#science elective
	#general elective 2
	if "IDE-400" in line:
		column=line.split()
		if len(column)>3:
			IDE400_grade= column[3]


	#term VII
	if "EE-423" or "CPE-423"in line:
		column=line.split()
		if len(column)>3:
			EE423_grade= column[3]
	if "EE-465" in line:
		column=line.split()
		if len(column)>3:
			EE465_grade= column[3]
	if "IDE-401" or "TG-403" in line:
		column=line.split()
		if len(column)>3:
			IDE401_grade= column[3]
	if "CPE-490" in line:
		column=line.split()
		if len(column)>3:
			CPE490_grade= column[3]
	#general elective 2
	#technical elective 1
	#technical elective 2

	#term VIII
	if "EE-424" or "CPE-424"in line:
		column=line.split()
		if len(column)>3:
			EE424_grade= column[3]
	if "IDE-402" or "TG-404" in line:
		column=line.split()
		if len(column)>3:
			IDE402_grade= column[3]

	#humanities
	if Humanity[0] in line:
		column=line.split()
		if len(column)>3:
			humanity0_grade= column[3]
	if Humanity[1] in line:
		column=line.split()
		if len(column)>3:
			humanity1_grade= column[3]
	if Humanity[2] in line:
		column=line.split()
		if len(column)>3:
			humanity2_grade= column[3]
	if Humanity[3] in line:
		column=line.split()
		if len(column)>3:
			humanity3_grade= column[3]

	
	#General
	if General[0] in line:
		column=line.split()
		if len(column)>3:
			general0_grade= column[3]
	if General[1] in line:
		column=line.split()
		if len(column)>3:
			general1_grade= column[3]
	if General[2] in line:
		column=line.split()
		if len(column)>3:
			general2_grade= column[3]
	#Science
	if Science[0] in line:
		column=line.split()
		if len(column)>3:
			science0_grade= column[3]
	if Science[1] in line:
		column=line.split()
		if len(column)>3:
			science1_grade= column[3]
	#Science Lab
	if ScienceLab[0] in line:
		column=line.split()
		if len(column)>3:
			sciencelab0_grade= column[3]
	#Technical
	if Technical[0] in line:
		column=line.split()
		if len(column)>3:
			technical0_grade= column[3]
	if Technical[1] in line:
		column=line.split()
		if len(column)>3:
			technical1_grade= column[3]
	if Technical[2] in line:
		column=line.split()
		if len(column)>3:
			technical2_grade= column[3]
	if Technical[3] in line:
		column=line.split()
		if len(column)>3:
			technical3_grade= column[3]
# finding the year


parseData.close()













