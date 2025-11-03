from setuptools import setup, find_packages

setup(
    name="how-shell-assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "ollama==0.6.0",
        "pyperclip==1.11.0",
        "psutil==7.1.3"
    ],
    entry_points={
        "console_scripts": [
            "how2=how.cli:main",  
        ],
    },
    python_requires=">=3.9",
    description="Command-line shell assistant using LLMs",
    author="Dan Higgins",
    license="MIT",
)
