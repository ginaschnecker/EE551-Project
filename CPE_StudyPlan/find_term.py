NewList=[' ------------------2011 Summer Session 1--------------------\n', 'Class: PEP-111-WS Grade: A', ' ------------------------2011 Fall--------------------------\n', 'Class: CAL-103-M Grade: C+', 'Class: CH-115-RP Grade: C+', 'Class: CH-117-E Grade: A', 'Class: E-101-A Grade: P', 'Class: E-115-LB Grade: A', 'Class: E-120-N Grade: A-', 'Class: E-121-Q Grade: A', 'Class: MA-121-C Grade: A', 'Class: MA-122-CC Grade: A', ' -----------------------2012 Spring-------------------------\n', 'Class: CAL-105-I Grade: A-', 'Class: CH-116-RA Grade: C-', 'Class: CH-118-A Grade: B+', 'Class: E-102-A Grade: P', 'Class: E-122-C Grade: A-', 'Class: MA-123-F Grade: B+', 'Class: MA-124-FF Grade: B+', 'Class: PE-200-V2 Grade: P','Class: MGT-103 Grade: A', ' ------------------------2012 Fall--------------------------\n', 'Class: E-126-B Grade: C+', 'Class: E-231-A Grade: B+', 'Class: E-245-B Grade: B+', 'Class: HHS-130-A Grade: B+', 'Class: MA-221-A Grade: ', 'Class: PE-200-V2 Grade: P', 'Class: PEP-112-RA Grade: A-', ' -----------------------2013 Spring-------------------------\n', 'Class: CPE-360-A Grade: A-', 'Class: CPE-390-A Grade: B-', 'Class: E-232-B Grade: A-', 'Class: E-234-RD Grade: C', 'Class: MA-134-A Grade: C', 'Class: MA-221-A Grade: C', 'Class: PE-200-V2 Grade: P', ' ------------------------2013 Fall--------------------------\n', 'Class: BT-244-D Grade: A', 'Class: CPE-487-A Grade: A', 'Class: E-243-A Grade: A', 'Class: E-321-B Grade: A', 'Class: E-344-A Grade: A-', 'Class: EE-471-A Grade: A', ' -----------------------2014 Spring-------------------------\n', 'Class: BT-243-C Grade: A', 'Class: CPE-322-A Grade: A', 'Class: CPE-345-A Grade: A', 'Class: CPE-462-EV Grade: A', 'Class: E-355-B Grade: A-', 'Class: HPL-339-EV Grade: B-', 'Class: PE-200-V2 Grade: P', ' ------------------2014 Summer Session 1--------------------\n', 'Class: E-234-A Grade: B+', ' ------------------------2014 Fall--------------------------\n', 'Class: CPE-423-A Grade: A', 'Class: CPE-490-A Grade: B+', 'Class: CS-550-WS Grade: B', 'Class: CS-570-C Grade: A', 'Class: EE-586-WS Grade: B', 'Class: PE-200-B2 Grade: P', 'Class: PEP-151-A Grade: A', 'Class: TG-403-H Grade: A', ' -----------------------2015 Spring-------------------------\n', 'Class: CPE-424-A Grade: A', 'Class: CPE-441-A Grade: A', 'Class: EM-275-A Grade: A', 'Class: HSS-175-B Grade: B', 'Class: LSP-102-A Grade: B+', 'Class: PE-200-V2 Grade: P', 'Class: TG-404-H Grade: A']#,'Number of terms taken: 11'] #idk 

terms=[]
for term in NewList:

	if "---" in term:
		aTerm=term.split()
		#if len(term)>1:
		terms.append(aTerm[1][0]+aTerm[0][-2]+aTerm[0][-1])
	