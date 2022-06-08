from googlesearch import search
import xlrd
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter

name=[]
link=[]
facebook=[]
instragram=[]
archivo = "./input.xls"
wb = xlrd.open_workbook(archivo)
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    cell = sheet.cell_value(i,0)
    google_query_linkedin = cell + " linkedin"
    google_query_facebook= cell + " facebook"
    google_query_instagram= cell + " instragram"
    for i in range(5):
        name.append(cell)
    for i in search(google_query_linkedin,stop=1,lang="cl",country="CL"):
        link.append(i)
        print(i)
    for i in search(google_query_facebook,stop=1,lang="cl",country="CL"):
        facebook.append(i)
        print(i)
    for i in search(google_query_instagram,stop=1,lang="cl",country="CL"):
        instragram.append(i)
        print(i)
data = {"name": name,"link": link,"instragram":instragram,"facebook":facebook}
df = pd.DataFrame(data)
witer = pd.ExcelWriter("./output.xlsx",engine="xlsxwriter")
df.to_excel(witer,sheet_name="Hoja1",index=False)    
witer.save()
print("OK")

