# -*- coding: utf-8 -*-
import csv, codecs

class Candidates(object):

    w={}
    reader = codecs.open("candidates.csv", 'r', encoding='utf-8')
    i=0
    for line in reader:
        line=line.split(',')
        Full_Name = line[14]
        Race = line[39]
        Constituency = line[6]
        Sub_District = line[46]
        voting_district=line[45]
        ballot_number=line[7]
        District = line[5]
        if i!=0:
            if  w.get(District) == None:
                w[District]={}
            if w[District].get(Sub_District) == None:
                w[District][Sub_District]={}
            if w[District][Sub_District].get(Race)==None :
                w[District][Sub_District][Race]={}
            if w[District][Sub_District][Race].get(ballot_number)== None:
                 w[District][Sub_District][Race][ballot_number]={}
            if w[District][Sub_District][Race][ballot_number].get('names')== None:
                 w[District][Sub_District][Race][ballot_number]['names']=[]
            if w[District][Sub_District][Race][ballot_number].get('num')== None:
                w[District][Sub_District][Race][ballot_number]['num']=0
            if w[District][Sub_District][Race][ballot_number].get('constituency')== None:
                w[District][Sub_District][Race][ballot_number]['constituency']=Constituency
            if w[District][Sub_District][Race][ballot_number].get('ballot_number')== None:
                w[District][Sub_District][Race][ballot_number]['ballot_number']=ballot_number
            
            w[District][Sub_District][Race][ballot_number]['names'].append(Full_Name)
            w[District][Sub_District][Race][ballot_number]['num']=len(w[District][Sub_District][Race][ballot_number]['names'])
            w[District][Sub_District][Race][ballot_number]['voting_district']=voting_district
            w[District][Sub_District][Race][ballot_number]['ballot_number']=ballot_number

            
            # if(w[District][Sub_District][Race][ballot_number]['num']>100):
            #     print ballot_number
            #     print Full_Name
        i=1   

    # def __init__(self, file_name):



#delimiter = ';'




# print(w)
