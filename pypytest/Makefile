all:
	bash ./build_env.sh
	pip-review --local --interactive
	pip-compile --upgrade --output-file requirement.txt requirement.in
	python -m pip install -r requirement.txt
	echo "build Done. exec run.sh to start"
