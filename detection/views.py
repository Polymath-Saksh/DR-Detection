from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from transformers import pipeline

# Load the Diabetic Retinopathy model from Hugging Face
model = pipeline("image-classification", model="sakshamkr1/ResNet50-APTOS-DR")

def detection_view(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # Make prediction using the model
        predictions = model(uploaded_file_url)
        max_prediction = max(predictions, key=lambda x: x['score'])

        return render(request, 'detection/detection.html', {
            'uploaded_file_url': uploaded_file_url,
            'predictions': predictions,
            'max_prediction': max_prediction
        })
    return render(request, 'detection/detection.html')
