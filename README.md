# SafeJourney-AI
SafeJourney-AI is an advanced driver drowsiness detection and road safety enhancement system. Powered by machine learning and deep learning, it analyzes in-car camera feeds in real-time to ensure driver alertness and enhance road safety. 

# Video
[![Now in Android: 55]          // Title
(https://i.ytimg.com/vi/Hc79sDi3f0U/maxresdefault.jpg)] // Thumbnail
(https://youtu.be/rqU9VOm5JgM "SafeJourney-AI")    // Video Link

[Youtube](https://youtu.be/rqU9VOm5JgM)
[Onedrive](https://1drv.ms/v/s!Ag-zNH1pNyxzhC9r2IZ7_wvzx9SP?e=b5pkgv)

# Presentation
[Onedrive](https://1drv.ms/p/s!Ag-zNH1pNyxzhDDy4FHPTnzSG2Tc?e=tH0tq5)
[Google Drive](https://docs.google.com/presentation/d/10vyVEpRxzrKNkHlp8sxCEZ8x6sNLERK6/edit?usp=sharing&ouid=113870251689131757855&rtpof=true&sd=true)

# Install requirements.txt
`pip install requirements.txt`

# Required Python Version
`python>=3.11, <3.12`

# Additional requirements
This Project depends on dlib which can be downloaded and installed seperately.
[Download dlib](https://raw.githubusercontent.com/Murtaza-Saeed/dlib/master/dlib-19.24.1-cp311-cp311-win_amd64.whl)
Install the downloaded file using : `pip install dlib-19.24.1-cp311-cp311-win_amd64.whl`
[ Note run the pip command on the folder where the file got downloaded ] 

# Running the Model
run the model by running `Graph.py` which is located inside the *server/*dir. [ Relative path : `server/Graph.py`]

# Seeing the Results
After Running *Graph.py*
Navigate to `http://127.0.0.1:8050/` in any browser of you choice to see the live graph and the facial landmarks.

# Debugging and limitations 
If found any bugs and if you face any issues while setting up the repo. Raise a issue.
This project was tested on python version *Python 3.11.6* 
Browser Used : *Firefox Version 118.0.1*
platform : *Windows 11 Version 22H2 ( OS Build 22624.1616 )*

If you experience issues related to the model's predictions, it might be due to the poor quality of the laptop camera or webcam, as they often have less than 1MP and lack low light capturing capabilities. These cameras are suitable for video conferences but may limit the model's performance in image classification tasks. Additionally, this model is specifically designed to work with cameras like [product](https://amzn.eu/d/i6vwRat), which offer better resolution (1080p) and have 5MP with dedicated night mode.
