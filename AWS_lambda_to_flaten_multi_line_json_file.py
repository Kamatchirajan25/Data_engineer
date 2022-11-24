from __future__ import print_function

import boto3

import xml.etree.ElementTree as ET

import csv

import getopt

import sys

import urllib

import uuid

import os

import json

from xml.dom import minidom



 

print ("===loading funtion===")

 


s3 = boto3.client('s3')
 

def lambda_handler(event, context):

    source_bucket = 'kamatchibucket'
    
    s3_folder='athena_test/'

   

    # The logic to find the new updated file names and other details

   
    file_key = 'sample_data.json'
    

 

    # Read the latest uploaded XML file and convert it to CSV.

    # The logic is specific to what XML File is expect

    # The below logic of conversion from XML to CSV needs to be use case specfic and should be changed

    data = s3.get_object(Bucket=source_bucket, Key=f"{s3_folder}{file_key}")

    contents = data['Body'].read()
    
    
    def flatten_json(y):
        out = {}
 
        def flatten(x, name=''):
            # If the Nested key-value
            # pair is of dict type
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
                    # If the Nested key-value
                    # pair is of list type
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x
 
        flatten(y)
        return out
    flaten_output=flatten_json(contents)
    with open('/tmp/flaten_output.json', 'w') as f:
        f.write(str(flaten_output))
    
    with open('/tmp/flaten_output.json', 'rb') as cp:
        s3.upload_fileobj(cp, source_bucket, 'athena_test/flaten_output.json')
        print("== copy completed==")

    

    
 



   

    