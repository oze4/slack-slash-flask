from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

PORT = os.getenv("PORT")
