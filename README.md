# Sentiment-Analysis App Built Using Hugging Face 🤗 Inference API and Streamlit⚡️

## Description
I have developed a straightforward sentiment analysis app that leverages the Hugging Face Inference API, made available through the Gradio client on Hugging Face Spaces. The code for the API is hosted on Hugging Face Spaces, providing an API endpoint for sentiment analysis. The front end of this app is built using the Streamlit library.

- To explore the backend code, please visit [this link](https://huggingface.co/spaces/internettrashh/sentiment_analysis/tree/main).
- If you wish to run the app on your local machine, start by installing the dependencies listed in the `requirements.txt` file and execute [app.py](https://github.com/internettrashh/sentiment-analysis/blob/main/app.py).
- An example of how to utilize my API endpoint in your projects can be found in [example.py](https://github.com/internettrashh/sentiment-analysis/blob/main/example.py).

## Backstory
The inspiration for this project came from a question: "How can I run, train, and host AI and machine learning models without access to a powerful GPU?" Google Colab had restrictions on running certain AI models, such as Stable Diffusion, on their GPUs. During my research, I stumbled upon Hugging Face Spaces and their Transformers and Diffusers libraries, which offer a way to use AI models without diving into the complexities of model training and deployment. This aligned perfectly with my needs.

I started my journey with a brief 15-minute crash course on Hugging Face libraries, which you can watch [here](https://www.youtube.com/watch?v=QEaBAZQCtwE&t=53s). I then set out to create a simple [sentiment analysis app](https://huggingface.co/spaces/internettrashh/sentiment_analysis).

As I progressed, a new challenge emerged: "How do I incorporate these models into my own applications?" I serendipitously discovered a solution when I came across this [image](https://github.com/internettrashh/sentiment-analysis/blob/6702de87df1aa3d383ac36d66275b43d7c33a04c/screenshots/imageedit_2_9716364892.png) and [screenshot](https://github.com/internettrashh/sentiment-analysis/blob/6702de87df1aa3d383ac36d66275b43d7c33a04c/screenshots/Screenshot%202023-10-29%20at%204.28.44%20PM.png) that provided example code for using the API. This confirmed that I could reliably utilize the API endpoint in my own applications.

In addition, I watched several code challenge videos by [Nicholas Renotte](https://www.youtube.com/watch?v=Ebb4gUI2IpQ) where I was introduced to Streamlit, a Python frontend framework. Streamlit simplifies the creation and hosting of user interfaces for machine learning and AI applications. I decided to use the Python template for the API in conjunction with the Streamlit library to build this app. The app features a textarea for user input, which is then processed by the API model based on the provided example. I also implemented a function to extract and display only the label and score from the output string. In the end, I hosted this project on Streamlit itself, taking advantage of its free hosting service.

## Future Plans
Looking ahead, I intend to apply the knowledge gained from this project to create my image generation app. This app will utilize my own fine-tuned Stable Diffusion model to generate pictures with specific themes, depending on the dataset of images used. Furthermore, I plan to employ another AI model to classify these generated images because, well, I'm a bit lazy! 😂 I'm also excited to explore technologies such as ControlNet and others to achieve even better results.

This wraps up my README.



