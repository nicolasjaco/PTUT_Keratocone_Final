from django.http import JsonResponse
from django.conf import settings
import csv
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
    data_path = 'C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'
    csv_md5 = hashlib.md5(str(filename).encode())
    csv_id = csv_md5.hexdigest()
    csv = open(data_path+csv_id+'.csv', 'wb')
    csv.write(filename)
    csv.close()
    result=csv_reader(csv_id,methode)
    return result

def csv_reader(csv_id,methode):
    #Lire le CSV
    df = pd.read_csv('C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'+csv_id+'.csv')
    df['Date'] = pd.to_datetime(df['Date'],format="%d/%m/%Y")
    df = df.sort_values(by='Date',ascending = False)

    #Définir les différentes variables
    dernière_donnée = df.iloc[0,:]
    date=str(dernière_donnée.Date)
    kmean=int(dernière_donnée.Kmean)
    pachy=int(dernière_donnée.pachy)
    myopie=int(dernière_donnée.myopie)
    opacite=(str(dernière_donnée.opacite)) 
    quatre = df.iloc[1,:]
    difference_4 = (dernière_donnée.Date - quatre.Date)
    if(methode=="Determiner le KC"):
        result=determiner_KC(myopie,kmean,opacite,pachy)
    if(methode=="Méthode de Stojanovic"):
        result="hello"
    if(methode=="Méthode de Mazzotta"):
        result="hello"
    if(methode=="Méthode de Wittig-Silva 2008"):
        result="hello"
    if(methode=="Méthode de Gomes"):
        result="hello"
    os.remove('C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'+csv_id+'.csv')

    #Conditions selon l'anciennete des variables
    if ( 100 <= difference_4.days <= 140):
        six = df.iloc[2,:]
        difference_6 = (dernière_donnée.Date - six.Date)
        if (141 <= difference_6.days <= 240):
            return result
            # {"date":date,
            # "kmean":kmean,
            # "pachy":pachy,
            # "myopie":myopie,
            # "opacité":opacite}

        return result
        # {"date":date,
        # "kmean -4mois":kmean,
        # "pachy -4mois":pachy,
        # "myopie -4mois":myopie,
        # "opacité -4mois":opacite}
    else:  
        return result
        # {"date":date,
        #     "kmean":kmean,
        #     "pachy":pachy,
        #     "myopie":myopie,
        #     "opacité":opacite}

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

