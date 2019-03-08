#!/usr/bin/env python

import os
import sys

sys.path.append(os.getcwd())

from footprints.db import engine
from footprints.db.models import Base


Base.metadata.create_all(engine)
