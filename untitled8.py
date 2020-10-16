# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:37:20 2020

@author: lenovo
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/lenovo/Documents/ps_salary_proj/chromedriver"

df = gs.get_jobs('Physical therapist', 30, False, path, 15)

df