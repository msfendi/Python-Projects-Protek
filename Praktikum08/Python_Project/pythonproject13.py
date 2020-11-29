def nilaiTertinggi(nilaiMhs):
    nilaiAkhir = []

    for i in nilaiMhs:
        nilai = (i['mid'] + (i['uas'] * 2)) / 3
        nilaiAkhir.append(nilai)
    hasil = nilaiAkhir.index(max(nilaiAkhir))

    nimTinggi = nilaiMhs[hasil]['nim']
    namaTinggi = nilaiMhs[hasil]['nama']

    print("Mahasiswa dengan nilai tertinggi adalah", namaTinggi, "dengan NIM", nimTinggi)


nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
            
nilaiTertinggi(nilaiMhs)