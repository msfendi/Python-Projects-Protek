bindo = int(input('Masukkan nilai Bhs Indonesia :'))
ipa = int(input('Masukkan nilai IPA :'))
mat = int(input('Masukkan nilai Matematika :'))

if( bindo >= 60) and ( ipa >= 60):
    if( mat > 70) :
        print(' ')
        print('Status Kelulusan : LULUS')
    else:
        print(' ')
        print('Status Kelulusan : TIDAK LULUS')
else:
    print(' ')
    print('Status Kelulusan : TIDAK LULUS')