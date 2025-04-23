from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Detection

class DetectionModelTest(TestCase):
    def test_string_representation(self):
        detection = Detection(prediction={"class_1": 0.1, "class_2": 0.9})
        self.assertEqual(str(detection), f"Detection {detection.id}")

class DetectionViewTest(TestCase):
    def test_detection_page(self):
        response = self.client.get(reverse('detection'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Upload an image")

    def test_image_upload(self):
        with open('test_image.jpg', 'rb') as img:
            image = SimpleUploadedFile(img.name, img.read(), content_type='image/jpeg')
            response = self.client.post(reverse('detection'), {'image': image})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Prediction scores")
