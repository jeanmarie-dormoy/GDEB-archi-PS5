.text

_start:
.global	_start

.data
	A:.word Ox19
	B:.word 0x4
	RES:.word 0x0


main:
	LDR R0,A
	LDR R1,B
	MULS R0, R1, R0
	STR R0, RES

