import torch
from torchvision import transforms, models
from PIL import Image
import json

class Sorter:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])


        with open("class_names.json", "r") as f:
            self.class_names = json.load(f)


        self.model = models.resnet18(pretrained=False)
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, len(self.class_names))
        self.model.load_state_dict(torch.load("assets/image_sorter_model.pth", map_location=self.device))
        self.model.to(self.device)
        self.model.eval()


    def predict(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            output = self.model(image)
            _, pred = torch.max(output, 1)
            return self.class_names[pred.item()]

