import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REPO_NAME = "StreamLab"
AUTHOR_USER_NAME = "Sabbir-Azim"
AUTHOR_EMAIL = "fazley.azim.sabbir@gmail.com"
SRC_REPO = "StreamLab"

setuptools.setup(
    name=REPO_NAME,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)