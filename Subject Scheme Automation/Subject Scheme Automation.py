#!/usr/bin/env python
# coding: utf-8

# # Log in to the Subject Scheme Confluence Page

# In[1]:


import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[2]:


headers = {"user-agent": 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/83.0.4103.116 safari/537.36'}

login_data = {
    'os_username' : 'akumar5',
    'os_password' : 'Decem@2020',
    'login' : 'Log in'
    }

with requests.Session() as requests:
    url = 'https://confluence-lvs.prod.mcafee.com/pages/viewpage.action?spaceKey=IDCS&title=Subject+scheme+tracking'
    source = requests.get(url, headers=headers)
    soup = BeautifulSoup(source.content, 'lxml')
    login_data['SAMLRequest'] = soup.find('input', attrs={'name': 'SAMLRequest'})['value']
    source = requests.post(url, data=login_data, headers=headers)
    
    new_source = requests.get('https://confluence-lvs.prod.mcafee.com/pages/viewpage.action?spaceKey=IDCS&title=Subject+scheme+tracking').text
    soup = BeautifulSoup(new_source, 'lxml')
    print(soup)
    


# # Splitting the Product Names and Product Keys into Separate Lists

# In[3]:


rows = []

table = soup.find("table")

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    for item in td:
        row = item.text
        rows.append(row)
        


# In[4]:


product_names = []
product_keys = []

table = soup.find("table")

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [item.text for item in td]
    col1 = row[0:1]
    col2 = row[1:2]
    
    col1 = ''.join(col1)
    col2 = ''.join(col2)
    
    product_names.append(col1)
    product_keys.append(col2)


# In[5]:


prod_dict = dict(zip(product_keys, product_names))


# # Building the XML document

# In[6]:


import xml.etree.ElementTree as ET
from xml.dom import minidom


# In[7]:


# with open('arun.ditamap') as f:
#     lines = f.readlines()
    
# with open('test.ditamap', 'a+') as file:
#     contents = file.writelines(lines)


# In[10]:


subjectdef1 = ET.SubElement(subjectHead, "subjectdef", keys=k, navtitle=v)
subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)


# In[11]:


root = ET.Element("subjectScheme")
subjectHead = ET.SubElement(root, "subjectHead", navtitle='Product', id='product-head')
subjectHead2 = ET.SubElement(root, "subjectHead", navtitle='Category', id='cat-head')
subjectHead3 = ET.SubElement(root, "subjectHead", navtitle='Landing', id='landing-head', outputclass='landing')

# Product facets
for k,v in prod_dict.items():
      
    if re.findall(r'\D{5,}', v) and 'Cloud Threat Detection' not in v and 'Device Control' not in v and 'System Information Reporter' not in v and 'Saas Web Protection Service' not in v and 'SAAS-WPS' not in v and 'Security as a Service' not in v:
        # MACC
        if re.findall(r'Application and Change Control', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MACC \d.\d.\D', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'Application Control$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^Change Control', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        # DLP
        elif re.findall(r'^MVISION$', v): 
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'On-premises', v): 
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MV-DLPE|MV-DLPMac|MV-DLPD|MV-DLPP|MV-DLPM', v): 
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'DLPE \d\d.\d.\D', v): 
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'DLPMac \d\d.\d.\D', v): 
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'DLPD \d\d.\d.\D', v): 
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'DLPP \d\d.\d.\D', v): 
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'DLPM \d\d.\d.\D', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        # ENS
        elif re.findall(r'ENSS \d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'ENS-\D{2,} \d\d.\d.\D', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'ENS-\D{2,} \d\d.\d.\d', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'ENS-\D{2,} \d\d.\d.\d', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        # MEPM, ENSS, ePO-CB    
        elif re.findall(r'MEPM \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'ENSS \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'EPO-CB \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'EPO-CB \d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'HIPS \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'HIPS \d.\d.\d{1,}', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-MNE$', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MOVE \d.\d{1,}.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MOVE \d.\d{1,}.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-CB$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-EPT$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-EDR$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-EPO$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-INS$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-UCE$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^SAAS-EMA$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^SAAS-EMP$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'SAAS-OM \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'SAAS-OM \d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'NTBA \d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MSDW \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MSDW \d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MSME \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MSME \d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MSMS \d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^MV-TIE$', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VNSP \d{1,}.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VNSP \d{1,}.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VSEL \d{1,}.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VSEL \d{1,}.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VSES \d{1,}.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VSE-CLS \d{1,}.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'VSEM \d{1,}.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MVM-D \d{1,}.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MVM-D \d{1,}.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^WGCS-UCE$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^EPO-CLD$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
        else:
            subjectdef1 = ET.SubElement(subjectHead, "subjectdef", keys=k, navtitle=v)
             
    # DLP
    elif re.findall(r'DLP \d\d.\d.\D', v):
        subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
    # ENS
    elif re.findall(r'ENS \d\d.\d.\D', v):
        subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    # ENS    
    elif re.findall(r'ENS \d\d.\d.\d{1,}', v):
        subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'ESM \d\d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'ESM \d\d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'EPO-CLD', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'^INV$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'^MV-M$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'NSP \d\d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'NSP \d\d.\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'MWG \d\d.\d.\D', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'^PBC$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
    elif re.findall(r'^WGCS$', v):
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)
            
    
    elif re.findall(r'\D{2,} \d.\d.\D', v):
        
        if re.findall(r'^AC \d.\d.\D', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^CC \d.\d.\D', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'EPO \d.\d\d.\d', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MNE \d.\d.\D', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'TIE \d.\d.\D', v):
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)
        else:
            subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)

    elif re.findall(r'\D{2,} \d.\d.\d', v):
        
        if re.findall(r'^AC \d.\d.\d', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'^CC \d.\d.\d', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'MNE \d.\d.\d', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        elif re.findall(r'TIE \d.\d.\d', v):
            subjectdef4 = ET.SubElement(subjectdef3, "subjectdef", keys=k, navtitle=v)
        else:
            subjectdef3 = ET.SubElement(subjectdef2, "subjectdef", keys=k, navtitle=v)

# Categorical facets
cat_dict = {'cat-hardware':'Hardware', 'cat-installation':'Installation and Getting Started',
            'cat-integration':'Integration', 'cat-migration':'Migration', 
           'cat-product':'Product Usage', 'cat-reference':'Reference', 
           'cat-release-notes':'Release-Notes'}
for k,v in cat_dict.items():
    subjectdef1 = ET.SubElement(subjectHead2, "subjectdef", keys=k, navtitle=v)

# Landing facets
land_dict = {'land-endpoint-security-v10-7-x':'ENS 10.7.x', 'land-endpoint-security-v10-6-x':'ENS 10.6.x',
            'land-endpoint-security-v10-6-0':'ENS 10.6.0', 'land-endpoint-security-v10-5-x':'ENS 10.5.x', 
           'land-endpoint-security-v10-5-0':'ENS 10.5.0', 'land-epo-v5-10-x':'EPO 5.10.x', 
           'land-epo-v5-9-x':'EPO 5.9.x'}
for k,v in land_dict.items():
    if re.findall(r'\D{3,} \d{1,}.\d{1,}.\D', v):
        subjectdef1 = ET.SubElement(subjectHead3, "subjectdef", keys=k, navtitle=v)
        
    else:
        subjectdef2 = ET.SubElement(subjectdef1, "subjectdef", keys=k, navtitle=v)


xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("automated_subject_scheme.ditamap", "w") as f:
    f.write(xmlstr)


# In[13]:


with open('header_schema.ditamap') as f:
    schema = f.readlines()
    
with open('subject-scheme.ditamap', 'w') as f:
    contents = f.writelines(schema)
    
with open('automated_subject_scheme.ditamap') as f:
    f.seek(24)
    subject_scheme = f.readlines()
    
with open('subject-scheme.ditamap', 'a+') as f:
    final = f.writelines(subject_scheme) 


# In[ ]:




