"""Template robot with Python."""
import os

from RPA.Browser import Selenium
from RPA.PDF import PDF
from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import File
from RPA.HTTP import HTTP
from RPA.Excel.Files import Files

local_d = os.getcwd() + "/"
browser = Selenium()

def logIn():
    browser.open_available_browser("https://robotsparebinindustries.com/")
    browser.wait_until_element_is_enabled("id:username")
    browser.input_text("username","maria")
    #Verificar por que browser.input_password no funciona (verificar si tiene realación con las vaults)
    browser.input_text("password","thoushallnotpass")
    browser.click_button("Log in")
    browser.wait_until_element_is_enabled("id:firstname")

def descargaExcel():
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/SalesData.xlsx",overwrite=True)

def llenoCampos(tabla):
    browser.input_text("id:firstname",tabla["First Name"])
    browser.input_text("id:lastname",tabla["Last Name"])
    browser.input_text("id:salesresult",tabla["Sales"])
    browser.select_from_list_by_value("id:salestarget",str(tabla["Sales Target"]))
    browser.click_button("Submit")

def extraigoData():
    excel = Files()
    excel.open_workbook("SalesData.xlsx")
    tabla_excel = excel.read_worksheet_as_table(header=True)
    excel.close_workbook()
    for fila in tabla_excel:
        llenoCampos(fila)

def resultados():
    browser.screenshot("css:div.sales-summary",local_d+"/output/sales_summary.png")
    browser.capture_page_screenshot(local_d+"/output/captura_web.png")


def salgo():
    browser.click_button("Log out")
    browser.close_browser()


if __name__ == "__main__":
    logIn()
    #descargaExcel()
    extraigoData()
    resultados()
    salgo()
