# Portfolio Management App

## Running the App
- Open terminal in the `server` directory
- Create a virtual python env and install the required dependencies
- Activate the virtual env using `source bin/activate`
- Run the `python3 tests/helpers/create_in_memory_db.py` script to create a SQLite database
- Run `uvicorn src.api.app:app --reload` to start the backend