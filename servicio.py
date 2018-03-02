import json
from tkinter import filedialog
from watson_developer_cloud import VisualRecognitionV3

def conexion():
	visual_recognition = VisualRecognitionV3(
	    '2016-05-20',
	    api_key='{API KEY}')

	file = filedialog.askopenfilename(filetypes =( ("JPEG","*.jpeg"),("JPG","*.jpg") ,("All files", "*.*")))
	

	with open(file , 'rb') as images_file:
	    classes = visual_recognition.classify(
	        images_file)

	print(json.dumps(classes, indent=2))


	d = classes["images"][0]["classifiers"][0]["classes"][0]["class"]
	d1 = classes["images"][0]["classifiers"][0]["classes"][0]["score"]

	return ("It is more likely to be :	{} \nwith this certainty:	{}".format(d,d1))


def clasificar():
	visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='{API KEY}')


	f1 = filedialog.askopenfilename(filetypes =( ("JPEG","*.jpeg"),("All files","*.*") ))

	f2 = filedialog.askopenfilename(filetypes =( ("JPEG","*.jpeg"),("All files","*.*") ))


	with open(f1, 'rb') as deportivo, open(
        f2, 'rb') as normal:
	    model = visual_recognition.create_classifier(
	        'autos',
	        deportivo_positive_examples=deportivo,
	        normal_positive_examples=normal)
	print(json.dumps(model, indent=2))


