
import sys,os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from scripts.add import load_json

#Name: Anusha Asim, Email: anushaasim21@yahoo.com, Country: UAE
def test_load_json():
  response = load_json()
  assert isinstance(response, dict)
  assert response.get("Anusha Asim") =="Football"
  pytest test/test.py -s
  
