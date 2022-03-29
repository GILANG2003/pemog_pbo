def garis():
    print("====================================")

print(" Program Menginap DI Hotel ")
print(" -------------------------------------------------------------")
print ("| lama inap |   superior    |    deluxe     |    premium    |")
print(" -------------------------------------------------------------")
print ("|  1-2hari  | 100.000/night | 150.000/night | 200.000/night |")
print ("|  3-4hari  | 90.000/night  | 135.000/night | 180.000/night |")
print ("|  >=5hari  | 80.000/night  | 120.000/night | 160.000/night |")
print("--------------------------------------------------------------")

print ("Tipe Kamar")
print ("1. Superior")
print ("2. Deluxe")
print ("3. Premium")


tipe_kamar = input("Masukan tipe kamar : ")
lama_inap  = int(input("Masukan lama inap : "))

if tipe_kamar == "1":
    if lama_inap <= 2:
        total_harga = 100000
    elif lama_inap <= 4 :
        total_harga = 90000
    elif lama_inap >=5 :
        total_harga = 80000*lama_inap
    else:
        total_harga = 100000*lama_inap


elif tipe_kamar == "2":
    if lama_inap <= 2:
        total_harga = 150000
    elif lama_inap <= 4 :
        total_harga = 135000
    elif lama_inap >=5 :
        total_harga = 120000*lama_inap
    else:
        total_harga = 120000*lama_inap


elif tipe_kamar == "3":
    if lama_inap <= 2:
        total_harga = 200000
    elif lama_inap <= 4 :
        total_harga = 180000
    elif lama_inap >=5 :
        total_harga = 160000*lama_inap
    else:
        total_harga = 200000*lama_inap


garis()
print("Kamar yang dipilih  : ",(tipe_kamar))
print("Lama inap           : ", (lama_inap))
print("Total harga         : ",(total_harga))
home=input("Ingin Memesan Lagi (Y/N)? ")
back=print("")
garis()

if home == "Y":
    print ("Tipe Kamar")
    print ("1. Superior")
    print ("2. Deluxe")
    print ("3. Premium")


    tipe_kamar = input("Masukan tipe kamar : ")
    lama_inap  = int(input("Masukan lama inap : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4 :
            total_harga = 90000
        elif lama_inap >=5 :
            total_harga = 80000*lama_inap
        else:
            total_harga = 100000*lama_inap


    elif tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4 :
            total_harga = 135000
        elif lama_inap >=5 :
            total_harga = 120000*lama_inap
        else:
            total_harga = 120000*lama_inap


    elif tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4 :
            total_harga = 180000
        elif lama_inap >=5 :
            total_harga = 160000*lama_inap
        else:
            total_harga = 200000*lama_inap

    garis()
    print("Kamar yang dipilih  : ",(tipe_kamar))
    print("Lama inap           : ", (lama_inap))
    print("Total harga         : ",(total_harga))
    home=input("Ingin Memesan Lagi (Y/N)? ")
    back=print("")
    garis()
else:
    back
    
    if home == "Y":
        print ("Tipe Kamar")
        print ("1. Superior")
        print ("2. Deluxe")
        print ("3. Premium")


        tipe_kamar = input("Masukan tipe kamar : ")
        lama_inap  = int(input("Masukan lama inap : "))

        if tipe_kamar == "1":
            if lama_inap <= 2:
                total_harga = 100000
            elif lama_inap <= 4 :
                total_harga = 90000
            elif lama_inap >=5 :
                total_harga = 80000*lama_inap
            else:
                total_harga = 100000*lama_inap


        elif tipe_kamar == "2":
            if lama_inap <= 2:
                total_harga = 150000
            elif lama_inap <= 4 :
                total_harga = 135000
            elif lama_inap >=5 :
                total_harga = 120000*lama_inap
            else:
                total_harga = 120000*lama_inap


        elif tipe_kamar == "3":
            if lama_inap <= 2:
                total_harga = 200000
            elif lama_inap <= 4 :
                total_harga = 180000
            elif lama_inap >=5 :
                total_harga = 160000*lama_inap
            else:
                total_harga = 200000*lama_inap

        garis()
        print("Kamar yang dipilih  : ",(tipe_kamar))
        print("Lama inap           : ", (lama_inap))
        print("Total harga         : ",(total_harga))
        home=input("Ingin Memesan Lagi (Y/N)? ")
        back=print("")
        garis()
    else:
        back     
     
     
if home == "Y":
    print ("Tipe Kamar")
    print ("1. Superior")
    print ("2. Deluxe")
    print ("3. Premium")


    tipe_kamar = input("Masukan tipe kamar : ")
    lama_inap  = int(input("Masukan lama inap : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4 :
            total_harga = 90000
        elif lama_inap >=5 :
            total_harga = 80000*lama_inap
        else:
            total_harga = 100000*lama_inap


    elif tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4 :
            total_harga = 135000
        elif lama_inap >=5 :
            total_harga = 120000*lama_inap
        else:
            total_harga = 120000*lama_inap


    elif tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4 :
            total_harga = 180000
        elif lama_inap >=5 :
            total_harga = 160000*lama_inap
        else:
            total_harga = 200000*lama_inap

    garis()
    print("Kamar yang dipilih  : ",(tipe_kamar))
    print("Lama inap           : ", (lama_inap))
    print("Total harga         : ",(total_harga))
    home=input("Ingin Memesan Lagi (Y/N)? ")
    back=print("")
    garis()
else:
    back

        
if home == "Y":
    print ("Tipe Kamar")
    print ("1. Superior")
    print ("2. Deluxe")
    print ("3. Premium")


    tipe_kamar = input("Masukan tipe kamar : ")
    lama_inap  = int(input("Masukan lama inap : "))

    if tipe_kamar == "1":
        if lama_inap <= 2:
            total_harga = 100000
        elif lama_inap <= 4 :
            total_harga = 90000
        elif lama_inap >=5 :
            total_harga = 80000*lama_inap
        else:
            total_harga = 100000*lama_inap


    elif tipe_kamar == "2":
        if lama_inap <= 2:
            total_harga = 150000
        elif lama_inap <= 4 :
            total_harga = 135000
        elif lama_inap >=5 :
            total_harga = 120000*lama_inap
        else:
            total_harga = 120000*lama_inap


    elif tipe_kamar == "3":
        if lama_inap <= 2:
            total_harga = 200000
        elif lama_inap <= 4 :
            total_harga = 180000
        elif lama_inap >=5 :
            total_harga = 160000*lama_inap
        else:
            total_harga = 200000*lama_inap

    garis()
    print("Kamar yang dipilih  : ",(tipe_kamar))
    print("Lama inap           : ", (lama_inap))
    print("Total harga         : ",(total_harga))
    home=input("Ingin Memesan Lagi (Y/N)? ")
    back=print("")
    garis()
else:
    back
