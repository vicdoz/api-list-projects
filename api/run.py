#!/usr/bin/env python
from api.app import app

app.run(host='127.0.0.1', port=8081, debug=True, use_reloader=False)