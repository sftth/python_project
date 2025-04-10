ENV_NAME = k8s_env

run:
	@echo "Running main.py in conda env..."
	conda run -n $(ENV_NAME) python main.py

env:
	@echo "Creating conda environment ($(ENV_NAME))..."
	conda env list | grep $(ENV_NAME) || conda env create -f environment.yaml

clean:
	@echo "Removing conda environment ($(ENV_NAME))..."
	conda remove --name $(ENV_NAME) --all -y
