def garis():
    print("=================================")

def sort_asc(array):
    array = sorted(array)
    return (array)

def sort_desc(array):
    array = sorted(array, reverse = True)
    return(array)

def rata_rata(angka):
    return sum(angka)/len(angka)

garis()
print("Masukan Tiga Buah Nilai")
nilaiA = int(input("Nilai A : "))
nilaiB = int(input("Nilai B : "))
nilaiC = int(input("Nilai C : "))
angka = (nilaiA,nilaiB,nilaiC)
print()

print("Urutan Nilai Ascending : "
      ,(sort_asc(angka)))
print("Urutan Nilai Descending : "
      ,(sort_desc(angka)))


print("Nilai MAX : ", max(angka))
print("Nilai MIN : ", min(angka))
print("Nilai RATA RATA : ", round(rata_rata(angka)))
garis()
