short-url-shortener
===================

A simple URL shortener using Django and fbootstrap for CSS.


How to RUN:
-----------
 1. On **UNIX-like** OSes.
    - Download the fbootstrap project from https://github.com/ckrack/fbootstrapp/downloads
    
    - Make a folder named 'static' in short folder and unpack the fbootsrap project files in it.
    
    - Set these fields according to your database in **settings.py**.

                 'ENGINE': 'django.db.backends.',
                 'NAME': '',
                 'USER': '',
                 'PASSWORD': ''
    - Run **python manage.py syncdb**
    - Run **python manage.py runserver**

 2. On Windows.
    - Download the fbootstrap project from https://github.com/ckrack/fbootstrapp/downloads
    - Make a folder named 'static' in short folder and unpack the fbootsrap project files in it.
    - Set these fields according to your database in **settings.py**.

                 'ENGINE': 'django.db.backends.',
                 'NAME': '',
                 'USER': '',
                 'PASSWORD': ''
    - Edit the STATICFILES_DIRS and TEMPLATE_DIRS in **settings.py** and use something like
      'C:/Documents and Settings/User/Desktop/short/templates'  #Notice forward slashes
    - Run **python manage.py syncdb**
    - Run **python manage.py runserver**