# UCD-Search
This is a collection of Jupyter Notebooks that aim to create a UCD sample from deep sky surveys using machine learning tools. 

### Installation Guide
To install and test these random forest models, follow the steps below.
First, clone the repository in your terminal using:

```
git clone https://github.com/malinadesai/UCD-Search
```

To make full use of the data provided in this code, an Astro Data Lab login is required. Follow the instructions to create an account at: https://datalab.noirlab.edu/account/login.html. If you wish to access data from the deep sky surveys, you must run these notebooks in Astro Data Lab's jupyter server. For convenience, the training, testing, and validation data are located in the `data` folder and can be used and accessed without an account. 

The required package dependencies are located in the `requirements.txt` file and can be installed through the `setup.py` script by running the following:

```
pip install -r requirements.txt
python setup.py install
```

You can check your pip and python versions in the command line by running:

```
python --version
pip --version
```
to see if any updates are required. 









