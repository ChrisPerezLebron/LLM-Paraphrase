from flask import Flask, jsonify, render_template, request
import ollama
import re

app = Flask(__name__)
ollama.pull('llama3.2')

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/api/paraphrase", methods=['POST'])
def paraphrase():
    data = request.get_json()

    inputText = data.get("text")
    # print(type(inputText))
    # print(inputText)
    
    professionalPrompt = f''' 
        Rewrite the following text in a professional tone. Just respond with the professional version don't include any 
        other explanation or preamble text:

        '{inputText}'
    '''
    professionalResponse =  ollama.generate(model="llama3.2", prompt=professionalPrompt)


    politePrompt = f''' 
        Rewrite the following text in a polite tone. Just respond with the polite version don't include any 
        other explanation or preamble text:

        '{inputText}'
    '''
    politeResponse =  ollama.generate(model="llama3.2", prompt=politePrompt)


    casualPrompt = f''' 
        Rewrite the following text in a casual tone. Just respond with the casual version don't include any 
        other explanation or preamble text:

        '{inputText}'
    '''
    casualResponse =  ollama.generate(model="llama3.2", prompt=casualPrompt)


    socialMediaPrompt = f''' 
        Rewrite the following text in a social media tone. That is, in a tone suitable for social media posts and ultra 
        casual conversations. Remember, text on social media tends to use lots of emojis and slang. Just respond with 
        the social media version don't include any other explanation or preamble text:

        '{inputText}'
    '''
    socialMediaResponse =  ollama.generate(model="llama3.2", prompt=socialMediaPrompt)
    

    return jsonify({"professional": professionalResponse['response'],
                    "casual": casualResponse['response'],
                    "polite": politeResponse['response'],
                    "social-media": socialMediaResponse['response']
                    }), 200

