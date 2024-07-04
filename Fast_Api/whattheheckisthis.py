Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> whattheheckisthis.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'whattheheckisthis' is not defined
>>> # -*- coding: utf-8 -*-
>>> """
... Created on Mon Jul 04 2024
... @author: whattheheckisthis
... """
'\nCreated on Mon Jul 04 2024\n@author: whattheheckisthis\n'
>>> # pip install fastapi uvicorn
>>>
>>> # 1. Library imports
>>> import uvicorn
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'uvicorn'
>>> from fastapi import FastAPI, Query
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'fastapi'
>>> from typing import Optional
>>>
>>> # 2. Create the app object
>>> app = FastAPI()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FastAPI' is not defined
>>>
>>> # 3. Index route, opens automatically on http://47.72.156.147:8000
>>> @app.get('/')
... def index():
...     return {'message': 'Hello, World'}
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>> # 4. Route with a single parameter, returns the parameter within a message
>>> #    Located at: http://47.72.156.147:8000/welcome?name=whattheheckisthis
>>> @app.get('/welcome')
... def get_name(name: Optional[str] = Query("whattheheckisthis", description="Specify your name")):
...     if name:
...         return {'Welcome To My Workspace': name}
...     else:
...         return {'message': 'Welcome To My Workspace'}
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>> # 5. Run the API with uvicorn
>>> #    Will run on http://47.72.156.147:8000
>>> if __name__ == '__main__':
...     uvicorn.run(app, host='47.72.156.147', port=8000)
... # 5. Run the API with uvicorn
