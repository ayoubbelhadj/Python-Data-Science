from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="abelhadj",
    author_email="abelhadj@student.42.fr",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abelhadj/ft_package",
    packages=find_packages(),
    python_requires=">=3.10",
    license="MIT",
)