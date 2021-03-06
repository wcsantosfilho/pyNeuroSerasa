#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:23:00 2020
#PYNEUROSERASA - Parse useful information in Neurotech JSON
@author: wcsantosfilho
"""

import json
import sys
import getopt
import os

keyExpected = ["GTWR_SERASAB49C_BCREDI_LST_b001NomeTitular", \
    "GTWR_SERASAB49C_BCREDI_LST_b001CpfTitular", \
    "GTWR_SERASAB49C_BCREDI_LST_b001NovaSituacaoRf", \
    "GTWR_SERASAB49C_BCREDI_LST_b357QtdTotalOcorrc", \
    "GTWR_SERASAB49C_BCREDI_LST_b357ValorTotOcorrc", \
    "GTWR_SERASAB49C_BCREDI_LST_b357TipoOcorrencia", \
    "GTWR_SERASAB49C_BCREDI_b359TotOcorrencias", \
    "GTWR_SERASAB49C_BCREDI_b361OcorrenciasTot", \
    "GTWR_SERASAB49C_BCREDI_LST_b362Cartorio", \
    "GTWR_SERASAB49C_BCREDI_LST_b362OcorrenciasTot", \
    "GTWR_SERASAB49C_BCREDI_LST_b362Uf", \
    "GTWR_SERASAB49C_BCREDI_LST_b362ValorOcorrencia", \
    "GTWR_SERASAB49C_BCREDI_b280DescScorEscolhd", \
    "GTWR_SERASAB49C_BCREDI_b280PontuacaoScore" ]

keyLabel = ["NomeTitular", \
    "CPFTitular", \
    "Situacao Receita Federal", \
    "RESUMO PEND PAGTO - QtdTotalOcorrc", \
    "RESUMO PEND PAGTO - ValorTotOcorrc", \
    "RESUMO PEND PAGTO - TipoOcorrencia", \
    "RESUMO CHQ SEM FUNDO - TotOcorrencias", \
    "RESUMO PROTESTOS - OcorrenciasTot", \
    "DETALHE PROTESTOS - Cartorio", \
    "DETALHE PROTESTOS - OcorrenciasTot", \
    "DETALHE PROTESTOS - Uf", \
    "DETALHE PROTESTOS - ValorOcorrencia", \
    "SCORING - DescScorEscolhd", \
    "SCORING - PontuacaoScore" ]

if __name__ == "__main__":
    if ( len(keyExpected) != len(keyLabel) ):
        sys.exit("Problema nas listas. Verifique")

    inputdir = ''
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'pyNeuro.py -i <inputdir> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'pyNeuro.py -i <inputdir> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg    
    print 'Input dir is "', inputdir
    print 'Output file is "', outputfile
    inputdir = inputdir.strip()
    dirs = os.listdir( inputdir )
    outputfile = outputfile.strip()
    g = open(outputfile, "wt")

    for keyItem in keyLabel:
        g.write(keyItem)
        g.write(',')
    g.write('\n')

    for inputfile in dirs:
        print (inputdir+inputfile)
        inputfile = inputfile.strip()
        f = open(inputdir+inputfile)
        r = f.read().decode('utf8')

        y = json.loads(r)
        z = y["Result"]["Outputs"]
        thisdict = {}
        for xpto in z:
            zKey = xpto["Key"]
            thisdict[zKey] = xpto["Value"]
        w = ''
        for keyItem in keyExpected:
            wKey = keyItem
            w = thisdict[wKey]
            #g.write(wKey)
            #g.write('=')
            g.write(w.encode('utf8'))
            g.write(',')

        g.write('\n')

    g.close()
    print("-----------")
    print("FIM")