import clip
import torch
from PIL import Image


class CLIP:
    """A handler to communicate with CLIP model"""

    def __init__(self, type_="ViT-B/32"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(name=type_, device=self.device)

    def classify(self, image: Image.Image, classes: list[str]):
        """Classify given images amongst given classes"""
        images = self.preprocess(image).unsqueeze(0).to(self.device)
        tokenized_classes = clip.tokenize(texts=classes).to(self.device)

        with torch.no_grad():
            logits_per_image, _ = self.model(images, tokenized_classes)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()

        result = []
        for prob in probs:
            score_dict = {name: round(score, 3)
                          for name, score in zip(classes, prob)}
            result.append(score_dict)
        return result
