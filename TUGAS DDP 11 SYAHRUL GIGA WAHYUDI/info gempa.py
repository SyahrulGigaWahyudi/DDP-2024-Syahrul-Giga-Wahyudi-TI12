#memanggil file dempa dan import semua
from gempa import*

#membuat objek gempa argumen
gempa1 = gempa("banten",1.2)
#informasi gempa
print("## info gempa maseh ##")
print()
gempa1.dampak()
gempa2= gempa("palu",6.1)

gempa2.dampak()
print()
gempa3= gempa("cianjur,",5.6)

gempa3.dampak()
print()
gempa4= gempa ("jaya pura",3.3)

print()
gempa4.dampak()
print()
gempa5= gempa ("garut",4.0)

print()
gempa5.dampak ()


