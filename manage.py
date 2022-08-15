from distutils.log import debug
import uvicorn
from app import app, configuration
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    if configuration.DEBUG == True:
        # For local
        uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True, debug=True)
    else:
        # For production
        uvicorn.run(app, host='0.0.0.0', port=8000, debug=False)