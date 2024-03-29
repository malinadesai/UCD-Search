from setuptools import setup, find_packages

# check that python version is 3.8 or above
python_version = sys.version_info
if python_version < (3, 8):
    sys.exit("Python < 3.8 is not supported, please install version 3.8.0 or higher.")
print("Confirmed Python version {}.{}.{} >= 3.8.0".format(*python_version[:3]))

# get the required package names
def get_requirements(kind=None):
    if kind is None:
        fname = "requirements.txt"
    else:
        fname = f"{kind}_requirements.txt"
    with open(fname, "r") as ff:
        requirements = ff.readlines()
    return requirements

setup(
    name='UCD-Search',
    version='1.0',
    description='Set of ML models developed to find UCDs in Deep Sky Surveys'
    author='Malina Desai'
    author_email='mmdesai@mit.edu'
    packages=find_packages()
    install_requires=get_requirements()
)


