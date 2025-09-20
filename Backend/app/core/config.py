import os
from dotenv import load_dotenv
load_dotenv()

POSTGRESQL_CONNECTION_STRING=os.getenv("POSTGRESQL_CONNECTION_STRING")