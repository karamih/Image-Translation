# Image-Translation
<em>
consider you travel to another country! and you don't understand their language, when you are walking in the street you see a billboard, an advertisement, some text on the wall but you can't understand what they are.  even you want to figure out addresses; now you can simply take a picture of those and then this script gives you translated texts :D
</em>
<hr>

### How does it like?

<img src="statics/ocr.jpg" width=500, height=500>

#### How does it work:<br>

*  OCR: Detecting text with easyocr
*  TRANSLATION: translating using langchain and chat-gpt


<img src="statics/output_ocr.jpg" width=500, height=500>

### One more:

<img src="statics/ocr2.jpg" width=500, height=500>
<img src="statics/output_ocr2.jpg" width=500, height=500>

<hr>

### How to use?

*  In `translation.py` file you can modify langchain for e.g you could change ouput tranlation language. only need to change prompt variable just with change the language.

<br>

*  Eacyocr does two things, first detect texts and then recognize them. for detect and recognize your initial language, add your language to `reader` variable in `ocr.py` file.

<br>

*  remember to create a `.env` file and push your openai api key in that. `OPENAI_API_KEY = "API KEY"`

<br>

That's it, now run the `ocr.py` file and give your image to the function.


