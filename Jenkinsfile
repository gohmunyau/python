podTemplate(containers: [ 
  containerTemplate( 
    name: 'python',  
    image: 'jenkins/inbound-agent-python:latest',  
    command: 'sleep',  
    args: '30d') 
])  
{ 
  node(POD_LABEL)  
  { 
    stage('Get a Python Project')  
    { 
      container('python')  
      {        
          stage('Checkout Code')  
          { 
            sh 'pwd' 
            sh 'ls -la' 
            sh 'git clone https://github.com/gohmunyau/python.git' 
            sh 'ls -la python'  
          } 
          stage('Installing Packages')  
          { 
            sh 'apt update -y'
            sh 'apt install pip -y'
            sh 'apt install python3 -y'
            sh 'apt install python3-requests -y'
            sh 'apt install python3-psutil -y'
            sh 'apt install pylint -y'
            sh 'pwd'
          }
          stage('Static Code Check')  
          { 
            sh 'pwd'
            sh 'pylint python/pythonfile.py'
          } 
        
          stage('Unit Test Check')
        {
          sh 'pwd'
          sh 'python3 -m unittest python/pythontest.py'
          } 
        }
      } 
    } 
  } 

