import random
sayi=0

while sayi%10 == sayi //10:
    sayi = random.randrange(10,99)

tahmin=0

while tahmin != sayi :
    tahminStr = input("lütfen bir sayi tahmini giriniz: ")
    tahmin = int(tahminStr)
    if tahmin >=10 and tahmin <=98 and tahminStr[0]!=tahminStr[1]:
    

        sayiStr = str(sayi)
        dogruYer =0
        yanlisYer =0

        if tahminStr[0] == sayiStr[0]:
            dogruYer +=1

        if tahminStr[1] == sayiStr[1]:
            dogruYer +=1
    
        if tahminStr[0] == sayiStr[1]:
            yanlisYer +=1

        if tahminStr[1] == sayiStr[0]:
            yanlisYer +=1

        if dogruYer==0 and yanlisYer==0:
            print("skor= 0")

        if dogruYer==0 and yanlisYer!=0:
            print("yanlisYer "+ str(yanlisYer))

        if dogruYer!=0 and yanlisYer==0:
            print("dogru yer "+ str(dogruYer))

    else:
        print("lütfen geçerli bir sayi giriniz!")

    print("bilgisayarin tuttuğu sayi " + sayiStr )

print("Trbriksss!")
    
