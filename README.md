# Country Laws

### Requirements
- Python3.6+
- pip3

## Installations:
### Python and pip3
On linux (debian based) OS follow this instructions:
```
sudo apt install python3 python3-pip
```

### Setup virtual environment
Install ```virtualenvwrapper```, it will serve as a wrapper to your project and its modules
```
pip3 install virtualenvwrapper
```

Now that you have ```virtualenvwrapper``` installed on your machine you should complete its configuration like this:
open terminal and type ```nano ~/.bashrc``` or ```nano ~/.zshrc``` if you using oh-my-zh
at the bottom of the file write the following:
```
export WORKON_HOME=$HOME/.Envs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

and if the obove exports do not work try the following:
```
export WORKON_HOME=$HOME/.Envs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source $HOME/.local/bin/virtualenvwrapper.sh
```
once done save (```ctrl+x```) and exit then activate the exports by running this command ```source ~/.bashrc``` or ```source ~/.zshrc```

Now you can create a virtual environment your machne by typing: 

```
mkvirtualenv name-of-virtualenv
```

### Adding this project to your machine
First clone it to your desired directory on your machine
```
git clone https://github.com/Sjk-Lacoste/country-laws.git
```

now 
```
cd country-laws
```
and make sure your virtualenv is activated ```workon name-of-virtualenv```
```
pip3 install -r requirements.txt
```
this will install all required modules to your virtual environment.

now migrate all tables to database by running the following command:
```
python3 manage.py migrate
```

Now you can run the project:
```
python3 manage.py runserver
```

If ever by any chance you want to test some stuff via admin dashbord you may run the following command:
```
python3 manage.py createsuperuser
```
and when your local server is running you may goto ```127.0.0.1/admin```

@Authors
- <a href="http://github.com/Sjk-Lacoste">Tshepo Mohlatlole</a>
- <a href="">Sbonelo Mkhize</a>
- <a href="">Letlhoholo Lefatlhe</a>
- <a href="">Masai Mahapa</a>