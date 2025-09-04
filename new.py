import os

# Define project structure
structure = {
    "SignSpeak": {
        "backend": {
            "utils": ["speech_to_text.py", "text_to_sign.py", "avatar_engine.py", "__init__.py"],
            "models": ["translator_model.py", "avatar_model.py", "__init__.py"],
            "static": {
                "css": [],
                "js": [],
                "avatars": []
            },
            "__files__": ["__init__.py", "app.py", "routes.py"]
        },
        "frontend": {
            "templates": ["index.html", "avatar.html", "signin.html"],
            "static": {
                "css": [],
                "js": [],
                "img": []
            }
        },
        "data": {
            "sign_videos": [],
            "datasets": [],
            "preprocessed": []
        },
        "notebooks": ["model_training.ipynb", "experiments.ipynb"],
        "tests": ["test_speech.py", "test_sign.py", "test_avatar.py"],
        "__files__": ["requirements.txt", "README.md", ".gitignore"]
    }
}

# Function to create folders/files
def create_structure(base, struct):
    for name, content in struct.items():
        if name == "__files__":
            for file in content:
                file_path = os.path.join(base, file)
                with open(file_path, "w") as f:
                    f.write(f"# {file}\n")
        elif isinstance(content, dict):
            path = os.path.join(base, name)
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            path = os.path.join(base, name)
            os.makedirs(path, exist_ok=True)
            for file in content:
                with open(os.path.join(path, file), "w") as f:
                    f.write(f"# {file}\n")

# Run script
create_structure(".", structure)
print("✅ Project structure created successfully!")
