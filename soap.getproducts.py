from zeep import Client, Settings
from zeep.exceptions import Fault
from zeep import xsd

# you should get these 3 variables from your Intersolve contact
soapuser = "xxxxxx"
soappass = "xxxxxx"
soappo = 123456

request_data = {
    'HomePage': 'false',
    'ProductOwnerNr': soappo,
}

header = xsd.ComplexType([
    xsd.Element('authentication',
                    xsd.ComplexType([
                        xsd.Element('username',xsd.String()),
                        xsd.Element('password',xsd.String()),
                    ])
                )
                 ])

header_value = header(authentication={'username':soapuser,'password':soappass})
settings = Settings(strict=False, xml_huge_tree=True)
client = Client(wsdl='live_intersolve_wsdl.xml', settings=settings)
products = client.service.GetProducts(**request_data, _soapheaders=[header_value])
print(products)