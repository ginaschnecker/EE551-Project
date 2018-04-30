NewList=[' ------------------------2013 Fall--------------------------\n', 'Class: CAL-103-L Grade: B', 'Class: CH-115-RC Grade: B', 'Class: CH-117-A Grade: A', 'Class: E-101-A Grade: P', 'Class: E-115-LC Grade: A', 'Class: E-120-C Grade: A', 'Class: E-121-H Grade: A-', 'Class: MA-121-C Grade: A', 'Class: MA-122-CC Grade: A', 'Class: PE-200-X9 Grade: ', ' -----------------------2014 Spring-------------------------\n', 'Class: CAL-105-N Grade: B+', 'Class: CH-116-RB Grade: D+', 'Class: CH-118-E Grade: A-', 'Class: E-122-B Grade: B+', 'Class: MA-123-F Grade: B+', 'Class: MA-124-FF Grade: B+', 'Class: MGT-103-I Grade: A', 'Class: PE-200-X9 Grade: P', 'Class: PEP-111-RC Grade: A-', ' -----------------------2015 Spring-------------------------\n', 'Class: BT-243-B Grade: B', 'Class: E-126-B Grade: B+', 'Class: E-231-B Grade: A-', 'Class: E-245-A Grade: A-', 'Class: MA-221-E Grade: B', 'Class: PE-200-X9 Grade: P', 'Class: PEP-112-RB Grade: B', 'Class: HHS-370-EV Grade: A', 'Number of terms taken: 4', '-----------------------2016 Spring-------------------------\n','-----------------------2017 Spring-------------------------\n','-----------------------2018 Spring-------------------------\n','-----------------------2019 Spring-------------------------\n','-----------------------2002 Spring-------------------------\n',
'-----------------------2015 Spring-------------------------\n']

terms=[]
for term in NewList:

	if "---" in term:
		aTerm=term.split()
		#if len(term)>1:
		terms.append(aTerm[1][0]+aTerm[0][-2]+aTerm[0][-1])
print terms
