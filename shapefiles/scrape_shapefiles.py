import zipfile
import urllib
import os
import urllib.request

def url_creator(county):
    return "https://sos.iowa.gov/shapefiles/County%20Precincts/{county}.zip".format(county=county)
    
counties = ["Adair", "Adams", "Allamakee", "Appanoose", "Aubudon", "Benton", "Black Hawk", "Boone", "Bremer", "Buchanan", "Buena Vista", "Butler", "Calhoun", "Carroll", "Cass", "Cedar", "Cerro Gordo", "Cherokee", "Chickasaw", "Clarke", "Clay", "Clayton", "Clinton", "Crawford", "Dallas", "Davis", "Decatur", "Delaware", "Des Moines", "Dickinson", "Dubuque", "Emmet", "Fayette", "Floyd", "Franklin", "Fremont", "Greene", "Grundy", "Guthrie", "Hamilton", "Hancock", "Hardin", "Harrison", "Henry", "Howard 2014", "Howard", "Humboldt", "Ida", "Iowa", "Jackson", "Jasper", "Jefferson", "Johnson", "Jones", "Keokuk", "Kossuth", "Lee", "Linn final", "Louisa", "Lucas", "Lyon", "Madison", "Mahaska", "Marion", "Marshall", "Mills", "Mitchell", "Monona", "Monroe", "Montgomery", "Muscatine", "O'Brien", "Osceola", "Page 2013 Precincts", "Page", "Palo Alto", "Plymouth", "Pocahontas (2)", "Polk", "Pottawattamie", "Poweshiek", "Ringgold", "Sac", "Scott", "Shelby", "Sioux", "Story", "Tama", "Taylor", "Union", "Van Buren", "Wapello", "Warren precincts", "Washington", "Wayne", "Webster", "Winnebago", "Winneshiek", "Woodbury", "Worth", "Wright"]
 
# for county in counties:
#     baseurl = url_creator(county)
    
#     opener = urllib.request.build_opener()
#     opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
#     urllib.request.install_opener(opener)
#     local_filename, headers = urllib.request.urlretrieve(url = baseurl)
#     zip_ref = zipfile.ZipFile(file = local_filename, mode = "r")
#     zip_ref.extractall(path = os.getcwd())     #os.getcwd() directs to current working directory
#     zip_ref.close()
    
    
# import urllib.request

# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
# urllib.request.install_opener(opener)
# urllib.request.urlretrieve(url = baseurl)



import urllib.request
url = url_creator(counties[0])
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()