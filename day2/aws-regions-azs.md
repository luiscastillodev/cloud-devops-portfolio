# Day 2 — AWS Regions, Availability Zones, Local Zones & Linux Basics

## Topics Covered
- AWS Global Infrastructure → How AWS achieves resilience and low latency
- Region vs Availability Zone vs Local Zone
- How AZ letters are randomized per account
- Linux Foundation Introduction (LFS101x Chapters 1–2)
- Linux philosophy and getting familiar with the system startup process

## AWS Hands-On Exploration

### Regions
- Compared regions and pricing differences
- Noted that region selection impacts:
  - Service availability
  - Latency
  - Data residency
  - Cost

### Availability Zones
- Identified AZ IDs vs AZ names:
  - e.g., `us-east-1a` does *not* equal `use1-az1` for everyone
- Learned your account’s AZ-ID mapping using the EC2 placement group view

### Local Zones
- Observed 13+ Local Zones available
- All listed as “Not Opted In” (correct for new accounts)
- Understood their use cases (low-latency workloads near large metros)

## Linux Foundations Progress
### LFS101x Chapters Completed:
- **Chapter 1:** Linux Foundation overview
- **Chapter 2:** Linux philosophy and open-source concepts

### Notes Learned
- Linux is modular; everything is a file.
- System startup follows a structured boot → kernel → services → user space.
- Linux encourages pipelines, tools chaining, and text-focused workflows.

## Takeaways
- Clear understanding of how AWS infrastructure is organized.
- Recognized the purpose and hierarchy of Regions → AZs → Local Zones.
- Linux concepts established a foundation for later CLI work.
