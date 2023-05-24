from setuptools import setup, find_packages

setup(
    name='voice_assistant',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'speechrecognition',
        'pyttsx3',
        'python-dotenv'
    ],
)
