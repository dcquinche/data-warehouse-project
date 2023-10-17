# data-warehouse-project
This is the final project of the Cloud Data Warehouses program. The project is based on a music streaming startup, Sparkify, that wants to move their user base and song database data onto the cloud, and wants us to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team.

We are going to work with three datasets that reside in S3:

- Song Dataset: which is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song.

- Log Dataset: which consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.

- Log Json: which contains the meta information that is required by AWS to correctly load from the log data.

Our purpose is to create the following five tables:

Fact Table
- songplays: records in event data associated with song plays.

Dimension Tables
- users: users in the app.
- songs: songs in music database.
- artists: artists in music database.
- time: timestamps of records in songplays broken down into specific units.

## Dependencies
- AWS
- SQL
- Python
- configparser (python package)
- psycopg2 (python package)

## Instructions
 1. [Content](#content)
 2. [Steps](#steps)

### Content
In this project you can find:

- The create_tables.py file: which contains the conection to the cluster and the functions to drop and create the fact and dimensional tables.

- The dwh.cfg file: which contains the variables needed to create the tables in the cluster.

- etl.py file: which contains the conection to the cluster and the functions to load data from S3 into staging tables.

- sql_queries.py file: which contains the queries to drop, create, copy and insert the tables.

### Steps
1. Create sql queries.

- Drop tables.
- Create tables.
- Copy dataset to the staging tables.
- Insert data from the staging tables to the final tables.

2. Create a role with redshift:

- Go to the IAM service of the AWS portal.
- Press the create role button.
- Attach the AmazonS3ReadOnlyAccess policy.
- Once is done, copy and paste the ARN string in the dwh.cfg file.

3. Create a security group:

- Go to the EC2 service of the AWS portal.
- Press the create security group button.
- Select the default vpn.
- Add inbound rule (with TCP protocol, port 5439 and source 0.0.0.0/0).
- Add outbound rule ((with source 0.0.0.0/0)).

4. Create a user:

- Go to the IAM service of the AWS portal.
- Press the create user button.
- Go to its security credentials.
- Create the access keys (access key and secret access key).
- Once is done, copy and paste the access keys in the dwh.cfg file.

5. Create a subnet group:

- Go to the Redshift Configurations service of the AWS portal.
- Press the create subnet group button.
- Select the default vpn.

6. Create a cluster:

- Go to the Redshift Clusters service of the AWS portal.
- Press the create cluster button.
- Give it an identifier name.
- Choose the number of nodes and its configuration (in my case I used 4 nodes with dc2.large configuration).
- Select the IAM role created on the second step.
- Define a name, port, username and password to the database in the database confgurations section.
- Select a default vpc, the security group created on the third step and the cluster subnet group from the step 5 in the network and security section.
- Once is done, copy and paste the variables needed from the cluster in the dwh.cfg file.

7. Run the following command to drop and create the tables.

  ```
  python create_tables.py
  ```

8. Run the following command to implement the ETL pipeline.

  ```
  python etl.py
  ```

9. Be sure to delete the cluster to avoid generating more expenses.

