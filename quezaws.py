def ask_question(question, options, correct_index):
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    try:
        answer = int(input("Your answer (1-4): "))
        if answer == correct_index + 1:
            print("✅ Correct!\n")
            return 1
        else:
            print(f"❌ Incorrect. Correct answer: {options[correct_index]}\n")
            return 0
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.\n")
        return 0


def run_quiz():
    print("🧠 Welcome to the AWS Quiz!\n")
    score = 0

    questions = [
        {
            "question": "What does AWS stand for?",
            "options": ["Amazon Web Server", "Amazon Web Services", "Advanced Web Services",
                        "Application Web Services"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service is used for computing?",
            "options": ["S3", "RDS", "EC2", "Lambda"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service is used for storing objects (files)?",
            "options": ["EC2", "S3", "RDS", "CloudWatch"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service is used for monitoring?",
            "options": ["IAM", "CloudTrail", "CloudWatch", "SNS"],
            "answer_index": 2
        },
        {
            "question": "What is IAM in AWS?",
            "options": ["Identity and Access Management", "Internet Access Module", "Instance Access Monitor",
                        "Integrated Application Management"],
            "answer_index": 0
        },
        {
            "question": "What is Amazon S3 used for?",
            "options": ["Compute", "Object storage", "Database", "Monitoring"],
            "answer_index": 1
        },
        {
            "question": "What is the use of Amazon EC2?",
            "options": ["Storage", "Virtual Servers", "Monitoring", "Messaging"],
            "answer_index": 1
        },
        {
            "question": "Which service is best for a SQL database?",
            "options": ["S3", "Lambda", "RDS", "EC2"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service is serverless?",
            "options": ["EC2", "RDS", "Lambda", "ECS"],
            "answer_index": 2
        },
        {
            "question": "What is the full form of VPC?",
            "options": ["Virtual Private Cloud", "Virtual Public Cloud", "Variable Private Cloud",
                        "Verified Private Channel"],
            "answer_index": 0
        },
        {
            "question": "Which AWS service manages user authentication?",
            "options": ["IAM", "S3", "CloudWatch", "Route 53"],
            "answer_index": 0
        },
        {
            "question": "What is the use of Route 53?",
            "options": ["Storage", "Domain registration and DNS", "Monitoring", "Security"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service provides a Content Delivery Network (CDN)?",
            "options": ["S3", "EC2", "CloudFront", "RDS"],
            "answer_index": 2
        },
        {
            "question": "Which service helps in automation and infrastructure as code?",
            "options": ["CloudTrail", "CloudFormation", "CloudWatch", "IAM"],
            "answer_index": 1
        },
        {
            "question": "AWS Lambda is best used for?",
            "options": ["Long-running applications", "Static websites", "Short-lived functions", "Virtual Machines"],
            "answer_index": 2
        },
        {
            "question": "Which database service supports NoSQL?",
            "options": ["RDS", "Redshift", "DynamoDB", "Aurora"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service is used to manage containers?",
            "options": ["ECS", "S3", "Lambda", "CloudFront"],
            "answer_index": 0
        },
        {
            "question": "What is the main benefit of Auto Scaling?",
            "options": ["Faster network", "Automatic billing", "Handle traffic automatically", "More storage"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service allows you to track API calls?",
            "options": ["CloudTrail", "CloudWatch", "SNS", "ECS"],
            "answer_index": 0
        },
        {
            "question": "Which AWS service is used to send notifications?",
            "options": ["SNS", "SQS", "RDS", "EC2"],
            "answer_index": 0
        },
        {
            "question": "What does EBS stand for?",
            "options": ["Elastic Block Store", "Elastic Binary System", "Extended Backup System",
                        "Elastic Base Service"],
            "answer_index": 0
        },
        {
            "question": "Which AWS service supports messaging queues?",
            "options": ["S3", "SNS", "SQS", "SES"],
            "answer_index": 2
        },
        {
            "question": "What is Amazon Aurora?",
            "options": ["Monitoring tool", "NoSQL database", "Relational DB engine", "Object storage"],
            "answer_index": 2
        },
        {
            "question": "What is a Region in AWS?",
            "options": ["Group of users", "Data center location", "Access policy", "Pricing plan"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service helps manage software packages?",
            "options": ["CodeDeploy", "CodeBuild", "CodeArtifact", "CodePipeline"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service is a CI/CD pipeline?",
            "options": ["CodePipeline", "CodeArtifact", "CloudTrail", "Route53"],
            "answer_index": 0
        },
        {
            "question": "How do you protect data at rest in AWS?",
            "options": ["Backups", "Encryption", "Multi-region", "Auto scaling"],
            "answer_index": 1
        },
        {
            "question": "Which service is used for secure file transfers?",
            "options": ["S3", "Transfer Family", "EC2", "EBS"],
            "answer_index": 1
        },
        {
            "question": "Which tool helps estimate AWS pricing?",
            "options": ["Billing Console", "Cost Explorer", "AWS Calculator", "AWS Budget"],
            "answer_index": 2
        },
        {
            "question": "What does AWS WAF protect against?",
            "options": ["Viruses", "DDOS", "SQL injection & threats", "Latency"],
            "answer_index": 2
        },
        {
            "question": "Which tool visualizes logs and metrics?",
            "options": ["CloudTrail", "CloudFront", "CloudWatch", "GuardDuty"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service scans containers for security?",
            "options": ["Inspector", "Shield", "Macie", "S3"],
            "answer_index": 0
        },
        {
            "question": "AWS budgets help you?",
            "options": ["Track network", "Send alerts on cost usage", "Monitor latency", "Control EC2"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service helps migrate databases?",
            "options": ["DMS", "SMS", "EC2", "RDS"],
            "answer_index": 0
        },
        {
            "question": "Which AWS service helps host static websites?",
            "options": ["Lambda", "S3", "EC2", "Redshift"],
            "answer_index": 1
        },
        {
            "question": "What is the use of Elastic Load Balancer?",
            "options": ["Store files", "Route traffic across instances", "Monitor instances", "Encrypt data"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service is data warehouse?",
            "options": ["Redshift", "Aurora", "S3", "Lambda"],
            "answer_index": 0
        },
        {
            "question": "AWS KMS is used for?",
            "options": ["Machine learning", "Key management and encryption", "Migration", "Networking"],
            "answer_index": 1
        },
        {
            "question": "Which service manages hybrid cloud architecture?",
            "options": ["Direct Connect", "VPC", "IAM", "ECS"],
            "answer_index": 0
        },
        {
            "question": "Which is not a valid EC2 pricing model?",
            "options": ["On-demand", "Reserved", "Spot", "Floating"],
            "answer_index": 3
        },
        {
            "question": "What does Cloud9 provide?",
            "options": ["IDE in the browser", "Container hosting", "Security scanner", "Lambda editor"],
            "answer_index": 0
        },
        {
            "question": "Which AWS service lets you use SQL for analytics?",
            "options": ["Athena", "EC2", "S3", "IAM"],
            "answer_index": 0
        },
        {
            "question": "Which service uses machine learning for predictions?",
            "options": ["SageMaker", "RDS", "Redshift", "IAM"],
            "answer_index": 0
        },
        {
            "question": "Which service offers managed Kubernetes?",
            "options": ["ECS", "EKS", "Lambda", "CloudFormation"],
            "answer_index": 1
        },
        {
            "question": "Which AWS service is a NoSQL caching solution?",
            "options": ["RDS", "Elasticache", "DynamoDB", "S3"],
            "answer_index": 1
        },
        {
            "question": "What does AWS Shield protect against?",
            "options": ["Cost issues", "Phishing", "DDoS attacks", "SQL injection"],
            "answer_index": 2
        },
        {
            "question": "Which is the AWS resource policy?",
            "options": ["IAM Role", "VPC", "S3 Bucket Policy", "Lambda Function"],
            "answer_index": 2
        },
        {
            "question": "Which AWS service handles secrets management?",
            "options": ["Secrets Manager", "IAM", "S3", "CloudTrail"],
            "answer_index": 0
        }
    ]

    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer_index"])

    print(f"\n🎯 Your final score: {score}/{len(questions)}")
    print("👍 Thanks for playing!\n")


if __name__ == "__main__":
    run_quiz()
