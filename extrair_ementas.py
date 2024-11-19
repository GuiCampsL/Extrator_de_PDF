import re
import os
from PyPDF2 import PdfReader

def extract_ementas(pdf_path):
    # Verifica se o arquivo existe
    if not os.path.exists(pdf_path):
        print(f"Arquivo não encontrado: {pdf_path}")
        return

    try:
        # Ler o conteúdo do PDF
        reader = PdfReader(pdf_path)
        text = "".join(page.extract_text() for page in reader.pages)

        if not text:
            print("Nenhum texto extraído do PDF. Verifique o formato do arquivo.")
            return

        # Diagnóstico: Salvar o texto completo extraído em um arquivo para visualização
        with open("texto_extraido.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print("Texto extraído salvo em 'texto_extraido.txt'.")

        # Ajustar a regex para procurar pela disciplina e a ementa
        pattern = r"([A-ZÁ-Ú\s]+)\nEmenta:\s*(.+?)(?=\n|Bibliografia|$)"
        matches = re.findall(pattern, text, re.DOTALL)

        if not matches:
            print("Nenhuma disciplina ou ementa encontrada com o padrão fornecido.")
            return
    

    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

# Caminho do PDF
pdf_path = r"C:\Users\SAMSUNG\OneDrive\Área de Trabalho\pdc_ementa.pdf"
extract_ementas(pdf_path)
