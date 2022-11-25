import xml.etree.ElementTree as etree
import lxml.etree
import csv

tree = etree.parse('DLTINS_20210117_01of01.xml')
root = tree.getroot()

NS = 'urn:iso:std:iso:20022:tech:xsd:auth.036.001.02'
header = ('Id', 'FullNm','ClssfctnTp','CmmdtyDerivInd','NtnlCcy','Issr')

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    rows = []
    a=root.iter('{%s}TermntdRcrd' % NS)
    b=root.iter('{%s}FinInstrmGnlAttrbts' % NS)
    for FinInstrmGnlAttrbts,TermntdRcrd in zip(b,a):
        Id = FinInstrmGnlAttrbts.find('{%s}Id' % NS).text
        FullNm = FinInstrmGnlAttrbts.find('{%s}FullNm' % NS).text
        ClssfctnTp = FinInstrmGnlAttrbts.find('{%s}ClssfctnTp' % NS).text
        CmmdtyDerivInd = FinInstrmGnlAttrbts.find('{%s}CmmdtyDerivInd' % NS).text
        NtnlCcy = FinInstrmGnlAttrbts.find('{%s}NtnlCcy' % NS).text
        Issr = TermntdRcrd.find('{%s}Issr' % NS).text
        print(Id, FullNm, ClssfctnTp, CmmdtyDerivInd, NtnlCcy,Issr)
        row = Id, FullNm, ClssfctnTp, CmmdtyDerivInd, NtnlCcy,Issr
        writer.writerow(row)

