# AWS Lambda RDS auto incremento de armazenamento
Script em Python para AWS Lambda. Realiza o auto incremento do armazenamento de uma instancia RDS que esteja alarmada no CloudWatch 
RDS Low-Free-Storage-Space.

## Configuração
* Criar um alarme "Free Storage Space" no CloudWatch com prefixo "awsrds"
* Criar função no Lambda com aws-lambda-rds-inc-storage.py
* Criar Role no IAM
* Criar regra de evento CRON no CloudWatch com a chamada da função Lambda
