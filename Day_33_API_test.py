#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:59:39 2022

@author: user0
"""
import requests

response = requests.get(url="https://www.ebi.ac.uk/pdbe/api/pdb/entry/experiment/1cbs")
print(response) # this is a response code
# 404 doesn't exist
#1XX menas hold on 
#200 means success
#300 means you don't have permission to get, so, go away
#500 there is some other issue, the server is down or the website down.
print(response.status_code)
#if response.status_code != 200:
#    print("error")
# report the error
#if response.status_code == 404:
#    raise Exception ("That resource doesn't exist")
#elif response.status_code == 401:
#    raise Exception ("You are not authorised to access this data.")
response.raise_for_status()    
data=response.json()
print(data)



