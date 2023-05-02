import requests
import csv

url = 'https://data.usajobs.gov/api/Search?Keyword=Cyber&&ResultsPerPage=500'
headers = {'User-Agent': "lrudroju@gmu.edu", 'accept': "application/json", 'Host': "data.usajobs.gov", 'Authorization-Key': "cZG1yuFZ+Y/f5T+GnAcOn+P2n8kwVqBpx4U20ho5rDA="}

# Get JSON Data
json_data = requests.get(url, headers=headers).json()
items = json_data["SearchResult"]["SearchResultItems"]

with open('usajob.csv', 'w') as csv_file:
    fieldnames = ["Title", "Location", "Organization", "Department", "QualificationSummary"]
    writer = csv.writer(csv_file)
    writer.writerow(fieldnames)
    for item in items:
        title = item["MatchedObjectDescriptor"]["PositionTitle"]
        location = item["MatchedObjectDescriptor"]["PositionLocationDisplay"]
        organization = item["MatchedObjectDescriptor"]["OrganizationName"]
        department = item["MatchedObjectDescriptor"]["DepartmentName"]
        qualificationSummary = item["MatchedObjectDescriptor"]["QualificationSummary"]
        writer.writerow([title, location, organization, department, qualificationSummary])


        