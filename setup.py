from setuptools import find_packages, setup

with open("README.rst") as f:
    readme_text = f.read()

with open("LICENSE") as f:
    license_text = f.read()

setup(
    name="django_account_api",
    version="0.0.1",
    install_requires=["django>=3", "djangorestframework", "django-rest-knox"],
    url="https://www.github.com/nvn-nil/django_account_api",
    license="MIT",
    author="@nvn-nil",
    description="A Django app to setup auth api end points",
    long_description=readme_text,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)
