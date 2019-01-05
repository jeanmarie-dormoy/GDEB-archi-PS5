import sys

def getInstructions(file) :
	f = open(file, "r")
	lines = f.readlines()
	for i in range(0,len(lines)) :
		lines[i] = lines[i].strip()
	return lines

def translate(lines) :
	f = open("out", "w")
	res = "v2.0 raw\n"
	for line in lines :
		spacesplit = line.split(" ")
		if len(spacesplit) > 2 : 
			for i in range(2,len(spacesplit)) :
				spacesplit[1]+=spacesplit[i].strip() 
		spacesplit[0] = spacesplit[0].upper()
		if spacesplit[0]=='LDR' :
			res += str(getLDR(spacesplit[1])) +"\n"
		if spacesplit[0]=='CMP' : 
			res += str(getCMP(spacesplit[1])) +"\n"
		if spacesplit[0]=='STR' : 
			res += str(getSTR(spacesplit[1])) +"\n"
		if spacesplit[0][0] == 'B' :
			res += conditional(spacesplit,searchStr(lines,spacesplit[1]+':')) + "\n"
		if spacesplit[0]=='SUB' : 
			res += str(getSUB(spacesplit[1])) +"\n"
		if spacesplit[0]=='MOVS' or spacesplit[0]=='MOV':
			res += str(getMOVS(spacesplit[1])) +"\n"	
		if spacesplit[0]=='MUL' or spacesplit[0]=='MULS' :
			res += str(getMUL(spacesplit[1])) +"\n"	
		if spacesplit[0]=='ADDS' :
			res += str(getADDS(spacesplit[1])) +"\n"
		if spacesplit[0]=='ADD' :
			res += str(getADD(spacesplit[1])) +"\n"
		if spacesplit[0]=='LSLS' or spacesplit[0]=='LSL' :
			res += str(getLSLS(spacesplit[1])) +"\n"
		if spacesplit[0]=='LSRS' :
			res += str(getLSLS(spacesplit[1])) +"\n"
		if spacesplit[0]=='ASRS' :
			res += str(getASRS(spacesplit[1])) +"\n"
		if spacesplit[0]=='SUBS' :
			res += str(getSUBS(spacesplit[1])) +"\n"
		if spacesplit[0]=='ANDS' :
			res += str(getANDS(spacesplit[1])) +"\n"
		if spacesplit[0]=='EORS' :
			res += str(getEORS(spacesplit[1])) +"\n"
		if spacesplit[0]=='ADCS' :
			res += str(getADCS(spacesplit[1])) +"\n"
		if spacesplit[0]=='SBCS' :
			res += str(getSBCS(spacesplit[1])) +"\n"
		if spacesplit[0]=='RORS' :
			res += str(getRORS(spacesplit[1])) +"\n"
		if spacesplit[0]=='RSBS' :
			res += str(getRSBS(spacesplit[1])) +"\n"
		if spacesplit[0]=='CMN' :
			res += str(getCMN(spacesplit[1])) +"\n"
		if spacesplit[0]=='ORRS' :
			res += str(getORRS(spacesplit[1])) +"\n"
		if spacesplit[0]=='BICS' :
			res += str(getBICS(spacesplit[1])) +"\n"
		if spacesplit[0]=='MVNS' :
			res += str(getMVNS(spacesplit[1])) +"\n"
	f.write(res)


def reformat(val,length):
	if (int(val)<0) :
		temp = -int(val)
		temp = bin(temp)[2:]
		new=''
		for i in range(0,len(temp)) :
			if temp[i] =='0':
				new+='1'
			if temp[i] =='1':
				new+='0'
		leng = len(new)
		new = int(new,2)+1
		new = bin(new)[2:]
		for i in range (0,leng-len(new)) :
			new = '0'+new
		nbzero = length - len(new)
		for i in range(0,nbzero) : 
			new = '1'+new
		return new
	else :
		val = bin(int(val))[2:]
		nbzero = length - len(val)
		for i in range(0,nbzero) : 
			val = "0"+val
		return val

def getANDS(values) :
	values= values.split(',')
	rdn = reformat(values[0][1],3)
	rm = reformat(values[1][1],3)
	res = "0100000000" + rm + rdn
	return hex(int(res, 2))[2:]

def getADCS(values) :
	values= values.split(',')
	rdn = reformat(values[0][1],3)
	rm = reformat(values[1][1],3)
	res = "0100000101" + rm + rdn
	return hex(int(res, 2))[2:]

def getSBCS(values) :
	values= values.split(',')
	rdn = reformat(values[0][1],3)
	rm = reformat(values[1][1],3)
	res = "0100000110" + rm + rdn
	return hex(int(res, 2))[2:]

def getTST(values) :
	values= values.split(',')
	rn = reformat(values[0][1],3)
	rm = reformat(values[1][1],3)
	res = "0100001000" + rm + rn
	return hex(int(res, 2))[2:]

def getRSBS(values) :
	values= values.split(',')
	rd = reformat(values[0][1],3)
	rn = reformat(values[1][1],3)
	res = "0100001001" + rn + rd
	return hex(int(res, 2))[2:]

def getRORS(values) :
	values= values.split(',')
	rdn = reformat(values[0][1],3)
	rm = reformat(values[1][1],3)
	res = "0100000111" + rm + rdn
	return hex(int(res, 2))[2:]


def getEORS(values) :
	values= values.split(',')
	rdn = reformat(values[0][1],3)
	rm = reformat(values[1][1],3)
	res = "0100000001" + rm + rdn
	return hex(int(res, 2))[2:]

def getLSLS(values) :
	if (values.find('#')!=-1) :
		imm = values.split('#')[1]
		imm = reformat(imm,5)
		rd = reformat(values[0][len(values[0])-1],3)
		rm = reformat(values[1][len(values[1])-1],3)
		res = '00000'+imm+rm+rd
		return hex(int(res, 2))[2:]
	else :
		values= values.split(',')
		rd = reformat(values[0][1],3)
		rm = reformat(values[1][1],3)
		res = '0100000010'+rm+rd
		return hex(int(res, 2))[2:]

def getASRS(values) :
	if (values.find('#')!=-1) :
		imm = values.split('#')[1]
		imm = reformat(imm,5)
		rd = reformat(values[0][len(values[0])-1],3)
		rm = reformat(values[1][len(values[1])-1],3)
		res = '00010'+imm+rm+rd
		return hex(int(res, 2))[2:]
	else :
		values= values.split(',')
		rd = reformat(values[0][1],3)
		rm = reformat(values[1][1],3)
		res = '0100000100'+rm+rd
		return hex(int(res, 2))[2:]

def getLSRS(values) :
	if (values.find('#')!=-1):
		imm = values.split('#')[1]
		imm = reformat(imm,5)
		rd = reformat(values[0][len(values[0])-1],3)
		rm = reformat(values[1][len(values[1])-1],3)
		res = '00001'+imm+rm+rd
		return hex(int(res, 2))[2:]
	else :
		values= values.split(',')
		rd = reformat(values[0][1],3)
		rm = reformat(values[1][1],3)
		res = '0100000011'+rm+rd
		return hex(int(res, 2))[2:]

def getLDR(values) :
	values = values.replace('[','')
	values = values.replace(']','')
	imm = reformat(values.split('#')[1],8)
	values = values.split(',')
	rt = reformat(values[0][len(values[0])-1],3)
	res = "10011" + rt + imm
	return hex(int(res, 2))[2:]

def getADDS(values) :
	values = values.replace('[','')
	values = values.replace(']','')
	if (values.find('#') != -1):
		imm = values.split('#')[1]
		imm = reformat(imm,3)
		values = values.split(',')
		rd = reformat(values[0][1],3)
		rn = reformat(values[1][1],3)
		res = "0001110" + imm + rn + rd
		return hex(int(res, 2))[2:]
	else :
		values = values.split(',')
		rd = reformat(values[0][1][2:],3)
		rn = reformat(values[1][1][2:],3)
		rm = reformat(values[2][1][2:],3)
		res = "0001100" + rm + rn + rd
		return hex(int(res, 2))[2:]

def getSUBS(values) :
	values = values.replace('[','')
	values = values.replace(']','')
	if (values.find('#') != -1):
		imm = reformat(values.split('#')[1],3)
		values = values.split(',')
		rd = reformat(values[0][1],3)
		rn = reformat(values[1][1],3)
		res = "0001111" + imm + rn + rd
		return hex(int(res, 2))[2:]
	else :
		values = values.split(',')
		rd = reformat(values[0][1][2:],3)
		rn = reformat(values[1][1][2:],3)
		rm = reformat(values[2][1][2:],3)
		res = "0001101" + rm + rn + rd
		return hex(int(res, 2))[2:]

def getADD(values) :
	imm = reformat(values.split('#')[1],7)
	res = "101100000"+imm
	return hex(int(res, 2))[2:]

def getMUL(values) : 
	values = values.split(',')
	rdm = reformat(values[0][len(values[0])-1],3)
	rn = reformat(values[1][len(values[0])-1],3)
	res = '0100001101'+rn+rdm
	return hex(int(res, 2))[2:]

def getMOVS(values) :
	if values.find('#')!=-1 :
		imm = values.split('#')[1]
		values = values.split(',')
		imm = reformat(imm,8)
		part2 = reformat(values[0][len(values[0])-1],3)
		res = "00100" +part2+ imm
		return hex(int(res, 2))[2:]
	return '0000'

def getSTR(values) :
	values = values.replace('[','')
	values = values.replace(']','')
	imm = values.split('#')[1]
	imm = reformat(imm,8)
	values = values.split(',')
	part2 = reformat(values[0][len(values[0])-1],3)
	res = "10010" + part2 + imm
	return hex(int(res, 2))[2:]


def getCMN(values) : 
	values = values.split(",")
	rm = reformat(values[1][1],3)
	rn = reformat(values[0][1],3)
	res = "0100001011"+rm+rn
	return hex(int(res, 2))[2:]

def getORRS(values) : 
	values = values.split(",")
	rm = reformat(values[1][1],3)
	rdn = reforat(values[0][1],3)
	res = "0100001100"+rm+rdn
	return hex(int(res, 2))[2:]

def getBICS(values) : 
	values = values.split(",")
	rm = reformat(values[1][1],3)
	rdn = reformat(values[0][1],3)
	res = "0100001110"+rm+rdn
	return hex(int(res, 2))[2:]

def getMVNS(values) : 
	values = values.split(",")
	rm = reformat(values[1][1],3)
	rd = reformat(values[0][1],3)
	res = "0100001111"+rm+rd
	return hex(int(res, 2))[2:]

def getCMP(values) : 
	values = values.split(",")
	rm = reformat(values[1][1],3)
	rn = reformat(values[0][1],3)
	res = "0100001010"+rm+rn
	return hex(int(res, 2))[2:]

def searchStr(lines,strn) :
	i=0
	d = 0
	while i<len(lines) :
		if (lines[i][0]=='@') :
			d+= 1
		if lines[i][len(lines[i])-1] == ':' :
			d += 1
		if lines[i] == strn:
			return i - d + 1

		i+=1
	return 0;

def getSUB(line):
	line = line.split('#')
	a = reformat(line[1],7)
	a = '101100001' + a
	return hex(int(a, 2))[2:]

def conditional(lineArray,position) :
	res =""
	r = ""
	cond = lineArray[0][1:]
	imm = bin(position)
	imm = imm[2:]
	nbzero = 8 - len(imm)
	for i in range(0,nbzero) : 
		imm = "0"+imm
	conds = {'EQ' : '0000','NE' : '0001','CS' : '0010','CC' : '0011','MI' : '0100','PL' : '0101','VS' : '0110','VC' : '0111','HI' : '1000','LS' : '1001','GE' : '1010','LT' : '1011','GT' : '1100','LE' : '1101','AL' : '1110','' : '1110'}
	r=conds[cond]
	res = "1101"+r+imm
	return hex(int(res,2))[2:]

if __name__ == '__main__':
	if (len(sys.argv) != 2) : 
		print("N'oubliez pas d'ajouter en argument le fichier d'entree")
		exit(1)
	else :
		translate(getInstructions(sys.argv[1]))
		print("Ecriture reussie dans le fichier \'out\'")