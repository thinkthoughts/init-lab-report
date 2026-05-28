setup:
	pip install -r requirements.txt

init:
	jupyter nbconvert --execute --to notebook --inplace notebooks/init.ipynb
