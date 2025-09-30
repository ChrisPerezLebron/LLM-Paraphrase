from flask import Flask, jsonify, render_template, request, Response
import json
import ollama

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


@app.route("/api/paraphrase_stream", methods=['POST'])
def paraphrase_stream():
    data = request.get_json()
    input_text = data.get("text", "")
    style = data.get("style", "professional")

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
        # Generate tokens from Ollama (streaming)
        for token in ollama.generate(model="llama3.2", stream=True, prompt=prompt):
            # Send each token as JSON lines
            token_text = token.response
            yield token_text

    return Response(generate_tokens(), mimetype="text/plain")