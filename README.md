# Application-quality-python-flask
## Running servce
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python hello.py  # and access http://localhost:5000
```

We have two endpoints / -- it prints hello world
                      /num accepts a number num=<number> and returns a new number by adding 100 to the number.
## Running tests
```bash
pytest
```