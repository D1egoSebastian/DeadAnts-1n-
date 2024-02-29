import unittest
from deadants import antsfunction

class TestAntFunction(unittest.TestCase):
    def test_ants1(self):
        ants_problem = "ant anantt aantn"
        self.assertEqual(antsfunction(ants_problem), 2)
        
    def test_ants2(self):
        ants_problem = ""
        self.assertEqual(antsfunction(ants_problem), 0)
    
    def test_ants3(self):
        ants_problem = "ant ant .... a nt"
        self.assertEqual(antsfunction(ants_problem), 1)

    def test_ants4(self):
        ants_problem = "a n t"
        self.assertEqual(antsfunction(ants_problem), 1)

    def test_ants5(self):
        ants_problem = ".n..tt.n.nt..t.ntant..aaaaa..tn.na.aaat..n..tn.ntan.t" 
        self.assertEqual(antsfunction(ants_problem), 9)

if __name__ == '__main__':
    unittest.main()