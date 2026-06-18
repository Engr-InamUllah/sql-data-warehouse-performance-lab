import unittest
from src.benchmark import benchmark
class BenchmarkTest(unittest.TestCase):
 def test_runs(self):
  result=benchmark(1000);self.assertIn("with_index_ms",result);self.assertGreaterEqual(result["with_index_ms"],0)
if __name__=="__main__":unittest.main()