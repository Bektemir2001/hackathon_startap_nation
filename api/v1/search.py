from flask import Blueprint, request
from ai.speech_recognition import SpeechRecognition
import time
speech_recognition = SpeechRecognition()
from controllers.search_product import ElasticSearch
e = ElasticSearch()
bp = Blueprint('search', __name__, url_prefix='/search')

@bp.post('')
def search_voice():
    print("start")
    if 'audio' not in request.files:
        return "Файл 'audio' не был отправлен."
    audio_file = request.files['audio']
    print(audio_file)
    if audio_file.filename == '':
        return "Не выбран файл."
    save_path = 'audios/'+str(time.time())+'.wav'
    try:
        audio_file.save(save_path)
        print(save_path)
        return {"result": speech_recognition.recognition(save_path)}
    except Exception as e:
        return f"Произошла ошибка при сохранении файла: {str(e)}"

@bp.get('/product')
def search_txt():
    search = request.args['search']
    return {"res": e.search_product(search)}

