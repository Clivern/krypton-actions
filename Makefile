PYTHON ?= python3
PIP ?= $(PYTHON) -m pip


help: Makefile
	@echo
	@echo " Choose a command run in Krypton:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo


## config: Install dependencies.
config:
	$(PIP) install pycodestyle
	$(PIP) install flake8
	$(PIP) install flake8-comprehensions
	$(PIP) install flake8-eradicate
	$(PIP) install flake8-todo
	$(PIP) install -r requirements.txt


## lint-pycodestyle: PyCode Style Lint
lint-pycodestyle:
	@echo "\n>> ============= Pycodestyle Linting ============= <<"
	@find app -type f -name \*.py | while read file; do echo "$$file" && pycodestyle --config=./pycodestyle --first "$$file" || exit 1; done


## lint-flake8: Flake8 Lint.
lint-flake8:
	@echo "\n>> ============= Flake8 Linting ============= <<"
	@find app -type f -name \*.py | while read file; do echo "$$file" && flake8 --config=flake8.ini "$$file" || exit 1; done


## lint: Lint The Code.
lint: lint-pycodestyle lint-flake8
	@echo "\n>> ============= All linting cases passed! ============= <<"


## outdated-pkg: Show outdated python packages
outdated-pkg:
	@echo "\n>> ============= List Outdated Packages ============= <<"
	$(PIP) list --outdated


## ci: Run all CI tests.
ci: lint outdated-pkg
	@echo "\n>> ============= All quality checks passed ============= <<"


.PHONY: help