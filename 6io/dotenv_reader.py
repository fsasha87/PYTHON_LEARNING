# dotenv:p_i_python-dotenv->.env:HOST=localhost->a.py:i_os->load_dotenv()->print(os.getenv(''))

#  pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

print(int(os.getenv('PORT')))
print(os.getenv('HOST'))

