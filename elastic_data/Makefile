ENV_NAME = elastic_env

run:
	@echo "Running main.py in conda env..."
	conda run -n $(ENV_NAME) python main.py

env:
	@echo "Creating conda environment ($(ENV_NAME))..."
	# conda env list | grep $(ENV_NAME) || conda env create -f environment.yaml
	conda env update -n $(ENV_NAME) -f environment.yaml --prune
clean:
	@echo "Removing conda environment ($(ENV_NAME))..."
	conda remove --name $(ENV_NAME) --all -y
