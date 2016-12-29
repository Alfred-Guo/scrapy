# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
from spd import Spd
import PyPDF2
import traceback
import os

class Springer(Spd):
    def __init__(self):
        super(Springer,self).__init__('springer','springer')
    
    def getUrls(self):
        url='http://www.springer.com/cn/book/%s'
        #return [(url%i[1],{'file':i[0]}) for i in self.scan() if i]
        return [('http://www.springer.com/cn/book/9781461471370',{'file':'te'})]
    
    def scan(self):
        paths=[r'C:\Users\Alfred\Desktop\book']
        for path in paths:
            for p,ds,fs in os.walk(path):
                for f in fs:
                    if os.path.splitext(f)[1]=='.pdf':
                        f=os.path.join(p,f)
                        yield (f,self.getIsbn(f))
                        
    def getIsbn(self,f):
        fobj=open(f,'rb')
        try:
            reader=PyPDF2.PdfFileReader(fobj)
            for i in range(min(10,reader.numPages)):
                p=reader.getPage(i)
                s=p.extractText()
                n=s.find('ISBN-13')
                if n!=-1:
                    s=s[n+7:].replace(':','').replace('-','').replace(' ','')
                    fobj.close()
                    return s[:13]
                            
                n=s.find('ISBN')
                if n!=-1:
                    s=s[n+4:].replace(':','').replace('-','').replace(' ','')
                    if s[:13].isdigit():
                        fobj.close()
                        return s[:13]
                    else:
                        fobj.close()
                        return s[:10]
                
        except:
            fobj.close()
            traceback.print_exc()
            return ''
                
if __name__=='__main__':
    springer=Springer()
    springer.start_crawl()