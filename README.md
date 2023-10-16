# data-warehouse-project
This is the final project of the Cloud Data Warehouses program.

## Tools Needed
- AWS
- Python
- SQL

## Instructions
 1. [Content](#content)
 2. [Steps](#steps)

### Content
In this project you can find:
- The create_tables.py file which contains the conection to the cluster and the functions to drop and create the fact and dimensional tables.
- The dwh.cfg file which contains the variables needed to create the tables in the cluster.
- etl.py file which contains the conection to the cluster and the functions to load data from S3 into staging tables.
- sql_queries.py which contains the queries to drop, create, copy and insert the tables.

### Steps
1. You have to create the sql queries to manage the tables.
2. From the IAM service of the AWS portal, you should create a role with redshift service and attach the AmazonS3ReadOnlyAccess policy. When, this is done, you can copy and paste the ARN string in the dwh.cfg file.
3. From the EC2 service of the AWS portal, you should create a security group to authorise the redshift cluster access, you can select the default vpn and add inbound (with TCP protocol, port 5439 and source 0.0.0.0/0) and outbound ((with source 0.0.0.0/0)) rules.
4. From the IAM service of the AWS portal, you should create a user, go to its security credentials and create the access keys (access key and secret access key), and put them in the dwh.cfg file.
5. From the Redshift Configurations service of the AWS portal, you should create a subnet group with de default vpc.
6. From the Redshift Clusters service of the AWS portal, you should create a cluster, give it an identifier name, choose the number of nodes and its configuration (in my case I used 4 nodes with dc2.large configuration), select the IAM role created on the second step, in the database confgurations section define a name, port, username and password to the database, and finally, in the network and security section select a default vpc, the security group created on the third step and the cluster subnet group from the step 5.
7. Get the variables needed from the cluster created on the previous step and put them in the dwh.cfg file.
8. Run the following command to drop and create the tables.
  ```
  python create_tables.py
  ```
9. Run the following command to implement the ETL pipeline.
  ```
  python etl.py
  ```
10. Be sure to delete the cluster to avoid generating more expenses.
