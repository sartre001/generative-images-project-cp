from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set the API key directly
openai.api_key = 'i have an api key with dalle for chatgpt 4... i rly cant submit this with it for obvious reasons...'

def generate_character(description, style, color_scheme, background):
    full_prompt = f"{description}, style: {style}, color scheme: {color_scheme}, background: {background}"

    response = openai.images.generate(
        model="dall-e-3",
        prompt=full_prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    # Extracting the image URL from the response
    image_url = response.data[0].url
    return image_url

@app.route('/', methods=['GET'])
def index():
    return render_template('generator.html')

@app.route('/generate', methods=['POST'])
def generate():
    description = request.form['description']
    style = request.form['style']
    color_scheme = request.form['color_scheme']
    background = request.form['background']

    image_url = generate_character(description, style, color_scheme, background)
    return render_template('result.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

    
