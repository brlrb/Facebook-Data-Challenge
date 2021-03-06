# -*- coding: utf-8 -*-
"""Facebook Data Challenge 2019

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ltkEm_0O707Fc2kMbOPYjedvK3DDLXL2

##**Facebook Data Challenge 2019**

---

**Challenge:** *Hi, my name is Zuck! I am thinking about opening a business in San Francisco. Problem is, I'm not very familiar with San Francisco so I need a data analyst to help me. In particular, I want help understanding the business landscape in San Francisco, what type of business I should open, and the most optimal location.*

**Solution:** We will be using ([Yelp Open Datasets](https://www.yelp.com/dataset/)) to base our recommendations to Zuck.
"""

# init
# Facebook Data Challenge 2019


# Import required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Yelp Open Datasets(local drive because of License Restriction)
# Download your copy via https://www.yelp.com/dataset/challenge
# From the RAW DATA:
# Step 1: Extract the businesses that is only in SF
# Step 2: Extract the review/ratings that matches business_id in SF

from google.colab import files
uploaded = files.upload()

# Import the uplaoded dataset into the dataframe 
import io
import json


tweets = []
for line in open('business.json', 'r'):
    print(line)