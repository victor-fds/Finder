import os
import re

import training

do_message = 0
trx = training.Training()

while do_message >= 0:
    print("\n\n\n------- Finder v1.0.0 -------")
    if do_message == 1:
        print("Arquivos de treinamento gerados com sucesso!")
    print("Menu:")
    print("1 - Treinamento")
    print("2 - Classificação")
    print("3 - Sair")
    print("Escolha: ", end="")
    op = int(input())

    if op == 1:
        print("\n\n\nTreinamento")
        print("1 - Procurar por TRs para iniciar o treinamento")
        print("2 - Treinar com as TRs armazenadas")
        print("Escolha: ", end="")
        train = int(input())

        if train == 1:
            print("\nDigite 0 para voltar ao menu iniciar")
            print("Path do arquivo .fasta: ", end="")
            fasta_input = str(input())
            if fasta_input == "0":
                continue
            else:
                trx.run_trf(fasta_input)
                do_message = 1
        else:
            trx.run_training()
            do_message = 1
    elif op == 2:
        print("\n\nClassificação")
        print("1 - Entrar com um TR para análise")
        print("Escolha: ")
        classify = int(input())
    else:
        do_message = -1