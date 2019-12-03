# Influence Flowers

## Dataset

- Link: https://drive.google.com/open?id=1nK0kXxA4OIdPX5A87awZCWNt53Xi7p9N
> **NOTE:** Download this file into the root folder of the project

## Environment Setup

### Deployed Environment

- http://euler.la.asu.edu:8002/

### Testing

#### Some tested flowers

- http://euler.la.asu.edu:8002/moviesflower/?genre_list=Adventure,Action
- http://euler.la.asu.edu:8002/loadairbnbflower?city_name=Austin


### Deployment Environment Setup

- Download the dataset files from the above section and put it under the root folder. The project setup should look like this
```
-- Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay  
  |__ .vscode  
  |__ flowerapp  
  |__ .gitignore  
  |__ db.sqlite3  
  |__ manage.py  
  |__ README.md  
```
- Make sure you have the latest version of python3 installed in the deployment environment 
- Install Sympy using  
```
(base) ➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) pip3 install sympy
```
- Install Django version 2.2.6 using  
```
(base) ➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) pip3 install Django==2.2.6  
```
> **NOTE:** The project doesn't work with latest version of Django since the configuration for serving staticfiles has changed since this project was developed

- Run server using  
```
(base) ➜ Influence-Flowers-Sai-Akshit-Sandeep-Raghul-Akshay git:(master) python manage.py runserver 127.0.0.1:8001
```
- The server should start on port 8001 and can be accessed by opening [http://127.0.0.1:8001/](http://127.0.0.1:8001/) in the browser. The flower is tested primarily on Google Chrome browser.

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
