format:
	isort .
	black .
	flake8 .

test:
	python manage.py test flashcard_project/components