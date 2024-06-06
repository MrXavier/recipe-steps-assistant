import os
import chromadb


# import chromadb.utils.embedding_functions as embedding_functions
# api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)
# openai_ef = embedding_functions.OpenAIEmbeddingFunction(
#   api_key=api_key
# )


chroma_client = chromadb.PersistentClient(path="./chroma_db_steps")

collection = chroma_client.get_or_create_collection(name="steps_collection")

steps_title = [
  "Roast potatoes",
  "Cook bacon"
]
steps_desc = [
    "Quarter potatoes. Cut any larger potatoes into 1-inch pieces. Add potatoes and 1 tbsp (2 tbsp) oil to a parchment-lined baking sheet. Season with BBQ Seasoning, salt and pepper, then toss to coat. Roast in the middle of the oven, flipping halfway through, until tender and golden-brown, 22-25 min.",
    "Meanwhile, arrange bacon strips in a single layer on another parchment-lined baking sheet. Roast bacon in the top of the oven, flipping halfway through, until golden-brown and cooked through, 12-14 min. Using tongs, transfer bacon to a paper towel-lined plate. Carefully transfer bacon fat to a small heat-proof bowl. Reserve."
]
img_links = [
    "https://mvdataappstorageeunlprod.blob.core.windows.net/medialibrary-43a72c4d7b634ea6b37b2e2cfd6450f5-r/5bac400a092148e3abaed10aca0afeef/5bac400a092148e3abaed10aca0afeef/Large/HF210324_R28_W19_CA_RS153279-1_MB_Step1_low.jpg?sv=2017-04-17&sr=b&si=201904101622&sig=HEuwZf%2F63aFz%2BDpNv87a9M6Vm8zuPY%2BjVhdPw15h%2Fuk%3D&st=1849-12-13T07%3A24%3A49Z&se=2033-06-19T05%3A03%3A09Z",
    "https://mvdataappstorageeunlprod.blob.core.windows.net/medialibrary-43a72c4d7b634ea6b37b2e2cfd6450f5-r/8336803d45404568b2018d76b6dae67e/8336803d45404568b2018d76b6dae67e/Large/HF210914_R33_W44_CA_RP0406-2_MB_Step2_REMOVE%202%20SLICES%20OF%20BACON_low.jpg?sv=2017-04-17&sr=b&si=201904101622&sig=AudW9sjo0pt8tTYeN3d6VVXPTDzgeKjvuiLbnAjj%2Bj0%3D&st=1940-10-16T06%3A40%3A58Z&se=2033-01-01T05%3A23%3A16Z"
]

steps_combined = [f"{title} - {desc}" for title, desc in zip(steps_title, steps_desc)]
links_metadata = [{"imageLink": img_link} for img_link in img_links]
ids = [f"id{i+1}" for i in range(len(steps_title))]

collection.add(
    documents=steps_combined,
    metadatas=links_metadata,
    ids=ids
)
while True:
  query = input("Enter your query: ")
  if query == "quit":
    break
  results = collection.query(
      # query_texts=["This is a query is for hawaii fruits"], # Chroma will embed this for you
      # query_texts=["This is a document about pinapple"],
      # query_texts=["The moon is the only natural satellite of the Earth."], 
      # query_texts=["Slice potatoes and put into oven."], 
      query_texts=[query], 
      n_results=2 # how many results to return
  )
  print(results)
  links = [metadata[0]['imageLink'] for metadata in results['metadatas']]
  print(links)
