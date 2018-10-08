from Bio import SeqIO

f1 = 'rosalind_grph.txt'
f2 = 'rosalind_lcsm.txt'
f3 = 'BB11001.tfa'


class Fasta:

    def __init__(self, fileName):
        self.f=fileName

    def read_fasta_file_as_list_of_pairs(self):
        for record in SeqIO.parse(self.f, 'fasta'):
            print('[', record.id, ',', record.seq, ']')
        return record

    def read_fasta_file_as_dictionary(self):
        dic = {}
        for record in SeqIO.parse(self.f, 'fasta'):
            key=record.id
            dic.setdefault(key,[])
            dic[key].append(record.seq)
        for keys, values in dic.items():
            print(keys)
            print(values)

        return dic


pares=Fasta(f1)
print('PARES: ')
pares.read_fasta_file_as_list_of_pairs()


dic=Fasta(f2)
print('DICCIONARIO: ')
pares.read_fasta_file_as_dictionary()






