pipeline {
    agent {
        kubernetes {
            // Define your Kubernetes pod template
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: python
                image: jenkins/inbound-agent-python:latest
                command:
                - 'sleep'
                args:
                - '30d'
            """
        }
    }

    stages {
        stage('Get a Python Project') {
            steps {
                container('python') {
                    script {
                        // Checkout code from the repository
                        sh 'pwd'
                        sh 'ls -la'
                        sh 'git clone https://github.com/gohmunyau/python.git'
                        sh 'ls -la python'
                    }
                }
            }
        }

        stage('Installing Packages') {
            steps {
                container('python') {
                    script {
                        // Install required packages
                        sh 'apt update -y'
                        sh 'apt install pip -y'
                        sh 'apt install python3 -y'
                        sh 'apt install python3-requests -y'
                        sh 'apt install python3-psutil -y'
                        sh 'apt install pylint -y'
                    }
                }
            }
        }

        stage('Static Code Check') {
            steps {
                container('python') {
                    script {
                        // Run pylint for static code analysis
                        sh 'pylint python/Pythonfile.py'
                    }
                }
            }
        }

        stage('Unit Test Check') {
            steps {
                container('python') {
                    script {
                        // Run unit tests
                        sh 'python3 -m unittest python/Pythonfile.py'
                    }
                }
            }
        }
    }
}

