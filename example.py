from gradio_client import Client

client = Client("https://internettrashh-sentiment-analysis.hf.space/--replicas/88zjj/")
result = client.predict(
		"he is a bad person!",	# str  in 'input_text' Textbox component
		api_name="/predict"
)
print(result)