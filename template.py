import os

# Define project structure
project_structure = {
    "compliance_checker": [
        "webscraper.py",
        "ingest_data.py",
        "exception.py",
        "main.py",
        "requirements.txt"
    ],
    "compliance_checker/artifacts": [],
    "compliance_checker/base_model": [
        "prepare_model.py",
        "fine_tune.py"
    ],
    "compliance_checker/config": [
        "params.yml"
    ]
}

# Function to create directories and files
def create_project_structure(structure):
    for directory, files in structure.items():
        os.makedirs(directory, exist_ok=True)
        for file in files:
            file_path = os.path.join(directory, file)
            with open(file_path, "w") as f:
                if file.endswith(".py"):
                    f.write("# " + file.split(".")[0].replace("_", " ").title() + "\n")
                elif file.endswith(".yml"):
                    f.write("# YAML Configuration\n")
                elif file.endswith(".txt"):
                    f.write("# List of dependencies\n")

if __name__ == "__main__":
    create_project_structure(project_structure)
    print("Project structure created successfully.")
