"""Determination de sièges dans une assemblée en fonction du nombre
de voix des listes"""

NB_DE_SIEGES = 100
dict_resultats_en_voix = {
"A":100153,
"B":181538,
"C":158894,

}

#dict_resultats_en_sieges nombre de sieges
dict_resultats_en_sieges = dict_resultats_en_voix.copy()
for i in dict_resultats_en_sieges:
    dict_resultats_en_sieges[i]=0



NB_DE_VOIX_TOTALES = 0
ST = 0

#Calcul nombre de voix
for i in dict_resultats_en_voix:
    nb_voix_candidat = (dict_resultats_en_voix.get(i))
    NB_DE_VOIX_TOTALES = NB_DE_VOIX_TOTALES+nb_voix_candidat

print ("Nombre de voix exprimées ",NB_DE_VOIX_TOTALES)


quotient_electoral = (NB_DE_VOIX_TOTALES/NB_DE_SIEGES)

print ("Quotient Electoral ", quotient_electoral)

for i in dict_resultats_en_voix:
    QES = (dict_resultats_en_voix.get(i))
    SG = int(QES/quotient_electoral)
    print (i,SG, "sieges")
    dict_resultats_en_sieges[i]= SG

#Calcul sieges attribués
for i in dict_resultats_en_sieges:
    SS = (dict_resultats_en_sieges.get(i))
    ST = ST+SS

print (ST)
SIR = NB_DE_SIEGES-ST
print (SIR)

VXX=0
SGP=0
#Distribution sieges restants
resultats_en_qe = dict_resultats_en_sieges.copy()
print (resultats_en_qe)
T = 1
while T < SIR+1:

    for i in resultats_en_qe:
        VXX=dict_resultats_en_voix[i]
        SGP=dict_resultats_en_sieges[i]+1
        MOY=VXX/SGP
        resultats_en_qe[i]= MOY

    v=list(resultats_en_qe.values())
    k=list(resultats_en_qe.keys())
    GG= ( k[v.index(max(v))])
    dict_resultats_en_sieges[GG]=dict_resultats_en_sieges[GG]+1
    print (GG)
    T=T+1
    print (dict_resultats_en_sieges)
    print (resultats_en_qe)

for i in dict_resultats_en_sieges:
    sieges_final= dict_resultats_en_sieges[i]
    print (i,sieges_final, "sieges")
