from first.ibm import text_to_speech
from blog.models import Post
from django.conf import settings
from first.arvan import s3_client , bucket
from django.shortcuts import redirect 

import logging

logger = logging.getLogger(__name__)

def convert_text_to_speech(request , pk):
    if request.method == "GET":
        print("going to serve")
        # try:
        post = Post.objects.get(pk=pk)
        print(f"post {post.title} is valid")
        if post.audio_path == None:
            
            print(f"post {post.title} has no audio file")
            
            audio = text_to_speech.synthesize(
                post.content,
                voice=settings.READER_VOICE,
                accept='audio/wav'        
            ).get_result().content
            
            print("audio file recieved")

            object_name = f"{post.title}_{post.pk}.wav"
            
            
            bucket.put_object(
                ACL = 'public-read',
                Body = audio,
                Key = object_name
            )
            
            print(f"audio file saved into the storage")
            
            
            generated_url = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': settings.ARVAN_STORAGE_BUCKET_NAME,
                    'Key': object_name
                }
            )
            
            post.audio_path = generated_url
            
            post.save()
            
            return redirect(generated_url)
        
        else:
            
            return redirect(post.audio_path)
            
            
        # except Post.DoesNotExist:
        #     messages.error(request ,"specified post does n't exist")
        #     return render(request , "home.html")
        # except Exception as ex:
        #     messages.error(request ,str(ex))
        #     return render(request , "post_detail.html" , {'object':post})
            