import requests
import io
from fastapi import HTTPException
from config import config

async def get_prediction(image_bytes: bytes):
    try:
        print('Roboflow is connected')
        url = config.ROBOFLOW_URL
        files = {
            'file': ('image.jpg', io.BytesIO(image_bytes), 'image/jpg')
        }
        response = requests.post(url, files=files)

        print(response.text)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail='Error')


        # return {'answer': response.json()} # if u need certain fields than do this -->
        return {
            'inference_id': response.json()['inference_id'],
            'result_time': response.json()['time'],
            'predictions': [
            {
                'class': pred['class'],
                'confidence': round(pred['confidence'] * 100, 1),
            }
            for pred in response.json().get('predictions', [])
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {e}')
