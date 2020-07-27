import os
import re

import training


def create_fasta_file(tr):
    with open('trf/teste.fasta', "w") as output:
        output.writelines(">Teste rápido\n")
        output.writelines(tr)

    output.close()

def clean_csv_from_path():
    files = os.listdir('trf/')

    # inicia o programa
    for file in files:
        if re.match("\.csv", file):
            os.remove("trf/" + file)
            files.remove(file)


do_message = 0
tr_class = training.Training()


while do_message >= 0:
    print("\n\n\n------- Finder v1.0.0 -------")
    if do_message == 1:
        print("Arquivos de treinamento gerados com sucesso!")
    elif do_message == 2:
        print("KNN treinado com sucesso!")
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
            print("Path do arquivo .fasta: ", end="")
            fasta_input = "trf/instaveis.fasta"
            tr_class.run_trf(fasta_input, 1, 1)
            fasta_input = "trf/conservados.fasta"
            tr_class.run_trf(fasta_input, 1, 0)
            do_message = 1
        else:
            tr_class.run_training()
            do_message = 2
    elif op == 2:
        print("\n\nClassificação")
        print("1 - Entrar com um TR para análise")
        print("2 - Indicar um .fasta para análise")
        print("Escolha: ", end="")
        classify = int(input())

        if classify == 1:
            print("\nPredizer características do TR")
            print("Entrada: ", end="")
            tr = input()
            create_fasta_file(tr)

            tr_class.run_trf("trf/teste.fasta", 0)
        else:
            print("\nPredizer características do TR")
            print("Arquivo .fasta: ", end="")
            #tr = input()
            tr_class.run_trf("trf/teste.fasta", 0, 0)
    else:
        do_message = -1
