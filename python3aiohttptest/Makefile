all:
	bash ./init.sh
	pip-review --local --interactive
	pip-compile --upgrade --output-file requirement.txt requirement.in
	python3 -m pip install -r requirement.txt
	echo "build Done. exec python3 hello.py to start"
