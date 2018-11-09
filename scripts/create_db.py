#!/usr/bin/env python

import os
import sys

sys.path.append(os.getcwd())

from app.db import engine
from app.db.models import Base


Base.metadata.create_all(engine)
