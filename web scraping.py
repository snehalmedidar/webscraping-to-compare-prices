#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import smtplib
from bs4 import BeautifulSoup #For web scraping


# In[2]:


amazon_product_url ="https://www.amazon.in/Plum-Luminence-Simply-Supple-Cleansing/dp/B08423CWXC/ref=sr_1_1_sspa?crid=2XPML9B0BDLOP&keywords=plum+cleansing+balm&qid=1660912570&sprefix=plum+clea%2Caps%2C274&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSVkzQk9FRklDUUM4JmVuY3J5cHRlZElkPUEwMjA2NTA2MUI0RUdXVFBTUDNQRyZlbmNyeXB0ZWRBZElkPUEwNzI4NzMxMlNGODRZS1NNRUFSRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
nykka_product_url="https://www.nykaa.com/plum-e-luminence-simply-supple-cleansing-balm/p/683146?ptype=product&skuId=683146&utm_content=ads&utm_source=GooglePaid&utm_medium=PLA&utm_campaign=performancemaxskin&gclid=CjwKCAjw6fyXBhBgEiwAhhiZst95C0Udfw4B36miwCFhPLRjQ8SacrewLbd-CcKYA9UQTaup3TGBOhoC_ZwQAvD_BwE"
netmeds_product_url="https://www.netmeds.com/non-prescriptions/plum-e-luminence-simply-supple-cleansing-balm-90-gm?source_attribution=ADW-CPC-Pmax_beauty_purchase&utm_source=ADW-CPC-Pmax_beauty_purchase&utm_medium=CPC&utm_campaign=ADW-CPC-Pmax_beauty_purchase&gclid=CjwKCAjw6fyXBhBgEiwAhhiZsrmGjSUvm0i1tMd4jcZS8dXTy7tdyU4wyGGKf0xG0BX1doh7uDds_BoC7GEQAvD_BwE"
headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"} 


# In[3]:


page = requests.get(url=amazon_product_url, headers=headers) 
soup = BeautifulSoup(page.content,'lxml') 
print(soup.prettify())


# In[4]:


title = soup.find(id = 'productTitle')


# In[5]:


text = title.get_text() # Will get text from html tags
product_title = text.strip() # Removing special characters like \n (newline)
print(product_title )


# In[6]:


price = soup.find('span', class_='a-price-whole')
price = price.get_text() # Will get text from html tags
amazon_product_price = price.strip() # Removing special characters like \n (newline)
print(amazon_product_price )


# In[7]:


page = requests.get(url=nykka_product_url, headers=headers) 
soup = BeautifulSoup(page.content,'lxml') 
print(soup.prettify())


# In[8]:


title = soup.find('h1', class_ = 'css-1gc4x7i')
text = title.get_text() # Will get text from html tags
product_title = text.strip() # Removing special characters like \n (newline)
print(product_title )


# In[9]:


price = soup.find('span', class_='css-1jczs19')
price = price.get_text() # Will get text from html tags
nykka_product_price = price.strip() 
nykka_product_price = nykka_product_price[1:]# Removing special characters like \n (newline)
print(nykka_product_price)


# In[10]:


page = requests.get(url=netmeds_product_url, headers=headers) 
soup = BeautifulSoup(page.content,'lxml') 
print(soup.prettify())


# In[11]:


title = soup.find('h1', class_ = 'black-txt')
text = title.get_text() # Will get text from html tags
product_title = text.strip() # Removing special characters like \n (newline)
print(product_title )


# In[12]:


price = soup.find('span', class_='final-price')
price = price.get_text() # Will get text from html tags
netmeds_product_price = price.strip() # Removing special characters like \n (newline)
print(netmeds_product_price )


# In[13]:


import pickle
def storeData():
   # initializing data to be stored in db
    amazon = {'key' : 'amazon', 'product_name' : 'Plum cleansing balm', 'price' : amazon_product_price}
    nykka = {'key' : 'onbuy', 'product_name' : 'Plum cleansing balm', 'price' : nykka_product_price}
    netmeds = {'key' : 'wex', 'product_name' : 'Plum cleansing balm', 'price' : netmeds_product_price}

   # database
    db = {}
    db['amazon'] = amazon
    db['nykka'] = nykka
    db['netmeds'] = netmeds

    
   # Its important to use binary mode
    dbfile = open('price_data', 'ab')
    
   # source, destination
    pickle.dump(db, dbfile)                    
    dbfile.close()


# In[14]:


#Loading Stored Data
def read_data():
    dbfile = open('price_data', 'rb')    
    sb_store = pickle.load(dbfile)
    for items in db_store:
        print(items, ' :: ', db[items])
    dbfile.close()


# In[15]:


amazon_product_price = float(amazon_product_price)
nykka_product_price  = float(nykka_product_price)
nedmeds_product_price = float(netmeds_product_price[14:])


# In[16]:


min_price = min (amazon_product_price,nykka_product_price, nedmeds_product_price )


# In[21]:


if min_price == amazon_product_price:
    comp= "amazon"
    URL = amazon_product_url
if min_price == nykka_product_price:
    comp="nykka"
    URL = nykka_product_url
if min_price == netmeds_product_price:
    comp="netmeds"
    URL = netmeds_product_url


# In[22]:


print("Please check:" + " " + comp + "  " + "click here" +" "+ URL)


# In[18]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
comp =["amazon", "nykka","netmeds"]
price=[amazon_product_price,nykka_product_price, nedmeds_product_price]
ax.bar(comp,price)
plt.show()


# In[ ]:


def send_mail():
    try:
        mail = EmailMessage()
        mail['from'] = 'trackmyvaccine37@gmail.com'
        mail['subject'] = "subject"
        mail['to'] = 'snehal.medidar@gmail.com'
        mail.set_content(xyz)
        
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT')
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ctx) as server:
            server.login('trackmyvaccine37@gmail.com','tgbmlofefkosjifl')
            server.send_message(mail)
        return True
    except Exception as e:
        print(e)
        return False


# In[ ]:


def xyz():
    body = f''' Hi,
    "Please click here {url}".format(url = URL)"
    '''
    send_mail("prices", body, email)
    return HttpResponse()


# In[ ]:


send_mail()

