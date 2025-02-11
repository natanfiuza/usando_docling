from docling.document_converter import DocumentConverter
from functions import *

source = "./assets/doc/manual_frascati_2015_PT_BR.pdf"
converter = DocumentConverter()
result = converter.convert(source)

content = result.document.export_to_markdown()

salvar_arquivo(alterar_extensao(source,'md'),content)
