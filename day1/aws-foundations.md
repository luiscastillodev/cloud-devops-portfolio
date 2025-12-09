# Day 1 — AWS Foundations & Console Exploration

## Topics Covered
- AWS Global Infrastructure overview
- Benefits of cloud computing (scalability, elasticity, high availability)
- Shared Responsibility Model
- Account setup and security fundamentals (MFA, billing alerts)

## AWS Console Exploration
Visited key AWS services to become familiar with layout and navigation:

### S3 Dashboard
- Observed S3’s global bucket namespace
- No buckets created yet (intended)
- Noted bucket creation workflow and settings

### EC2 Dashboard
- Viewed:
  - Instances (empty)
  - Security Groups
  - Key Pairs
  - Elastic IPs
  - Volumes
- Learned where compute resources will live during future labs

### VPC Dashboard
- Identified AWS-created default VPC
- Reviewed structure:
  - Subnets
  - Route Tables
  - Internet Gateway
  - Security vs network layers
- Noted the purpose of Local Zones, Wavelength Zones, and AZ mappings

## Billing & Account Hardening
- Enabled MFA on root account
- Set up AWS free tier alerts
- Set a zero-cost budget to prevent unexpected charges

## Notes Learned
- AWS separates *global* and *regional* services; EC2 and VPC are regional.
- Default VPC is provided for quick-start development, but production workloads use custom VPCs.
- IAM is separate from AWS sign-in accounts; Builder ID ≠ IAM user.
- Free Tier credits differ from free tier limits; credits apply automatically when available.

## Takeaways
- Feel comfortable navigating the AWS Console.
- Understand how regions/AZs factor into reliability and latency.
- Security hardening is the first task in any new AWS environment.
