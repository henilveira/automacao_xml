import xml.etree.cElementTree as ET
import openpyxl

tree = ET.parse('arquivo.xml')
root = tree.getroot()

workbook_empregados = openpyxl.Workbook()
sheet_empregados = workbook_empregados.active

identificadores = ['ID','Nome','Posição','Departamento','Salário']
sheet_empregados.append(identificadores)

for empregados in root.findall('.//employee'):
    id = empregados.find('id').text
    nome = empregados.find('name').text
    posicao = empregados.find('position').text
    departamento = empregados.find('department').text
    salario = empregados.find('salary').text
    dados_xml = [id,nome,posicao,departamento,salario]
    sheet_empregados.append(dados_xml)

workbook_empregados.save('xml_empregados.xlsx')