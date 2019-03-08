#!/usr/bin/env python

import os
import sys

sys.path.append(os.getcwd())

from footprints.db import session
from footprints.db.models import Category, Product
