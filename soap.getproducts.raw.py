import requests

# you should get these 3 variables from your Intersolve contact
soapuser = "xxxxxx"
soappass = "xxxxxx"
soappo = "123456" # must be string in this case


headers = {'content-type': 'text/xml'}
body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:loc="http://localhost:8011">
   <soapenv:Header>
      <loc:authentication>
         <username>"""+soapuser+"""</username>
         <password>"""+soappass+"""</password>
      </loc:authentication>
   </soapenv:Header>
   <soapenv:Body>
      <loc:GetProducts>
         <!--Optional:-->
         <CustomerNr>8</CustomerNr>
         <!--Optional:-->
         <HomePage>false</HomePage>
         <!--Optional:-->
         <ProductOwnerNr>"""+soappo+"""</ProductOwnerNr>
         <!--Optional:-->
         <!--Optional:-->
         <CustomerType>BusinessCustomer</CustomerType>
      </loc:GetProducts>
   </soapenv:Body>
</soapenv:Envelope>"""

response = requests.post("https://trade.intersolve.nl/ws/WS_WebShop",data=body,headers=headers)
print(response.text)