from io import FileIO
from first.ibm import text_to_speech
from blog.models import Post
from django.http import FileResponse
from django.conf import settings
from django.contrib import messages

def convert_text_to_speech(request , pk):
    if request.method == "GET":
        try:
            post = Post.objects.get(pk=pk)
            
            audio = text_to_speech.synthesize(
                post.content,
                voice=settings.READER_VOICE,
                accept='audio/wav'        
            ).get_result().content
            
            with open(f"{post.title}.wav" , 'wb') as file:
                file.write(audio)
                response = FileResponse(audio)
                return response
            
        except Post.DoesNotExist:
            messages.error("specified post does n't exist")
        except Exception as ex:
            messages.error(ex.message)