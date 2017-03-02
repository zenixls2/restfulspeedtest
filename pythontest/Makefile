all:
	bash -c "source ./venv/bin/activate"
	pip-review --local --interactive
	pip-compile --output-file requirements.txt requirements.in
	pip install -r requirements.txt
	echo "build Done. exec python hello.py to start"
