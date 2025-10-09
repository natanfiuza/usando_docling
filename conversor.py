import argparse
import os
from docling.document_converter import DocumentConverter
from functions import alterar_extensao, salvar_arquivo

def converter_pdf_para_markdown(caminho_arquivo_entrada, caminho_arquivo_saida=None):
    """
    Converte um arquivo PDF para o formato Markdown usando a biblioteca docling.

    Args:
        caminho_arquivo_entrada (str): O caminho para o arquivo PDF de entrada.
        caminho_arquivo_saida (str, optional): O caminho para o arquivo Markdown de saída.
                                            Se não for fornecido, o nome do arquivo de entrada
                                            será usado com a extensão .md.
    """
    # Verifica se o arquivo de entrada realmente existe antes de prosseguir
    if not os.path.exists(caminho_arquivo_entrada):
        print(f"Erro: O arquivo de entrada não foi encontrado em '{caminho_arquivo_entrada}'")
        return

    print(f"Iniciando a conversão do arquivo: {caminho_arquivo_entrada}...")

    try:
        # 1. Instancia o conversor da biblioteca docling
        converter = DocumentConverter()

        # 2. Executa a conversão do arquivo de origem
        resultado = converter.convert(caminho_arquivo_entrada)

        # 3. Exporta o conteúdo convertido para o formato Markdown
        conteudo_markdown = resultado.document.export_to_markdown()

        # 4. Determina o caminho do arquivo de saída
        if caminho_arquivo_saida:
            # Se o usuário especificou um nome de saída, usa esse nome
            caminho_final_saida = caminho_arquivo_saida
        else:
            # Se não, usa a função para alterar a extensão do arquivo original
            caminho_final_saida = alterar_extensao(caminho_arquivo_entrada, 'md')

        # 5. Usa a sua função para salvar o conteúdo no arquivo de destino
        salvar_arquivo(caminho_final_saida, conteudo_markdown)

    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a conversão: {e}")

if __name__ == "__main__":
    # Configuração do parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(
        description="Converte um arquivo PDF para o formato Markdown usando a biblioteca docling."
    )

    # Argumento 1: Posição obrigatória para o arquivo de entrada
    parser.add_argument(
        "caminho_pdf",
        type=str,
        help="O caminho completo para o arquivo PDF que será convertido."
    )

    # Argumento 2: Opcional (-o ou --output) para o arquivo de saída
    parser.add_argument(
        "-o", "--output",
        dest="caminho_saida",
        type=str,
        help="O nome (e caminho) opcional para o arquivo de saída .md. Se não for fornecido, será usado o nome do arquivo de entrada com a extensão .md."
    )

    # Analisa os argumentos fornecidos pelo usuário
    args = parser.parse_args()

    # Chama a função principal com os argumentos capturados
    converter_pdf_para_markdown(args.caminho_pdf, args.caminho_saida)