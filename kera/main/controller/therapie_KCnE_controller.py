from django.http import JsonResponse
import hashlib
import pandas as pd
import os

def handle(request,type_op):
    method = request.method
    if(method == 'POST'):
        filename=request.read()
        test=create_csv(filename,type_op)
        return JsonResponse(test,safe=False)

def create_csv(filename: str, type_op) -> str:
    data_path = 'C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'#changer path 
    csv_md5 = hashlib.md5(str(filename).encode())
    csv_id = csv_md5.hexdigest()
    csv = open(data_path+csv_id+'.csv', 'wb')
    csv.write(filename)
    csv.close()
    result=csv_reader(csv_id,type_op)
    return result


def csv_reader(csv_id,type_op):
    #Lire le CSV
    df = pd.read_csv('C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'+csv_id+'.csv')#changer path s
    df['Date'] = pd.to_datetime(df['Date'],format="%d/%m/%Y")
    df = df.sort_values(by='Date',ascending = False)
    #Définir les différentes variables
    dernière_donnée = df.iloc[0,:]
    AV=dernière_donnée.AV
    kctype=dernière_donnée.Kctype
    result=kcne(type_op,kctype,AV)
    os.remove('C:/Users/Nicolas/Desktop/Kera/kera/main/csv/'+csv_id+'.csv')
    return result

def kcne(type_op,kctype,AV):
        if (type_op == "LR"):
            if (AV >=0.8):
                return("Surveillance du patient sans opération pendant 3 mois")
            else :
                if (kctype == "central"):
                    return("Nous vous conseillons de faire l'opération PTK")
                else :
                    return("Nous vous conseillons de faire l'opération AIC")

        elif (type_op == "AIC"):
            if (AV >=0.8):
                return("Surveillance du patient sans opération pendant 3 mois")
            else :
                return("Nous vous conseillons de faire l'opération Keratoplastie")
        elif (type_op == "PTK"):
            if (AV >=0.8):
                return("Surveillance du patient sans opération pendant 3 mois")
            else :
                return("Nous vous conseillons de faire l'opération Keratoplastie")
        else :
            if (AV >=0.8):
                return("Surveillance du patient sans opération")
            else :
                return("Nous vous conseillons de faire l'opération LR")
