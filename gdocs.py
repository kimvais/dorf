from pickle import load
import gdata
import gdata.docs.service

__author__ = 'kimmo.parviainen'

USERNAME = "kimvais@gmail.com"
__PASSWORD = "" # Add here if the AUTH token goes stale

def upload(docname):
    service = gdata.docs.service.DocsService()
    service.ssl = True
    #service.ClientLogin(USERNAME, __PASSWORD)
    with open("authtoken.txt") as tokenfile:
        service.SetClientLoginToken(tokenfile.readlines()[0])
    ms = gdata.MediaSource(file_path=docname+".csv", content_type=gdata.docs.service.SUPPORTED_FILETYPES['CSV'])
    service.Upload(ms, docname)
