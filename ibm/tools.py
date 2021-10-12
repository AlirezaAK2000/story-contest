from first.ibm import text_to_speech
from blog.models import Post
from django.conf import settings
from first.arvan import s3_client , bucket
from django.shortcuts import redirect , render
from django.contrib import messages




def convert_text_to_speech(text , pk , title):
    audio = text_to_speech.synthesize(
        text,
        voice=settings.READER_VOICE,
        accept='audio/wav'        
    ).get_result().content
    

    object_name = f"{title}_{pk}.wav"
    
    
    bucket.put_object(
        ACL = 'public-read',
        Body = audio,
        Key = object_name
    )
    
    
    
    generated_url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': settings.ARVAN_STORAGE_BUCKET_NAME,
            'Key': object_name
        }
    )
    
    return generated_url
        
    
            
