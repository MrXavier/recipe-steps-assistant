import os
import openai
import textwrap
import openai_utils
import numpy as np
import json

openai.api_key = os.environ["OPENAI_API_KEY"]
model_gpt_4="gpt-4" 
model_gpt_3_5_turbo="gpt-3.5-turbo" 
CONTEXT, QUESTION = 'context', 'question'

def validate_input(input):
  if all(prop in input and input[prop] is not None for prop in [CONTEXT, QUESTION]):
    resp = {
      CONTEXT: input[CONTEXT],
      QUESTION: input[QUESTION]
    }
    return resp
  else:
    msg = "Cannot parse service's payload to json format."
    print(f" -- Error: {msg} Payload: {input}")
    raise Exception(msg)

def handle_completion(payload):
  payload = validate_input(payload)
  prompt = f'''De acordo com o contexto: "{payload[CONTEXT]}". Responda a sequinte pergunta: "{payload[QUESTION]}".'''
  print(" -- prompt: ", prompt)
  response = openai.ChatCompletion.create(
      model=model_gpt_3_5_turbo,
      messages=[
          {"role": "system", "content": "Você é um advogado e especialista em Direito e na legislação Brasileira. Responda a pergunta de acordo com as leis e regras da constituição Brasileira."},
          {"role": "user", "content": prompt}
      ],
      temperature=0.8,
      n=1,
      max_tokens=1000
  )
  print(" --- response: ", response)
  return response.choices[0].message.content
