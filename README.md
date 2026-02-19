# 🌐 AWS-Cost-Optimization-Dashboard

An Intelligent Multi-Region FinOps Automation System
 Detect • Analyze • Optimize • Visualize AWS Infrastructure Costs in Real-Time

-------------------------------------------------------------

## 📌 Project Description

AWS-Cost-Optimization-Dashboard is a cloud-native FinOps solution designed to automatically identify idle resources, oversized infrastructure, and potential savings across multiple AWS regions.

It integrates Cost Explorer, CloudWatch, Lambda automation, S3 reporting, SNS alerting, and Grafana visualization into a single, containerized analytics platform.

This project demonstrates real-world Cloud + DevOps + FinOps engineering, not just monitoring — but **actionable cost intelligence**.

---------------------------------------------------------------------

## 🎯 Problem It Solves

In multi-region cloud environments:

* Stopped EC2 instances still incur EBS storage costs
* Oversized compute leads to wasted monthly spend
* No centralized visibility across regions
* Manual cost audits are slow and reactive
* Organizations lack automated optimization insights

This system automates cloud cost governance.

------------------------------------------------------------------

## 🚀 Key Features

✅ Multi-Region Analysis (Mumbai, Frankfurt, São Paulo)
✅ Idle EC2 Detection using CloudWatch Metrics
✅ Rightsizing Recommendations based on utilization
✅ Estimated Monthly Savings Calculation
✅ Automated Report Storage in Amazon S3
✅ AWS Lambda Trigger for Scheduled Cost Analysis
✅ SNS Email Alerts for Optimization Opportunities
✅ Interactive Grafana Dashboard for Visualization
✅ Fully Dockerized Deployment (One Command Setup)
✅ Modular Architecture — Easily Extendable to RDS, EKS, etc.

---------------------------------------------------------------------------

## 🏗️ Architecture Overview

                ┌────────────────────────────┐
                │   AWS Multi-Region Setup   │
                │ ap-south-1 | eu-central-1 | sa-east-1
                └──────────────┬─────────────┘
                               │
                      CloudWatch + Cost Explorer
                               │
                               ▼
                  FastAPI Cost Optimization Engine
                               │
        ┌──────────────┬──────────────┬──────────────┐
        │              │              │
 Idle Detection   Rightsizing     Savings Estimator
        │              │              │
        └──────────────┴──────────────┘
                               │
                      Generated Optimization Report
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
          Stored in Amazon S3        SNS Notification Sent
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                      AWS Lambda Trigger
               (Scheduled FinOps Automation Layer)
                               ▼
                        Grafana Dashboard
                    Real-Time Cost Visualization


--------------------------------------------------------------------

## ☁️ AWS Services Used

| Service           | Purpose                                     |
| ----------------- | ------------------------------------------- |
| Amazon EC2        | Workload Infrastructure Being Analyzed      |
| AWS CloudWatch    | CPU Utilization Metrics                     |
| AWS Cost Explorer | Cost Data Extraction                        |
| AWS Lambda        | Scheduled Trigger for Optimization Workflow |
| Amazon S3         | Centralized Report Storage                  |
| Amazon SNS        | Email Alert Notifications                   |
| IAM               | Secure Cross-Service Access                 |
| Grafana           | Visualization Layer                         |
| Docker            | Application Containerization                |

-------------------------------------------------------------------------------

## 🌍 Supported Regions

Configured for real multi-region visibility:

ap-south-1    → Mumbai (Primary Control Region)
eu-central-1  → Frankfurt
sa-east-1     → São Paulo


These are dynamically controlled using:

TARGET_REGIONS=ap-south-1,eu-central-1,sa-east-1

-----------------------------------------------------------------

## 📂 Project Structure
AWS-Cost-Optimization-Dashboard/
│
├── api_layer/                  # FastAPI application layer
├── optimization_engine/        # Idle, Rightsizing, Savings logic
├── data_processing/            # Dataset preparation pipeline
├── data_source/                # AWS service integrations (EC2, Cost Explorer)
├── alerts/                     # SNS notification logic
├── dashboard/
│   ├── grafana/                # Grafana dashboards
│   └── powerbi/                # Optional BI dashboard
├── docs/                       # Final report & documentation
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md


-----------------------------------------------------------

## ⚙️ Environment Configuration

Create a `.env` file:

AWS_REGION=ap-south-1

TARGET_REGIONS=ap-south-1,eu-central-1,sa-east-1

S3_BUCKET_NAME=your-s3-bucket-name

SNS_TOPIC_ARN=arn:aws:sns:<region>:<your-account-id>:cost-optimization-alerts



AWS credentials are securely mounted inside Docker:

~/.aws → /root/.aws (read-only)


--------------------------------------------------------------------

## 🐳 Run Locally (Reproducible Deployment)

### Step 1 — Build & Start Services

docker compose up -d --build

### Step 2 — Access Services

| Service      | URL                        |
| ------------ | -------------------------- |
| FastAPI Docs | http://localhost:8000/docs |
| Grafana      | http://localhost:3000      |

Grafana Login:

Username: admin
Password: admin


-------------------------------------------------------------------

## 📊 API Endpoints

| Endpoint        | Function                        |
| --------------- | ------------------------------- |
| /idle-resources | Detect unused infrastructure    |
| /rightsizing    | Suggest optimal instance sizing |
| /savings        | Estimate cost savings           |
| /full-report    | Combined FinOps analysis        |

-------------------------------------------------------------------

## 🔔 Automation via AWS Lambda

AWS Lambda is configured to:

* Periodically trigger cost analysis workflow
* Generate updated optimization reports
* Store results in S3
* Notify stakeholders via SNS

This enables serverless FinOps automation without manual execution.

----------------------------------------------------------------------

## 📈 Grafana Dashboard Insights

The dashboard visualizes:

* Idle Instance Recommendations
* Rightsizing Opportunities
* Estimated Monthly Savings
* Cross-Region Cost Impact

-----------------------------------------------------------------------

## 🧪 Example Use Case (Experiment)

1️⃣ Launch EC2 instance in Frankfurt
2️⃣ Run workload for 10 minutes
3️⃣ Stop instance
4️⃣ Lambda triggers analysis
5️⃣ Dashboard shows Terminate Recommendation + Savings

------------------------------------------------------------------------

## 💡 Why This Project Is Valuable

This project demonstrates:

✔ Cloud Cost Governance (FinOps)
✔ Multi-Region Observability
✔ Serverless Automation (Lambda)
✔ DevOps Containerization
✔ Data-Driven Decision Systems
✔ Production-Style Cloud Architecture

-----------------------------------------------------------------------

## 🔮 Future Enhancements

* Add RDS & EBS optimization
* Predictive ML-based savings forecasting
* Auto-remediation workflows
* Kubernetes (EKS) deployment
* Enterprise FinOps integration

-------------------------------------------------------------------------

## 👨‍💻 Author

Aditya Banerjee
B.Tech CSE — Cloud & DevOps Engineer
Focused on AWS • DevOps •FinOps • Intelligent Automation

---------------------------------------------------------------------------

## 📜 License

MIT License

----------------------------------------------------------------------------

⭐ *This project reflects real-world cloud cost optimization practices used in modern FinOps environments.*
