nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]


print(60 * '=')
print("NIM".ljust(13), "NAMA".ljust(14), "N.MID".rjust(2), "N.UAS".rjust(10))
print(60 * '-')

for i in nilai:
    print(i['nim'].ljust(13), i['nama'].ljust(14), str(i['mid']).rjust(5), str(i['uas']).rjust(10))

print(61 * '-')