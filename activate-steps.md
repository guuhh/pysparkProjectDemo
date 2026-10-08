#To activate venve on python context
brew install python@3.11
/opt/homebrew/bin/python3.11 -m venv .venv
source .venv/bin/activate

#To deactivate:
deactivate

#accessos to the Kaggle API token
mkdir (within the project) data
chmode 777 pysparkProject/data
kaggle datasets download -d catherinerasgaitis/mxmh-survey-results -p ~/pysparkProject/data --unzip
chmod 755 .kaggle/ kaggle_token/

#Executions mode

python kaggle_demo.py
spark-submit kaggle_demo.py