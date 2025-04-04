import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
