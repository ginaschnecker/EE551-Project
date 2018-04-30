from input_to_variables import *

NewList=[' ------------------2011 Summer Session 1--------------------\n', 'Class: PEP-111-WS Grade: A', ' ------------------------2011 Fall--------------------------\n', 'Class: CAL-103-M Grade: C+', 'Class: CH-115-RP Grade: C+', 'Class: CH-117-E Grade: A', 'Class: E-101-A Grade: P', 'Class: E-115-LB Grade: A', 'Class: E-120-N Grade: A-', 'Class: E-121-Q Grade: A', 'Class: MA-121-C Grade: A', 'Class: MA-122-CC Grade: A', ' -----------------------2012 Spring-------------------------\n', 'Class: CAL-105-I Grade: A-', 'Class: CH-116-RA Grade: C-', 'Class: CH-118-A Grade: B+', 'Class: E-102-A Grade: P', 'Class: E-122-C Grade: A-', 'Class: MA-123-F Grade: B+', 'Class: MA-124-FF Grade: B+', 'Class: PE-200-V2 Grade: P','Class: MGT-103 Grade: A', ' ------------------------2012 Fall--------------------------\n', 'Class: E-126-B Grade: C+', 'Class: E-231-A Grade: B+', 'Class: E-245-B Grade: B+', 'Class: HHS-130-A Grade: B+', 'Class: MA-221-A Grade: ', 'Class: PE-200-V2 Grade: P', 'Class: PEP-112-RA Grade: A-', ' -----------------------2013 Spring-------------------------\n', 'Class: CPE-360-A Grade: A-', 'Class: CPE-390-A Grade: B-', 'Class: E-232-B Grade: A-', 'Class: E-234-RD Grade: C', 'Class: MA-134-A Grade: C', 'Class: MA-221-A Grade: C', 'Class: PE-200-V2 Grade: P', ' ------------------------2013 Fall--------------------------\n', 'Class: BT-244-D Grade: A', 'Class: CPE-487-A Grade: A', 'Class: E-243-A Grade: A', 'Class: E-321-B Grade: A', 'Class: E-344-A Grade: A-', 'Class: EE-471-A Grade: A', ' -----------------------2014 Spring-------------------------\n', 'Class: BT-243-C Grade: A', 'Class: CPE-322-A Grade: A', 'Class: CPE-345-A Grade: A', 'Class: CPE-462-EV Grade: A', 'Class: E-355-B Grade: A-', 'Class: HPL-339-EV Grade: B-', 'Class: PE-200-V2 Grade: P', ' ------------------2014 Summer Session 1--------------------\n', 'Class: E-234-A Grade: B+', ' ------------------------2014 Fall--------------------------\n', 'Class: CPE-423-A Grade: A', 'Class: CPE-490-A Grade: B+', 'Class: CS-550-WS Grade: B', 'Class: CS-570-C Grade: A', 'Class: EE-586-WS Grade: B', 'Class: PE-200-B2 Grade: P', 'Class: PEP-151-A Grade: A', 'Class: TG-403-H Grade: A', ' -----------------------2015 Spring-------------------------\n', 'Class: CPE-424-A Grade: A', 'Class: CPE-441-A Grade: A', 'Class: EM-275-A Grade: A', 'Class: HSS-175-B Grade: B', 'Class: LSP-102-A Grade: B+', 'Class: PE-200-V2 Grade: P', 'Class: TG-404-H Grade: A']#,'Number of terms taken: 11'] #idk 

for semester in NewList:
	if "CAL-105" in semester:
		aClass= semester.split()
		if len(aClass)> 3:
			CAL105_grade= aClass[3]
		else:
			CAL105_grade = " "
	if "CH-115" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CH115_grade= aClass[3]
		else:
			CH115_grade = " "
	if "CH-117" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CH117_grade= aClass[3]
		else:
			CH117_grade = " "
	if "E-101" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E101_grade= aClass[3]
		else:
			E101_grade = " "
	if "E-115" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E115_grade= aClass[3]
		else:
			E115_grade = " "	
	if "E-120" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E120_grade= aClass[3]
		else:
			CAL105_grade = " "
	if "E-121" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E121_grade= aClass[3]
		else:
			E121_grade = " "
	if "MA-121" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MA121_grade= aClass[3]
		else:
			MA121_grade = " "
	if "MA-122" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MA122_grade= aClass[3]
		else:
			MA122_grade = " "
	#Term II
	if "CAL-103" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CAL103_grade= aClass[3]
		else:
			CAL103_grade = " "
	if "E-122" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E122_grade= aClass[3]
		else:
			E122_grade = " "
	if "MA-123" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MA123_grade= aClass[3]
		else:
			MA123_grade = " "
	if "MA-124" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MA124_grade= aClass[3]
		else:
			MA124_grade = " "
	if "MGT-103" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MGT103_grade= aClass[3]
		else:
			MGT1O3_grade = " "
	if "PEP-111" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			PEP111_grade= aClass[3]
		else:
			PEP111_grade = " "

	#Term III
	if "E-126" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E126_grade= aClass[3]
		else:
			E126_grade = " "
	if "E-231" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E231_grade= aClass[3]
		else:
			E231_grade = " "
	if "E-245" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E245_grade= aClass[3]
		else:
			E245_grade = " "
	if "MA-221" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MA221_grade= aClass[3]
		else:
			MA221_grade = " "
	if "PEP-112" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			PEP112_grade= aClass[3]
		else:
			PEP112_grade = " "
	#humanities 1

	#term IV
	if "EE-250" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE250_grade= aClass[3]
		else:
			EE250_grade = " "
	if "EE-359" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE359_grade= aClass[3]
		else:
			EE359_grade = " "
	if "E-232" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E232_grade= aClass[3]
		else:
			E232_grade = " "
	if "E-234" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E234_grade= aClass[3]
		else:
			E234_grade = " "
	if "CPE-390" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CPE390_grade= aClass[3]
		else:
			CPE390_grade = " "
	if "CPE-360" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CPE360_grade= aClass[3]
		else:
			CPE360_grade = " "
	if "MA-134" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			MA134_grade= aClass[3]
		else:
			MA134_grade = " "
	#humanities 2

	#term V
	if "EE-471" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE471_grade= aClass[3]
		else:
			EE471_grade = " "
	if "EE-348" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE348_grade= aClass[3]
		else:
			EE348_grade = " "
	#humanities 3

	if "E-321" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E321_grade= aClass[3]
		else:
			E231_grade = " "
	if "E-243" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E243_grade= aClass[3]
		else:
			E243_grade = " "
	if "E-344" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E344_grade= aClass[3]
		else:
			E344_grade = " "
	if "CPE-487" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CPE487_grade= aClass[3]
		else:
			CPE487_grade = " "
	#term VI

	if "EE-322" or "CPE-322" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE322_grade= aClass[3]
		else:
			EE322_grade = " "
	if "EE-345" or "CPE-345" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE345_grade= aClass[3]
		else:
			EE345_grade = " "
	if "EE-448" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE448_grade= aClass[3]
		else:
			EE448_grade = " "
	if "E-355" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			E355_grade= aClass[3]
		else:
			E355_grade = " "
	if "CPE-390" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CPE390_grade= aClass[3]
		else:
			CPE390_grade = " "
	if "CPE-462" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CPE462_grade= aClass[3]
		else:
			CPE462_grade = " "
	#science elective
	#general elective 2
	if "IDE-400" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			IDE400_grade= aClass[3]
		else:
			IDE400_grade = " "


	#term VII
	if "EE-423" or "CPE-423"in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE423_grade= aClass[3]
		else:
			EE423_grade = " "
	if "EE-465" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE465_grade= aClass[3]
		else:
			EE465_grade = " "
	if "IDE-401" or "TG-403" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			IDE401_grade= aClass[3]
		else:
			IDE401_grade = " "
	if "CPE-490" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			CPE490_grade= aClass[3]
		else:
			CPE490_grade = " "
	#general elective 2
	#technical elective 1
	#technical elective 2

	#term VIII
	if "EE-424" or "CPE-424"in semester:
		aClass=semester.split()
		if len(aClass)>3:
			EE424_grade= aClass[3]
		else:
			EE424_grade = " "
	if "IDE-402" or "TG-404" in semester:
		aClass=semester.split()
		if len(aClass)>3:
			IDE402_grade= aClass[3]
		else:
			IDE_grade = " "

	#other courses
	#humanities
	if Humanity[0] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			humanity0_grade= aClass[3]
	if Humanity[1] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			humanity1_grade= aClass[3]
	if Humanity[2] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			humanity2_grade= aClass[3]
	if Humanity[3] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			humanity3_grade= aClass[3]

	
	#General
	if General[0] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			general0_grade= aClass[3]
	if General[1] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			general1_grade= aClass[3]
	if General[2] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			general2_grade= aClass[3]
	#Science
	if Science[0] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			science0_grade= aClass[3]
	if Science[1] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			science1_grade= aClass[3]
	#Science Lab
	if ScienceLab[0] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			sciencelab0_grade= aClass[3]
	#Technical
	if Technical[0] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			technical0_grade= aClass[3]
	if Technical[1] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			technical1_grade= aClass[3]
	if Technical[2] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			technical2_grade= aClass[3]
	if Technical[3] in semester:
		aClass=semester.split()
		if len(aClass)>3:
			technical3_grade= aClass[3]

