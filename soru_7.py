#BINEARY SEARCH ALGORITHM with RECURSIVE

def binearySearch(dizi,istenen,sol,sag):    #fonksiyonumuzu olusturduk
   
   
    varMi=False #istenen sayiyi kontrol edecegiz

    while sol<=sag and not varMi:   #ortancanin solunda küçük sayilar bulunuyor, saginda ise büyük sayilar. sol, sagdan büyük oldugu surece ve
                                    #istenen sayi bulunmadigi sürece devam edecek
        ortanca = (sol+sag)//2      #diziyi ortadan bölüp divide and conquere mantigi ile hareket ediyoruz.

        if dizi[ortanca] > istenen: #ortanca sayi aranilan sayidan büyük oldugu durumda
            return binearySearch(dizi,istenen,sol,ortanca-1)     #sagdaki sayi ortadan bir büyük olacak ve bununla birlikte döngüde büyük olan kisimlar isleme girmeyecek.

        elif dizi[ortanca] < istenen:   #ortadaki sayi aranilan sayidan küçükse
            return binearySearch(dizi,istenen,ortanca+1,sag)     #bastaki sayi ortancadan bir büyük olarak tanimladik
                                #küçük olan kisimlar devre disi kalacak
        else:
            varMi=True  #eger ki aradigimiz sayi ortada ise boolean degerimiz True ya dönecek

    return varMi
#----------------->DİZİ 1 ELEMANLI
dizi=[1]        
aranilan=8
sol=0
sag=len(dizi)-1

inIt = binearySearch(dizi,aranilan,sol,sag)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")

#----------------->DİZİ ELEMAN SAYISI TEK

dizi=[1,5,7,4,2,3,9]       
aranilan=8
sol=0
sag=len(dizi)-1

inIt = binearySearch(dizi,aranilan,sol,sag)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")
      
#----------------->DİZİ ELEMAN SAYISI ÇİFT

dizi=[1,8,2,4]        #eleman sayisi çift
aranilan=8
sol=0
sag=len(dizi)-1

inIt = binearySearch(dizi,aranilan,sol,sag)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")

        
