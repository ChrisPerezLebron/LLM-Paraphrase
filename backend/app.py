from flask import Flask, jsonify, render_template, request, Response
import json
import ollama
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

ollama.pull('llama3.2')

# display homepage
@app.route("/")
def main_page():
    return render_template("index.html")

# return rephrased content (no streaming)
@app.route("/api/paraphrase", methods=['POST'])
def paraphrase():
    data = request.get_json()

    inputText = data.get("text")
    
    professionalPrompt = f''' 
        Rewrite the following text in a professional tone. Just respond with the professional version don't include any 
        other explanation or preamble text. Remove all quotation marks from your response:

        '{inputText}'
    '''
    professionalResponse =  ollama.generate(model="llama3.2", prompt=professionalPrompt)


    politePrompt = f''' 
        Rewrite the following text in a polite tone. Just respond with the polite version don't include any 
        other explanation or preamble text. Remove all quotation marks from your response:

        '{inputText}'
    '''
    politeResponse =  ollama.generate(model="llama3.2", prompt=politePrompt)


    casualPrompt = f''' 
        Rewrite the following text in a casual tone. Just respond with the casual version don't include any 
        other explanation or preamble text. Remove all quotation marks from your response:

        '{inputText}'
    '''
    casualResponse =  ollama.generate(model="llama3.2", prompt=casualPrompt)


    socialMediaPrompt = f''' 
        Rewrite the following text in a social media tone. That is, in a tone suitable for social media posts and ultra 
        casual conversations. Remember, text on social media tends to use lots of emojis and slang. Just respond with 
        the social media version don't include any other explanation or preamble text. Remove all quotation marks from 
        your response:

        '{inputText}'
    '''
    socialMediaResponse =  ollama.generate(model="llama3.2", prompt=socialMediaPrompt)
    

    return jsonify({"professional": professionalResponse['response'],
                    "casual": casualResponse['response'],
                    "polite": politeResponse['response'],
                    "social-media": socialMediaResponse['response']
                    }), 200


# stream rephrased content 
@app.route("/api/paraphrase_stream", methods=['POST'])
def paraphrase_stream():
    data = request.get_json()
    input_text = data.get("text", "")
    style = data.get("style", "professional")
    useChatGPT = data.get("useChatGPT", False)

    prompt = None
    if style == "professional": 
        prompt = f''' 
            Rewrite the following text in a professional tone. Just respond with the professional version don't include any 
            other explanation or preamble text. Remove all quotation marks from your response:

            '{input_text}'
        '''
    elif style == "polite": 
        prompt = f''' 
            Rewrite the following text in a polite tone. Just respond with the polite version don't include any 
            other explanation or preamble text. Remove all quotation marks from your response:

            '{input_text}'
        '''
    elif style == "casual":
        prompt = f''' 
            Rewrite the following text in a casual tone. Just respond with the casual version don't include any 
            other explanation or preamble text. Remove all quotation marks from your response:

            '{input_text}'
        '''
    elif style == "socialMedia": 
        prompt = f''' 
            Rewrite the following text in a social media tone. That is, in a tone suitable for social media posts and ultra 
            casual conversations. Remember, text on social media tends to use lots of emojis and slang. Just respond with 
            the social media version don't include any other explanation or preamble text. Remove all quotation marks from 
            your response:

            '{input_text}'
        '''

    def generate_tokens():
        
        if useChatGPT:
            load_dotenv()
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment!")
            openai_client = OpenAI(api_key=api_key)
            
            # Stream from OpenAI ChatGPT
            stream = openai_client.chat.completions.create(
                model="gpt-5-nano",  # or gpt-4o, gpt-3.5-turbo, etc.
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    yield delta.content

        else:
            # Stream from Ollama
            for token in ollama.generate(model="llama3.2", stream=True, prompt=prompt):
                yield token.response

    return Response(generate_tokens(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)