from django.http import JsonResponse
from django.conf import settings
import csv
import hashlib

def handle(request,age,consultation,KC):
    method = request.method
    if(method == 'POST'):
        func=suivi(age,consultation,KC)
        return JsonResponse(func,safe=False)

def suivi(age,consultation,KC):

    if (age=="moins de 15"):
        if (consultation == "oui"):
            if (KC == "léger"):
                return "1 à 3 mois ou CXL d’emblée"
            elif (KC == "modéré"):
                return "1 à 3 mois ou CXL d’emblée"
            elif (KC == "sévère"):
                return("CXL d’emblée si non contre-indiqué ou surveillance à 1 mois")
        else:
            if (KC == "léger"):
                return("3 à 6 mois")
            elif (KC == "modéré"):
                return("3 mois")
            elif (KC == "sévère"):
                return("3 mois") 
                    
    if (age=="15 a 20"):
        if (consultation == "oui"):
            if (KC == "léger"):
                return("3 mois ou CXL d’emblée")
            elif (KC == "modéré"):
                return("3 mois ou CXL d’emblée")
            elif (KC == "sévère"):
                return("CXL d’emblée si non contre-indiqué ou surveillance à 1 mois")
        else:
            if (KC == "léger"):
                return("6 mois")
            elif (KC == "modéré"):
                return("3 à 6 mois")
            elif (KC == "sévère"):
                return("3 mois") 

    if (age=="20 a 30"):
        if (consultation == "oui"):
            if (KC == "léger"):
                return("3 à 6 mois")
            elif (KC == "modéré"):
                return("3 à 6 mois")
            elif (KC == "sévère"):
                return("3 mois")
        else:
            if (KC == "léger"):
                return("6 mois")
            elif (KC == "modéré"):
                return("6 mois")
            elif (KC == "sévère"):
                return("3 à 6 mois") 
            
    if (age=="30 a 40"):
        if (consultation == 1):
            if (KC == "léger"):
                return("6 mois")
            elif (KC == "modéré"):
                return("6 mois")
            elif (KC == "sévère"):
                return("3 à 6 mois")
        else:
            if (KC == "léger"):
                return("6 mois")
            elif (KC == "modéré"):
                return("6 mois")
            elif (KC == "sévère"):
                return("6 mois")
                    
    if (age=="plus de 40"):
        if (consultation == "oui"):
            if (KC == "léger"):
                return("6 mois")
            elif (KC == "modéré"):
                return("6 mois")
            elif (KC == "sévère"):
                return("6 mois")
        else:
            if (KC == "léger"):
                return("1 an")
            elif (KC == "modéré"):
                return("1 an")
            elif (KC == "sévère"):
                return("6 mois à 1 an") 