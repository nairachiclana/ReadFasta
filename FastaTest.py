
import unittest
from Fasta import Fasta


class TestMethods(unittest.TestCase):

    def test_should_incorrectFileName_raise_an_error_inPairs(self):
        with self.assertRaises(Exception):
            f = 'nada'
            fasta = Fasta(f)
            fasta.read_fasta_file_as_list_of_pairs()

    def test_should_incorrectFileName__Raise_an_error_inDic(self):
        with self.assertRaises(Exception):
            f = 'nada'
            fasta = Fasta(f)
            fasta.read_fasta_file_as_dictionary()

    def test_should_lastID_be_Rosalind_2869(self):
        f = 'rosalind_grph.txt'
        fasta = Fasta(f)
        last = fasta.read_fasta_file_as_list_of_pairs()
        self.assertEqual('Rosalind_2869', str(last.id[0:14]))

    def test_should_lastSeq_begin_by_GTTACGAGCC_in_list(self):
        f = 'rosalind_grph.txt'
        fasta = Fasta(f)
        last = fasta.read_fasta_file_as_list_of_pairs()
        self.assertEqual('GTTACGAGCC', str(last.seq[0:10]))

    def test_should_seq_of_Rosalind_5878_be_CACCCACCT_inDic(self):
        f = 'rosalind_grph.txt'
        fasta = Fasta(f)
        prueba = fasta.read_fasta_file_as_dictionary()
        self.assertEqual('CACCCACCT', str(prueba['Rosalind_5878'])[6:15])



if __name__=='__main__':
    unittest.main()