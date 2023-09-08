import requests
from Job import Job
from bs4 import BeautifulSoup

#URL we will be scraping
URL = "https://realpython.github.io/fake-jobs/"

#html of the page
page = requests.get(URL)

#Parse the page using beautiful soup
soup = BeautifulSoup(page.content, "html.parser")

#find the container with the job postings only
results = soup.find(id="ResultsContainer")

#get the contents of each job card
job_elements = results.find_all("div", class_="card-content")

#Intialize job list to store results
Jobs = []

#Loop through each card to the title, company, and location of each job
for job_element in job_elements:
    #Get elements
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    #Get Text of elements
    jobtitle = title_element.text
    company = company_element.text
    location = location_element.text

    #Trim White Space
    jobtitle = jobtitle.strip()
    company  = company.strip()
    location = location.strip()

    #Create Job Variable
    jobinstance = Job(jobtitle, company, location)
    
    #Add elements to job list
    Jobs.append(jobinstance)

#print results
for job in Jobs:
    print("Job Title: " + job.jobtitle)
    print("Job Location: " + job.joblocation)
    print("Company: " + job.company)
    print("\n")
