
from django.shortcuts import render
from django.http import JsonResponse
from .utils import find_best_match, preprocess_text
import google.generativeai as genai
from django.conf import settings  # Import Django settings

# Initialize Gemini (Make sure to configure API Key in settings.py)
genai.configure(api_key=settings.GOOGLE_API_KEY)  # Access API key from settings
print(f"Gemini API Key: {settings.GOOGLE_API_KEY}") 
model = genai.GenerativeModel('gemini-pro')

def chat_view(request):
    return render(request, 'chatbot/chat.html')

def gemini_answer(user_query):
    try:
        prompt = f"Answer the following question:\n{user_query}"
        response = model.generate_content(prompt)
        gemini_response = response.text #Gets the text from the Gemini response
        return JsonResponse({'response': gemini_response})
    except Exception as e:
        return JsonResponse({'response': f"Error generating response using Gemini: {e}"})

def get_response(request):
    if request.method == 'POST':
        user_query = request.POST.get('user_query', '')
        if not user_query:
            return JsonResponse({'response': "Please ask a question."})

        if "segment" in user_query.lower():
            cdp_base_url = 'https://segment.com/docs/'
            response_text = find_best_match(user_query, cdp_base_url)
            if response_text:
                return JsonResponse({'response': response_text})
            else:
                return gemini_answer(user_query)
        elif "mparticle" in user_query.lower():
            cdp_base_url = 'https://docs.mparticle.com/'
            response_text = find_best_match(user_query, cdp_base_url)
            if response_text:
                return JsonResponse({'response': response_text})
            else:
                return gemini_answer(user_query)
        elif "lytics" in user_query.lower():
            cdp_base_url = 'https://docs.lytics.com/'
            response_text = find_best_match(user_query, cdp_base_url)
            if response_text:
                return JsonResponse({'response': response_text})
            else:
                return gemini_answer(user_query)
        elif "zeotap" in user_query.lower():
            cdp_base_url = 'https://docs.zeotap.com/'
            response_text = find_best_match(user_query, cdp_base_url)
            if response_text:
                return JsonResponse({'response': response_text})
            else:
                return gemini_answer(user_query)
        else:
             try:
                 #Call Gemini Model and respond
                 prompt = f"Answer the following question:\n{user_query}"
                 response = model.generate_content(prompt)
                 gemini_response = response.text #Gets the text from the Gemini response
                 return JsonResponse({'response': gemini_response})
             except Exception as e:
                 return JsonResponse({'response': f"Error generating response using Gemini: {e}"})
    else:
        return JsonResponse({'response': "Invalid request"})
    
