activate_this = '/var/www/venv/bin/activate_this.py'
exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))

import sys
sys.path.insert(0, "/var/www/tempblog")
from tempblog import app as application


