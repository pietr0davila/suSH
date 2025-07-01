from setuptools import setup, find_packages

setup(
    name="suSH",
    version="0.1.0",
    author="Pietr0Davila",
    author_email="dsescuderop@gmail.com",
    description="Terminal interativo feito em python",
    url="github.com/pietr0davila/suSH",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "prompt_toolkit>=3.0.0",
        "colorama>=13.0.0",
        "rich>=13.0.0",
        "cryptography>=42.0.0",
    ],
    entry_points={
        "console_scripts": [
            "sush=main:main"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operation System :: OS Independent"
    ],
    include_package_data=True
)