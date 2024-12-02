# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ryll6ARjoL2PyFeyzJr-HcypvRT259i
"""

!pip install requests beautifulsoup4 openai langchain-openai

import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(['script', 'style']):
      script_or_style.decompose()
    texto = soup.get_text(separator= ' ')
    linhas = (line.strip() for line in texto.splitlines())
    parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
    texto_limpo = '\n'.join(part for part in parts if part)
    return texto_limpo
  else:
    print(f"Failed to fetch the URL. Status code {response.status_code}")
    return None


  text = soup.get_text()
  return text

extract_text_from_url('https://www.dio.me/articles/como-aprendi-kotlin-em-3-passos-simples')

from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint="",
    api_key="",
    api_version="",
    deployment_name="",
    max_retries=0
)

def translate_article(text, lang):
  messages = [
      ("system" , "Voce atua como tradutor de textos")
      ("user" , f"Trazdura o {text} para o idioma {lang} e responda em markdown")
  ]

  response = client.ivoke(messages)
  print(response.content)
  return response.content

translate_article("Hello World", "portugues")

