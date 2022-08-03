format:
	isort .
	black .
	flake8 .

test:
	coverage run manage.py test flashcard_project/components
	coverage report
	coverage html