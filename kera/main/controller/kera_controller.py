from django.http import JsonResponse
import datetime
import hashlib
import pandas as pd
import os

def handle(request,methode):
    method = request.method
    if(method == 'POST'):
        filename=request.read()
        test=create_csv(filename,methode)
        return JsonResponse(test,safe=False)


def create_csv(filename: str, methode) -> str:
    data_path = 'C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'#changer path 
    csv_md5 = hashlib.md5(str(filename).encode())
    csv_id = csv_md5.hexdigest()
    csv = open(data_path+csv_id+'.csv', 'wb')
    csv.write(filename)
    csv.close()
    result=csv_reader(csv_id,methode)
    return result

def csv_reader(csv_id,methode):
    #Lire le CSV
    df = pd.read_csv('C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'+csv_id+'.csv')#changer path 
    df['Date'] = pd.to_datetime(df['Date'],format="%d/%m/%Y")
    df = df.sort_values(by='Date',ascending = False)
    #Définir les différentes variables
    dernière_donnée = df.iloc[0,:]
    date_naissance=str(dernière_donnée.date_naissance)
    date=str(dernière_donnée.Date)
    kmean=int(dernière_donnée.Kmean)
    pachy=int(dernière_donnée.pachy)
    myopie=int(dernière_donnée.myopie)
    opacite=(str(dernière_donnée.opacite)) 
    AVC=float(dernière_donnée.AVC)
    sphere=float(dernière_donnée.spherique)
    SAI=float(dernière_donnée.SAI)
    kmax=dernière_donnée.kmax
    cylindre=dernière_donnée.cylindre
    rayon_lentille=dernière_donnée.rayon_lentille
    k1=dernière_donnée.k1
    k2=dernière_donnée.k2
    date_q=""
    kmean_q=None
    pachy_q=None
    myopie_q=None
    AVC_q=None
    sphere_q=None
    SAI_q=None
    kmax_q=None
    cylindre_q=None
    rayon_lentille_q=None
    k1_q=None
    k2_q=None
    date_s=""
    kmean_s=None
    pachy_s=None
    myopie_s=None
    AVC_s=None
    sphere_s=None
    SAI_s=None
    kmax_s=None
    cylindre_s=None
    rayon_lentille_s=None
    k1_s=None
    k2_s=None
    date_d=""
    kmean_d=None
    pachy_d=None
    myopie_d=None
    AVC_d=None
    sphere_d=None
    SAI_d=None
    kmax_d=None
    cylindre_d=None
    rayon_lentille_d=None
    k1_d=None
    k2_d=None
    warning= ""

    #Tri des variables selon leur anciennete on recherche les données correspondant a 3, 6 ou 12 mois 
    for j in range (len (df)):
        j=j+1
        premiere_ligne = df.iloc[j,:]
        difference_premiere = (dernière_donnée.Date - premiere_ligne.Date)
        mois=round(difference_premiere.days/30.5)
        if ( 3 <= mois <= 5 and date_q == ""):
            kmean_q=premiere_ligne.Kmean
            pachy_q=premiere_ligne.pachy
            myopie_q=premiere_ligne.myopie
            AVC_q=premiere_ligne.AVC
            sphere_q=premiere_ligne.spherique
            SAI_q=premiere_ligne.SAI
            kmax_q=premiere_ligne.kmax
            cylindre_q=premiere_ligne.cylindre
            rayon_lentille_q=premiere_ligne.rayon_lentille
            k1_q=premiere_ligne.k1
            k2_q=premiere_ligne.k2
        if (6 <= mois <= 8 and date_s == ""):
            if(date_q==""):
                autre_ligne = df.iloc[j-1,:]
                kmean_q=autre_ligne.Kmean
                pachy_q=autre_ligne.pachy
                myopie_q=autre_ligne.myopie
                AVC_q=autre_ligne.AVC
                sphere_q=autre_ligne.spherique
                SAI_q=autre_ligne.SAI
                kmax_q=autre_ligne.kmax
                cylindre_q=autre_ligne.cylindre
                rayon_lentille_q=autre_ligne.rayon_lentille
                k1_q=autre_ligne.k1
                k2_q=autre_ligne.k2
            kmean_s=premiere_ligne.Kmean
            pachy_s=premiere_ligne.pachy
            myopie_s=premiere_ligne.myopie
            AVC_s=premiere_ligne.AVC
            sphere_s=premiere_ligne.spherique
            SAI_s=premiere_ligne.SAI
            kmax_s=premiere_ligne.kmax
            cylindre_s=premiere_ligne.cylindre
            rayon_lentille_s=premiere_ligne.rayon_lentille
            k1_s=premiere_ligne.k1
            k2_s=premiere_ligne.k2
        if (12 <= mois <= 13 and date_d == ""):
            if(date_s==""):
                autre_ligne = df.iloc[j-1,:]
                kmean_q=autre_ligne.Kmean
                pachy_q=autre_ligne.pachy
                myopie_q=autre_ligne.myopie
                AVC_q=autre_ligne.AVC
                sphere_q=autre_ligne.spherique
                SAI_q=autre_ligne.SAI
                kmax_q=autre_ligne.kmax
                cylindre_q=autre_ligne.cylindre
                rayon_lentille_q=autre_ligne.rayon_lentille
                k1_q=autre_ligne.k1
                k2_q=autre_ligne.k2
            kmean_d=premiere_ligne.Kmean
            pachy_d=premiere_ligne.pachy
            myopie_d=premiere_ligne.myopie
            AVC_d=premiere_ligne.AVC
            sphere_d=premiere_ligne.spherique
            SAI_d=premiere_ligne.SAI
            kmax_d=premiere_ligne.kmax
            cylindre_d=premiere_ligne.cylindre
            rayon_lentille_d=premiere_ligne.rayon_lentille
            k1_d=premiere_ligne.k1
            k2_d=premiere_ligne.k2
            break
        if (mois >13 and date_d == ""):
            if(date_s==""):
                autre_ligne = df.iloc[j-1,:]
                kmean_s=autre_ligne.Kmean
                pachy_s=autre_ligne.pachy
                myopie_s=autre_ligne.myopie
                AVC_s=autre_ligne.AVC
                sphere_s=autre_ligne.spherique
                SAI_s=autre_ligne.SAI
                kmax_s=autre_ligne.kmax
                cylindre_s=autre_ligne.cylindre
                rayon_lentille_s=autre_ligne.rayon_lentille
                k1_s=autre_ligne.k1
                k2_s=autre_ligne.k2
            kmean_d=premiere_ligne.Kmean
            pachy_d=premiere_ligne.pachy
            myopie_d=premiere_ligne.myopie
            AVC_d=premiere_ligne.AVC
            sphere_d=premiere_ligne.spherique
            SAI_d=premiere_ligne.SAI
            kmax_d=premiere_ligne.kmax
            cylindre_d=premiere_ligne.cylindre
            rayon_lentille_d=premiere_ligne.rayon_lentille
            k1_d=premiere_ligne.k1
            k2_d=autre_ligne.k2
            warning="donnée datant 13 mois ou plus"
            break
    if(kmean_d==None):
        if(kmean_s==None):
            old_Kmean=kmean_q
            old_Myopie=myopie_q
            old_pachy=pachy_q
            old_AVC=AVC_q
            old_sphere=float(sphere_q)
            old_SAI=float(SAI_q)
            old_kmax=kmax_q
            old_cylindre=cylindre_q
            old_rayon_lentille=rayon_lentille_q
            old_k1=k1_q
            old_k2=k2_q
            warning="donnée datant de 4 mois"
        else:
            old_Kmean=kmean_s
            old_Myopie=myopie_s
            old_pachy=pachy_s
            old_AVC=AVC_s
            old_sphere=float(sphere_s)
            old_SAI=float(SAI_s)
            old_kmax=kmax_s
            old_cylindre=cylindre_s
            old_rayon_lentille=rayon_lentille_s
            old_k1=k1_s
            old_k2=k2_s
            warning="donnée datant de 6 mois ou plus"
    else:
        old_Kmean=kmean_d
        old_Myopie=myopie_d
        old_pachy=pachy_d
        old_AVC=AVC_d
        old_sphere=float(sphere_d)
        old_SAI=float(SAI_d)
        old_kmax=kmax_d
        old_cylindre=cylindre_d
        old_rayon_lentille=rayon_lentille_d
        old_k1=k1_d
        old_k2=k2_d

    if(methode=="Determiner le KC"):
        result=determiner_KC(myopie,kmean,opacite,pachy)
    if(methode=="Méthode de Stojanovic"):
        result=stojanovic(myopie,kmean,old_Myopie,old_Kmean,warning)
    if(methode=="Méthode de Mazzotta"):
        result=mazotta(kmean,old_Kmean,pachy,old_pachy,AVC,old_AVC,sphere,old_sphere,SAI,old_SAI,warning,date_naissance)
    if(methode=="Méthode de Wittig-Silva 2008"):
        result=Wittig_Silva_2008(kmax,old_kmax,cylindre,old_cylindre,sphere,old_sphere,rayon_lentille,old_rayon_lentille,warning)
    if(methode=="Méthode de Gomes"):
        result=gomes(kmean,old_Kmean,kmax,old_kmax,k1,old_k1,k2,old_k2,pachy,old_pachy,warning)
    os.remove('C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'+csv_id+'.csv')
    return result
 
def determiner_KC(Myopie,Kmean,Opacite,Pachy):
    if (Myopie<5 and Kmean<=48 ): 
        stade=1
        KC="léger"
        return("KC léger de stade 1")
    elif (Myopie>=5 and Myopie<8 and Kmean<=53 and Opacite==0 and Pachy>=400):
        stade=2
        KC="modéré"
        return("KC modéré de stade 2")
    elif (Myopie>8 and Myopie<10 and Kmean>53 and Opacite==0 and Pachy<400 and Pachy>=300):
        stade =3
        KC="modéré"
        return("KC modéré de stade 3")
    elif (Kmean>=55 and Opacite==1 and Pachy<300):
        stade=4
        KC="sévère"
        return("KC sévère de stade 4")
    else :
        stade=4
        KC="sévère"
        return "données discordantes concidéré comme stade 4"

def stojanovic(Myopie,Kmean,old_Myopie,old_Kmean,warning):
    if(Kmean-old_Kmean>=1.5 or Myopie-old_Myopie>=1):
        return ("La maladie est evolutive "+warning)    
    else:
        return ("La maladie n'est pas concidérée comme évolutive "+warning)

def mazotta(Kmean,old_Kmean,pachy,old_pachy,AVC,old_AVC,sphere,old_sphere,SAI,old_SAI,warning,date_naissance):
    i=0
    date_j=datetime.datetime.today()
    myDatetime = datetime.datetime.strptime(date_naissance,'%d/%m/%Y')
    age=date_j.year-myDatetime.year
    if(age<18):
        if(AVC-old_AVC>0.5):
            i=i+1
        if(sphere-old_sphere>0.5):
            i=i+1
        if(SAI-old_SAI>1):
            i=i+1
        if(Kmean-old_Kmean>1):
            i=i+1
        if(pachy-old_pachy>10):
            i=i+1
        if(i>=3):
            return("La maladie est évolutive " + warning)
        else:
            return("La maladie n'est pas concidérée comme évolutive " + warning)
    if(age>=18):
        if(AVC-old_AVC>0.5):
            i=i+1
        if(sphere-old_sphere>0.5):
            i=i+1
        if(SAI-old_SAI>1):
            i=i+1
        if(Kmean-old_Kmean>1):
            i=i+1
        if(pachy-old_pachy>10):
            i=i+1
        if(i>=3):
            return("La maladie est évolutive " + warning)
        else:
            return("La maladie n'est pas concidérée comme évolutive " + warning)

def Wittig_Silva_2008(kmax,old_kmax,cylindre,old_cylindre,sphere,old_sphere,rayon_lentille,old_rayon_lentille,warning):
    i=0
    if(kmax-old_kmax>=1):
        i=i+1
    if(cylindre-old_cylindre>=1):
        i=i+1
    if(sphere-old_sphere>=1):
        i=i+1
    if(old_rayon_lentille-rayon_lentille>=0.1):
        i=i+1
    if(i>=1):
        return("La maladie est évolutive " + warning)       
    else:
        return("La maladie n'est pas considérée comme évolutive " + warning)

def gomes(kmean,old_kmean,kmax,old_kmax,k1,old_k1,k2,old_k2,pachy,old_pachy,warning):
    i=0
    if(kmean-old_kmean>=1):
        i=i+1
    if(kmax-old_kmax>=1):
        i=i+1
    if(k1-old_k1>=1):
        i=i+1
    if(k2-old_k2>=1):
        i=i+1
    if(100-(pachy/old_pachy)*100>=5):
        i=i+1
    if(i>=2):
        return("La maladie est évolutive " + warning)
    else:
        return("La maladie n'est pas concidérée comme évolutive " + warning)