#GDEB-archi-PS5

Team GDEB PS5-ARCHITECTURE

Team Members: Pierre Gatto, Nassim El-Gazzah, Hugo Bricard, Jean-Marie Dormoy

Nous avons modifié une partie du ShiftAddSubMov:

Lorsqu'on fait MOVS R0, #255 (0xff)
Le module SASMov reconnaît 0xff et va compléter par des 1 pour remplir le 
registre R0.
On va se retrouver avec 0xffffffff sur 32 bits.

C'est pour cela que dans store_code.txt, on calcule le max entre 0xf et Oxfe
car si on calcule max entre 0xf et 0xff, il sera étendu à 0xffffffff à cause 
du MOVS (on n'initialise pas la mémoire manuellement mais indirectement avec
MOVS, LDR, STR dans le programme entré dans la ROM). 
Et le maximum entre 0xf et 0xffffffff est 0xf, avec la représentation en
complément à 2.

Nous avons des cas de test assez intéréssants dans le dossier tests.
