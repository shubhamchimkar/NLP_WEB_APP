import os
import nlpcloud


# Config: prefer environment variables for secrets and settings.
NLPCLOUD_MODEL = os.environ.get("NLPCLOUD_MODEL", "finetuned-llama-3-70b")
NLPCLOUD_API_KEY = os.environ.get("NLPCLOUD_API_KEY", "8e9d8d39750741fda214144051263737b9e64801")
NLPCLOUD_GPU = os.environ.get("NLPCLOUD_GPU", "True").lower() in ("1", "true", "yes")


# Initialize client
client = nlpcloud.Client(NLPCLOUD_MODEL, NLPCLOUD_API_KEY, gpu=NLPCLOUD_GPU)


def ner(text, searched_entity=None):
		"""Call nlpcloud.entities on `text`.

		Args:
			text: input text string
			searched_entity: optional string to pass as searched_entity param

		Returns:
			The raw result from client.entities (usually a dict)
		"""
		if searched_entity:
				return client.entities(text, searched_entity=searched_entity)
		return client.entities(text)


def config_info():
		"""Return current runtime config useful for debugging/testing (not secrets)."""
		return {
				"model": NLPCLOUD_MODEL,
				"api_key_provided": bool(os.environ.get("NLPCLOUD_API_KEY")),
				"gpu": NLPCLOUD_GPU,
		}


def sentiment(text, target=None):
	"""Run sentiment analysis via nlpcloud.

	Args:
	  text: input text
	  target: optional target string

	Returns:
	  Raw API response
	"""
	if target:
		return client.sentiment(text, target=target)
	return client.sentiment(text)


def summarization(text, size="small"):
	"""Run summarization via nlpcloud.

	size: optional size string forwarded to client.summarization
	"""
	return client.summarization(text, size=size)
