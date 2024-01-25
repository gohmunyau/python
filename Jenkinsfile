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
            sh 'apt update'
            sh 'apt install pip -y'
            sh 'apt install python3 -y'
            sh 'apt install python3-requests -y'
            sh 'apt install python3-psutil -y'

          } 
          stage('Static Code Check')  
          { 
            sh 'python3 PythonFile.py' 
 
          } 
          stage('Unit Test Check')  
          { 
            sh 'python3 -m unittest PythonFile.py'
          } 
        }
      } 
    } 
  } 

