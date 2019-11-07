# Influence Flowers

## Dataset

- Link: [Public link TBD](Currently the git repo with datasets, sqlitedb is available on the team gdrive)

## Environment Setup

### Deployment Environment Setup

- Download the dataset files from the above section and put these in the same folder structure in the github repo. Do not copy the .git folder while merging.
- Make sure you have the latest version of Python3, pip installed
- Set python environment if using conda  
➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) source /Users/sanadell/anaconda3/bin/activate  
(base) ➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) conda activate base  
- Install Django using  
(base) ➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) pip install Django
- Run server using 
(base) ➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) python manage.py runserver 127.0.0.1:8001
- The server should start on port 8001 and can be accessed by opening [http://127.0.0.1:8001/](http://127.0.0.1:8001/)

### Development Environment Setup

- Install Visual Studio Code
- Open the github repo folder and select debug icon
- Select the Debug icon on the Activity bar and select Python: Django configuration
- You can see other configurations which allow you to launch the Chrome Browser or [Browser Preview extension](https://marketplace.visualstudio.com/items?itemName=auchenberg.vscode-browser-preview) for debugging
- The default port is 8001 and can be changed in the launch.json file under .vscode folder

### Development Commands
```
Import CSV into sqlite
(base) ➜  Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) ✗ sqlite3 db.sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite> .mode csv
sqlite> .import /Users/sanadell/test.csv Test
```
