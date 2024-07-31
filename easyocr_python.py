import easyocr
reader = easyocr.Reader(['en'],gpu=True) # this needs to run only once to load the model into memory

result = reader.readtext('image.jpg',detail=0,paragraph=True,
                         contrast_ths=0.1,
                         adjust_contrast=0.5,
                         add_margin=0.1,
                         width_ths=0.7,
                         height_ths=0.7)

print(result)