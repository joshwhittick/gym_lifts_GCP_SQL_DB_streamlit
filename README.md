# gym_lifts_SQL_DB_streamlit_version

**Development of https://github.com/joshwhittick/gym_lifting_tracking as a web app using https://streamlit.io to host and https://cloud.google.com/sql/docs/mysql for a MySQL DB (although am on $300 trial so will also fail like Heroku version but just wanted that proof of concept)**

files here are for the purpose of launcing app on streamlit and not for running on personal machine with MySQL DB

**notes on files included:**

**DB_SQL_STREAMLIT_FUNCTIONS.py**
deffinition of functions required for the streamlit web app 

**Lifting_DB_Main_Page.py**
main page for streamlit web app launching

**pages/Insert to Database.py**
build streamlit page defining widgets to input data and calling the necessary functions to write to the DB

**pages/Interogate Database.py**
build streamlit page defining widgets where user can query DB data, calls necessary functions to connect to DB and express the results as text and graphs 

this could be improved to be more "valuable" i.e. more relevant graphs or other output formats like .csv files blah blah blah

**requirements.txt**
for streamlit to "pip install" the appropriate packages
