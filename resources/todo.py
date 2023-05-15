from flask_restful import Resource
from llama_index import SimpleDirectoryReader, ServiceContext, GPTVectorStoreIndex, LLMPredictor, load_index_from_storage, StorageContext
from langchain.chat_models import ChatOpenAI
import sys
import os

os.environ["OPENAI_API_KEY"] = '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'


class Todo(Resource):

  def construct_index(directory_path):
    num_outputs = 512

    modelo = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'))

    pdf = SimpleDirectoryReader(directory_path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=modelo)
    index = GPTVectorStoreIndex.from_documents(pdf, service_context = service_context)

    index.storage_context.persist(persist_dir="datos")
    return "Creado: ", 200
  

  def chatbot(input_text):
    storage_context = StorageContext.from_defaults(persist_dir="datos")
    index = load_index_from_storage(storage_context)
    pregunta = input_text + "Responde en español"
    response = index.as_query_engine().query(pregunta)
    return response.response
