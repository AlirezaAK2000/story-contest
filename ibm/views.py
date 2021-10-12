from blog.models import Post , Comment
from django.shortcuts import redirect , render
from django.contrib import messages
from .tools import convert_text_to_speech

import logging

logger = logging.getLogger(__name__)

def convert_post_to_speech(request , pk):
    if request.method == "GET":
        print("going to serve")
        try:
            post = Post.objects.get(pk=pk)
            if post.audio_path == None:
                generated_url = convert_text_to_speech(post.content , post.pk , post.title)
                
                post.audio_path = generated_url
                
                post.save()
                
                return redirect(generated_url)
            
            else:
                
                return redirect(post.audio_path)
                
            
        except Post.DoesNotExist:
            messages.error(request ,"specified post does n't exist")
            return render(request , "home.html")
        except Exception as ex:
            messages.error(request ,str(ex))
            return render(request , "post_detail.html" , {'object':post})
            
            
def convert_comment_to_speech(request , pk):
    if request.method == "GET":
        print("going to serve")
        try:
            comment = Comment.objects.get(pk=pk)
            if comment.audio_path == None:
                generated_url = convert_text_to_speech(comment.content , comment.pk , 'comment')
                
                comment.audio_path = generated_url
                
                comment.save()
                
                return redirect(generated_url)
            
            else:
                
                return redirect(comment.audio_path)
                
            
        except comment.DoesNotExist:
            messages.error(request ,"specified comment does n't exist")
            return render(request , "home.html")
        except Exception as ex:
            messages.error(request ,str(ex))
            return render(request , "post_detail.html" , {'object':comment.post})
            
            
