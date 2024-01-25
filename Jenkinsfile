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
            sh 'python -v' 
            sh 'git clone https://github.com/gohmunyau/python.git' 
            sh 'ls -la jenkins_python'  
          } 
          stage('Installing Packages')  
          { 
            sh 'apt-get install python3-pip'
            sh 'apt-get install python3-requests'
            sh 'apt-get install python3-psutil'

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

