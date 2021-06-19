from ftplib import FTP

def uploadToSdlDev():

    ftp = FTP('ftp-kc-us-west-2.sdlproducts.com')
    ftp.login(user='ftpmcafdevaws1', passwd='Qs8Kah#F&DdG')
    ftp.cwd('/App/Utilities/DITA-OT/DITA-OT244/plugins/com.zoominsoftware.docs.mcafee/resources')

    stagingSubjectScheme = "subject-scheme-stg.ditamap"
    prodSubjectScheme = "subject-scheme-prod.ditamap"

    localpath1 = open('c:\\! w o r k\\!systems work\\subject scheme updates\\subject-scheme-stg.ditamap', 'rb')
    localpath2 = open('c:\\! w o r k\\!systems work\\subject scheme updates\\subject-scheme-prod.ditamap', 'rb')

    ftp.storlines('stor ' + stagingSubjectScheme, localpath1)
    ftp.storlines('stor ' + prodSubjectScheme, localpath2)
    ftp.retrlines('list')

    ftp.quit()

def uploadToSdlProd():

    ftp = FTP('ftp-kc-us-west-2.sdlproducts.com')
    ftp.login(user='ftpmcafprodaws1', passwd='7e!%(kSGXM)X')
    ftp.cwd('SchemaMap')

    stagingSubjectScheme = "subject-scheme-stg.ditamap"
    prodSubjectScheme = "subject-scheme-prod.ditamap"

    localpath1 = open('c:\\! w o r k\\!systems work\\subject scheme updates\\subject-scheme-stg.ditamap', 'rb')
    localpath2 = open('c:\\! w o r k\\!systems work\\subject scheme updates\\subject-scheme-prod.ditamap', 'rb')

    ftp.storlines('stor ' + stagingSubjectScheme, localpath1)
    ftp.storlines('stor ' + prodSubjectScheme, localpath2)
    ftp.retrlines('list')

    ftp.quit()

uploadToSdlDev()
uploadToSdlProd()