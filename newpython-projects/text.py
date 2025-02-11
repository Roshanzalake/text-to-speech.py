from text_to_speech import save

text = input("Enter the text you want to convert to speech: ")
language = "en"  
output_file = "speech.mp3"  

save(text, language, file=output_file)
