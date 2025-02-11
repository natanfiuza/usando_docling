

import os

def alterar_extensao(caminho_arquivo, nova_extensao):
  """
  Altera a extensão de um arquivo.

  Args:
    caminho_arquivo: O caminho para o arquivo original.
    nova_extensao: A nova extensão do arquivo (sem o ponto).

  Returns:
    O caminho para o arquivo com a nova extensão.
  """
  nome_base, extensao_antiga = os.path.splitext(caminho_arquivo)
  novo_caminho = nome_base + "." + nova_extensao
  return novo_caminho

def salvar_arquivo(caminho_arquivo, texto):
  """
  Salva um texto em um arquivo.

  Args:
    caminho_arquivo: O caminho para o arquivo onde o texto será salvo.
    texto: O texto a ser salvo no arquivo.
  """

  try:
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
      arquivo.write(texto)
    print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
  except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")