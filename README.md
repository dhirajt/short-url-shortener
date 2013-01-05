short-url-shortener
===================

A simple URL shortener using Django and fbootstrap for CSS.


How to RUN:
-----------

- Download the fbootstrap project from https://github.com/ckrack/fbootstrapp/archive/master.zip
- Make a folder named 'static' in short folder and add the following files from the zipped file. <br />
  js,lib folders and css files bootstrap.css,bootstrap.min.css
- Set these fields according to your database in **settings.py**.                                                                                                                      
        
           'ENGINE': 'django.db.backends.',
           'NAME': '',
           'USER': '',
           'PASSWORD': ''
- Run **python manage.py syncdb**
- Run **python manage.py runserver**

