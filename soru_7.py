#BINEARY SEARCH ALGORITHM

def binearySearch(dizi,istenen,sol,sag):    #fonksiyonumuzu olusturduk
   
   
    varMi=False #istenen sayiyi kontrol edecegiz

    if sol<=sag:#ortancanin solunda küçük sayilar bulunuyor, saginda ise büyük sayilar. sol, sagdan büyük oldugu surece ve
        return -1                       #istenen sayi bulunmadigi sürece devam edecek

        ortanca = (sol+sag)//2      #diziyi ortadan bölüp divide and conquere mantigi ile hareket ediyoruz.

        if dizi[ortanca] > istenen: #ortanca sayi aranilan sayidan büyük oldugu durumda
            return binearySearch(dizi,istenen,sol,ortanca-1)     #sagdaki sayi ortadan bir büyük olacak ve bununla birlikte döngüde büyük olan kisimlar isleme girmeyecek.

        if dizi[ortanca] < istenen:   #ortadaki sayi aranilan sayidan küçükse
            return binearySearch(dizi,istenen,ortanca+1,sag)     #bastaki sayi ortancadan bir büyük olarak tanimladik
                                #küçük olan kisimlar devre disi kalacak
        else:
            varMi=True  #eger ki aradigimiz sayi ortada ise boolean degerimiz True ya dönecek

    return varMi

dizi=[1]        #eleman sayisi 1 
aranilan=8
sol=0
sag=len(dizi)-1

inIt = binearySearch(dizi,aranilan,sol,sag)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")

dizi=[1,5,7,4,2,3,9]        #eleman sayisi tek
aranilan=8
sol=0
sag=len(dizi)-1

inIt = binearySearch(dizi,aranilan,sol,sag)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")

dizi=[1,8,2,4]        #eleman sayisi çift
aranilan=8
sol=0
sag=len(dizi)-1

inIt = binearySearch(dizi,aranilan,sol,sag)

if inIt:
    print("Istenilen sayi dizi içerisindedir.")

else:
    print("Istenilen sayi dizi içerisinde yoktur.")




        
