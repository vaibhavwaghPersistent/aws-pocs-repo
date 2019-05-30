import objectpath
import json

def lambda_handler(event, context):
    with open('/opt/data/aws-regions.json', 'r') as f:
        regionsObject = json.load(f)
    
    obTree = objectpath.Tree(regionsObject)
    print("Inside objectpath-data-demo code")
    sydneyObject = obTree.execute('$.sydney')
    print('value of result obj =  $.sydney')

    return sydneyObject
