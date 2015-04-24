"""Start Virtual Env"""
& $Env:WORKON_HOME\DAD\Scripts\activate.ps1
cd $Env:PROJECT_HOME\DAD
git clone git@github.com:usma-it394/ay15-2-project-team-i-4.git
django-admin startproject --template=http://github.com/usma-it394/it394_project_template/archive/master.zip <tracker>
cd <tracker>
fix_name.ps1 -name "tracker"
"""OR"""
cd usma-it394/ay15-2-project-team-i-4
"""Install Packages"""
pip install -r requirements.txt
pip install csvimport.app.csvImportConf
Sync Database"""
python manage.py syncdb
"""Deploy to Heroku"""
heroku login
heroku create
git remote –v
git push heroku master
"""Create Database Structure"""
heroku run:detached python manage.py migrate
