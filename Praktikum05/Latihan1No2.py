bindo = int(input('Masukkan nilai Bhs Indonesia :'))
ipa = int(input('Masukkan nilai IPA :'))
mat = int(input('Masukkan nilai Matematika :'))

if( bindo > 100) or ( bindo < 0) or ( ipa > 100) or ( ipa < 0) or ( mat > 100) or ( mat < 0):
    print('Maaf input ada yang tidak valid')
elif( bindo >= 60) and ( ipa >= 60):
    if( mat > 70) :
        print('Status Kelulusan : LULUS')
    else:
        print('Status Kelulusan : TIDAK LULUS')
else:
    print('Status Kelulusan : TIDAK LULUS')