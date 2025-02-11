# Exemplo de uso da  biblioteca Docling


## Descrição

A biblioteca Docling processa varios tipos de documentos (PDF,DOCX,XLSX,PPTX, MArkdown,AsciiDoc,HTML,XHTML,PNG,JPEG,TIFF,BMP) e exporta para HTML,Markdown,JSON,Text e Doctags 

[GitHub](https://github.com/DS4SD/docling)



## Dependências

Este projeto utiliza as seguintes bibliotecas Python:


* **Docling:** O Docling simplifica o processamento de documentos, analisando diversos formatos — incluindo compreensão avançada de PDF — e fornecendo integrações perfeitas com o ecossistema de IA de geração.


  * 🗂️ **Análise de vários formatos de documentos** , incluindo PDF, DOCX, XLSX, HTML, imagens e muito mais
  * 📑 **Compreensão avançada de PDF**, incluindo layout de página, ordem de leitura, estrutura de tabela, código, fórmulas, classificação de imagem e muito mais
  * 🧬 **Formato de representação DoclingDocument** unificado e expressivo
  * ↪️ **Vários formatos e opções de exportação**, incluindo Markdown, HTML e JSON sem perdas
  * 🔒 **Capacidades de execução local** para dados sensíveis e ambientes com air gap
  * 🤖 **Integrações plug-and-play**, incluindo LangChain, LlamaIndex, Crew AI e Haystack para IA de agente
  * 🔍 **Amplo suporte OCR** para PDFs e imagens digitalizados
  * 💻 **CLI** simples e conveniente

  Você pode encontrar mais informações sobre o Docling em: [https://ds4sd.github.io/docling/](https://ds4sd.github.io/docling/)



## Observação sobre a Instalação

Conforme detalhado na seção [Instalação](#instalação), este projeto utiliza o `pipenv` para o gerenciamento de dependências. Ao executar o comando `pipenv install` (ou `pipenv install --dev` se desejar as dependências de desenvolvimento), o `pipenv` irá **automaticamente instalar o Docling e quaisquer outras dependências listadas no arquivo `Pipfile`** dentro do ambiente virtual do projeto. Portanto, você **não precisa** instalar essas bibliotecas manualmente.

Caso não esteja utilizando o `pipenv`, será necessário instalar as dependências manualmente usando o `pip`, por exemplo:

```bash
pip install docling
```
No entanto, **recomenda-se fortemente o uso do `pipenv`** para garantir a consistência do ambiente e evitar conflitos de dependências com outros projetos Python em seu sistema.

### Instalar o `pipenv`

Para instalar o pipenv basta utilizar o comando:

```bash

pip install pipenv

```

-----

## Instalação

Este projeto utiliza o `pipenv` para gerenciar as dependências. 

Siga os passos abaixo para instalar e configurar o ambiente de desenvolvimento:

### Pré-requisitos

*   Python 3.x (recomendado Python 3.11 ou superior)
*   `pip`
*   `pipenv`

### Passos para Instalação

1.  **Clone o repositório:**

    ```bash
    git clone git@github.com:natanfiuza/analise_dados.git
    cd analise_dados
    ```

2.  **Instale as dependências usando o `pipenv`:**

    ```bash
    pipenv install
    ```
    Este comando irá criar um ambiente virtual e instalar todas as dependências listadas no arquivo `Pipfile`.

3.  **Ative o ambiente virtual**

    ```bash
    pipenv shell
    ```
    Isso ativará o ambiente virtual criado pelo `pipenv`. Todos os comandos a seguir devem ser executados dentro desse ambiente.

4.  **(Opcional) Instale as dependências de desenvolvimento**

    Se você precisar das dependências de desenvolvimento (por exemplo, para testes), use:

    ```bash
    pipenv install --dev
    ```

**Pronto!** Agora você já pode executar o programa (veja a seção "[Utilização](#utilização)" para mais detalhes).


## Utilização

Execute o script `simple_conversion.py` para transformar `assets\doc\manual_frascati_2015_PT_BR.pdf` para `assets\doc\manual_frascati_2015_PT_BR.md`

## Contribuições e Contato

Contribuições para este projeto são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou ideias para expandir a simulação, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* neste repositório.

Para qualquer dúvida, sugestão ou feedback, entre em contato:

**Natan Fiuza**

**Email:** [contato@natanfiuza.dev.br](mailto:contato@natanfiuza.dev.br)

Espero que este projeto seja útil e inspirador para estudantes e entusiastas da programação Python!