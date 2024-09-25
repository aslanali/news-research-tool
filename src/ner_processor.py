from transformers import pipeline

class NERProcessor:
    def __init__(self, model_name="dbmdz/bert-large-cased-finetuned-conll03-english"):
        """Initialize the NER processor with a pre-trained model."""
        self.ner_pipeline = pipeline("ner", model=model_name, grouped_entities=True)
        # A simple list of known celebrities (you can expand this as needed)
        self.celebrity_names = {"elon musk", "giorgia meloni", "donald trump", "barack obama", "beyonce", "taylor swift"}

    def extract_entities(self, text):
        """Extract named entities from the given text."""
        return self.ner_pipeline(text)
    
    def format_entities(self, entities):
        """Format and filter out duplicate entities, showing only celebrities."""
        seen_entities = set()
        formatted_entities = []
        
        for entity in entities:
            entity_key = (entity["entity_group"], entity["word"].strip().lower())  # Normalize for comparison
            # Check if the entity is a person and in the celebrity list
            if entity["entity_group"] == "PER" and entity_key[1] in self.celebrity_names:
                if entity_key not in seen_entities:
                    seen_entities.add(entity_key)
                    entity_info = {
                        "entity": entity["entity_group"],
                        "word": entity["word"],
                        "score": round(entity["score"], 3)
                    }
                    formatted_entities.append(entity_info)
        
        return formatted_entities
