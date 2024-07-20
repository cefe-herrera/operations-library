# setup.py

from setuptools import setup, find_packages

setup(
    name="math_operations",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Armando Herrera",
    author_email="armandoher01@gmail.com",
    description="Una biblioteca para operaciones matemáticas básicas",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/math_operations",  # Repositorio del proyecto
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
