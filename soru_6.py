#BINEARY SEARCH ALGORITHM

def binearySearch(dizi,istenen):    #fonksiyonumuzu olusturduk
    n=len(dizi)
    sol=0           #dizimizi sol ve sag olmak üzere iki parta bölücez
    sag=n-1
    varMi=False #istenen sayiyi kontrol edecegiz

    while sol<=sag and not varMi:   #ortancanin solunda küçük sayilar bulunuyor, saginda ise büyük sayilar. sol, sagdan büyük oldugu surece ve
                                    #istenen sayi bulunmadigi sürece devam edecek
        ortanca = (sol+sag)//2      #diziyi ortadan bölüp divide and conquere mantigi ile hareket ediyoruz.

        if dizi[ortanca] > istenen: #ortanca sayi aranilan sayidan büyük oldugu durumda
            sag = ortanca-1     #sagdaki sayi ortadan bir büyük olacak ve bununla birlikte döngüde büyük olan kisimlar isleme girmeyecek.

        elif dizi[ortanca] < istenen:   #ortadaki sayi aranilan sayidan küçükse
            sol = ortanca+1     #bastaki sayi ortancadan bir büyük olarak tanimladik
                                #küçük olan kisimlar devre disi kalacak
        else:
            varMi=True  #eger ki aradigimiz sayi ortada ise boolean degerimiz True ya dönecek

    return varMi

dizi=[1]        #eleman sayisi 1 
aranilan=8

inIt = binearySearch(dizi,aranilan)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")

dizi=[1,5,7,4,2,3,9]        #eleman sayisi tek
aranilan=8

inIt = binearySearch(dizi,aranilan)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")

dizi=[1,8,2,4]        #eleman sayisi çift
aranilan=8

inIt = binearySearch(dizi,aranilan)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")




        
