import os
import re

import pandas as pd
from bs4 import BeautifulSoup

from kneighbors import Kneighbors


class Training(object):

    def __init__(self):
        pass

    def run_training(self):
        knn = Kneighbors()

        with open('trf/saida_treinamento.csv', "w") as output:
            files = os.listdir('trf/')

            for file in files:
                if re.match(".+\d\.csv", file):
                    with open('trf/'+file, "r") as saida_file:
                        # Escreve no arquivo o conteúdo:
                        output.writelines(saida_file)


        knn.do_kneighbors("trf/saida_treinamento.csv")


    def run_trf(self, fasta_url):
        #executa a chamada para o gerar os .html
        url = 'C:/Users/victo/PycharmProjects/Finder/trf/trf.exe '+fasta_url+' 2 5 5 80 10 40 2000 -l 6'
        os.system(url)

        #conta quantos arquivos .csv já existem no diretório, para não sobrescrever
        num_csv = 0
        files = os.listdir('trf/')
        for file in files:
            if re.match(".+\d\.csv", file):
                num_csv+=1

        tr_table_files = []
        tr_table_out = []

        i = num_csv
        for file in files:
            if re.match(".+\d\.html", file):
                tr_table_files.append(file)
                tr_table_out.append("trf/saida"+str(i)+".csv")
                i+=1

        #tr_table_files tem todos os arquivos corretos terminados em .html

        i = 0
        for file in tr_table_files:
            self.__make_csv('trf/'+file, tr_table_out[i], i)
            i+=1

        return 1


    def __make_csv(self, url, output_file, num_csv):
        soup = ""

        with open(url) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        repeats_table = soup.find('table')

        # gerando a lista em colunas repeat_id,purity,unit_size,unit_number,trf_score,score
        repeat_id = []
        start = []
        end = []
        period_size = []
        copy_number = []
        consensus_size = []
        purity = []
        percent_indels = []
        trf_score = []
        a = []
        c = []
        g = []
        t = []
        entropy = []

        i = 0
        for row in repeats_table.findAll("tr"):  # para tudo que estiver em <tr>
            cells = row('td')  # encontra todos os TDs

            if len(cells) == 12 and cells[0].find(text=True) != "Indices":  # número de colunas
                repeat_id.append(i)
                i += 1

                split = cells[0].find(text=True).split("--")
                start.append(split[0])
                end.append(split[1])

                period_size.append(cells[1].find(text=True))
                copy_number.append(cells[2].find(text=True))
                consensus_size.append(cells[3].find(text=True))
                purity.append(cells[4].find(text=True))
                percent_indels.append(cells[5].find(text=True))
                trf_score.append(cells[6].find(text=True))
                a.append(cells[7].find(text=True))
                c.append(cells[8].find(text=True))
                t.append(cells[9].find(text=True))
                g.append(cells[10].find(text=True))
                entropy.append(cells[11].find(text=True))

        df = pd.DataFrame()

        df['repeat_id'] = repeat_id
        df['start'] = start
        df['end'] = end
        df['period'] = period_size
        df['copy_number'] = copy_number
        df['consensus_size'] = consensus_size
        df['purity'] = purity
        df['indels'] = percent_indels
        df['trf_score'] = trf_score
        df['a'] = a
        df['c'] = c
        df['t'] = t
        df['g'] = g
        df['entropy'] = entropy

        if num_csv == 0:
            df.to_csv(output_file, index=False)
        else:
            df.to_csv(output_file, index=False, header=False)