import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ectrello", # Replace with your own username
    version="1.0",
    author="Hadi Alnehlawi",
    author_email="hadi.alnehlawi@gmail.com,
    description="Easy And Productive CLI To Interac With Trello API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
