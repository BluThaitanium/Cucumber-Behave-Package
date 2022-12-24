from setuptools import setup
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="behave_cucumber_formatter",
    version="1.0.0",
    license="THE_UNLICENSED",
    author="Phu Thai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["behave_cucumber_formatter"],
    description="Cucumber JSON formatter for pipeline tests",
    install_requires=["behave>=1.2.3,<=1.3"],
    url="https://github.com/BluThaitanium/Cucumber-Behave-Package",
    keywords=["cucumber", "behave", "formatter", "testing"],
)
