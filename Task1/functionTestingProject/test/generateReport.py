import os

#put allure report(.json) of temp into report and change to .html
os.system("allure generate ./temp -o ./reports --clean")