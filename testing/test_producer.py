from dotenv import load_dotenv
import os 

load_dotenv()

def test_something():
    assert os.environ['VAR'] == 'hell'