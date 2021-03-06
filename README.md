<img src="https://github.com/gary1998/ibm-hackathon-2019/blob/master/source_code/icon.png" alt="Icon" height="150" width="220"></img>

# FRIEND AFFINITY FINDER v1.0 (2019) #
### By Team EDGE ###
### For IBM HackChallenge 2019 ###
<hr>

#### Steps to setup using Docker Containers: ####
<pre> docker pull gary29198/faf-frontend:latest </pre>
<pre> docker pull gary29198/faf-backend:latest </pre>
<pre> docker run -d -p 8000:8000 gary29198/faf-frontend </pre>
<pre> docker run -d -p 5000:5000 gary29198/faf-backend </pre>
<hr>

#### Steps to setup using GitHub Repository: ####

**1) Clone the repository, ofcourse:**
<pre>git clone https://github.com/gary1998/ibm-hackathon-2019.git</pre>

**2) Install all the dependencies on your system:**
<pre>cd source_code</pre>
<pre>pip install -r requirements.txt</pre>

***(In case you don't have pip installed on your system: <a href="https://github.com/gary1998/ibm-hackathon-2019#steps-to-install-pip-v1911">Install pip v19.1.1</a>)***

**3) Start the backend server by following commands:**
<pre>python source_code/backend.py</pre>

**4) Start the frontend UI on server by following command:**
***If you're using Python v2.7***
<pre>python -m SimpleHTTPServer 8000</pre>

***If you're using Python v3.7***
<pre>python -m http.server 8000</pre>
<hr>

#### Steps to use: ####

**1) Access the UI on any web-browser**

***In case, you used GitHub Repository:***
<pre>http://localhost:8000/source_code/</pre>
***In case, you used Docker Images:***
<pre>http://localhost:8000/</pre>

![Dashboard](https://github.com/gary1998/ibm-hackathon-2019/blob/master/source_code/dashboard.png)


**2) Login to UI using Twitter Developer Credentials**

![Login](https://github.com/gary1998/ibm-hackathon-2019/blob/master/source_code/login.png)


**3) Select any friend, follower, text or your own tweets to analyze**

![Analysis](https://github.com/gary1998/ibm-hackathon-2019/blob/master/source_code/ff.png)


**4) Visualize 27 different properties of every friend, follower, text, or own tweets you analyzed in Card and Progress Bar form**

![Cards](https://github.com/gary1998/ibm-hackathon-2019/blob/master/source_code/cards.png)


**5) Estimate affinity in friends, followers, text, or own tweets in 3D graph**

![3D Affinity Graph](https://github.com/gary1998/ibm-hackathon-2019/blob/master/source_code/graph.png)

<hr>

<h6>Steps to install pip v19.1.1:</h6>
<h6><pre>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py</pre></h6>
<h6><pre>python get-pip.py</pre></h6>


#### Copyright EDGE &copy; 2019 #### 
