# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 2024
@author: whattheheckisthis
"""
# pip install fastapi uvicorn

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Query
from typing import Optional

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://47.72.156.147:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://47.72.156.147:8000/welcome?name=whattheheckisthis
@app.get('/welcome')
def get_name(name: Optional[str] = Query("whattheheckisthis", description="Specify your name")):
    if name:
        return {'Welcome To My Workspace': name}
    else:
        return {'message': 'Welcome To My Workspace'}

# 5. Run the API with uvicorn
#    Will run on http://47.72.156.147:8000
if __name__ == '__main__':
    uvicorn.run(app, host='47.72.156.147', port=8000)
# uvicorn whattheheckisthis:app --reload
