fullList = [
            [],
            ['CH 115', 'CH 117', 'E 101', 'E 121', 'E 120', 'E 115', 'MA 121', 'CAL 103'], ['Science:CH-116', 'ScienceLab:CH-118', 'E 122', 'MA 123', 'PEP 111', 'CAL 105', 'MGT 103'],
            ['Humanity:HHS-130', 'MA 221', 'MA 221R', 'PEP 112', 'PEP 112R', 'E 126', 'E 245', 'E 245L', 'E 231'],
            ['Humanity:BT-244', 'MA 134', 'E 232', 'E 232L', 'E 234', 'E 234R', 'CPE 360', 'CPE 390L', 'CPE 390'],
            ['Humanity:BT-243', 'EE 471', 'E 344', 'E 321', 'E 243', 'E 243R', 'CPE 487'],
            ['Science:PEP-151', 'EE 345', 'E 355', 'CPE 322', 'CPE 462', 'IDE 400', 'General:EM-275'],
            ['General:HSS-175', 'Technical:EE-586', 'Technical:CS-570', 'Extra:EXT 001', 'CPE 490', 'CPE 423', 'IDE 401'],
            ['Humanity:HPL-339', 'General:LSP-102', 'Technical:CPE-441', 'Technical:CS-550', 'Extra:EXT 002', 'CPE 424', 'IDE 402']
            ]

Humanity = []
General = []
Technical = []
Science = []
ScienceLab = []

for semesterList in fullList:
	for clss in semesterList:
		if "Humanity" in clss:
			#print clss
			clssSplit = clss.split(":")
			#print clssSplit[1]
			Humanity.append(clssSplit[1])
			#print Humanity
	for clss in semesterList:
		if "General" in clss:
			#print clss
			clssSplit = clss.split(":")
			#print clssSplit[1]
			General.append(clssSplit[1])
			#print General
	for clss in semesterList:
		if "Technical" in clss:
			#print clss
			clssSplit = clss.split(":")
			#print clssSplit[1]
			Technical.append(clssSplit[1])
			#print Technical
	for clss in semesterList:
		if "Science" in clss:
			#print clss
			clssSplit = clss.split(":")
			#print clssSplit[1]
			Science.append(clssSplit[1])
			#print Science[0]
	for clss in semesterList:
		if "ScienceLab" in clss:
			#print clss
			clssSplit = clss.split(":")
			#print clssSplit[1]
			ScienceLab.append(clssSplit[1])
			#print ScienceLab
	for clss in semesterList:
		if "Extra" in clss:
			#print clss
			clssSplit = clss.split(":")
			#print clssSplit[1]
			ScienceLab.append(clssSplit[1])
			#print ScienceLab









