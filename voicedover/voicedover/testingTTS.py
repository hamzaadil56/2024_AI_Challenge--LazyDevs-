from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    
def textToSpeech(text:str='Please say something.'):
    inputs = processor(text=text, return_tensors="pt")

        # load xvector containing speaker's voice characteristics from a dataset
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

    sf.write("speech1.wav", speech.numpy(), samplerate=16000)
    return 'speech1.wav'
  
  
text = '''
Hi. How are you. Here is a list of todos that you wanted me to give to you. 
You wanna buy eggs, some chocolates, and you gotta clean your car in the evening.
'''
textToSpeech(text)