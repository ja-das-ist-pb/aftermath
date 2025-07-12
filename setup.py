from setuptools import setup, find_packages

setup(
    name='aftermath',
    version='0.1.0',
    packages=find_packages(),
    install_requires=["numpy"],
    author='ja-das-ist-pb',
    author_email='paulpb0725@gmail.com',
    description='A lightweight math module with accurate constants and basic matrix operations.',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/ja-das-ist-pb/aftermath',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
