# Lambda Provisioned Concurrency Settings Sample for Serverless Framework

## Description

This is the sample codes settings Lambda Provisioned Concurrency with Serverless Framework.

You can build the application that you can ...

- set Provisioned Concurrency for Lambda using Serverless Framework

## Requirements

- node.js
- AWS CLI
- python 3.8
- Serverless Framework 1.6 >=

## Building

This is the step of building the app at your local.

### set up AWS account

- sign up AWS
- create AWS IAM user for building app and get access key and secret access key
  - Administration role is required becourse of CloudFormation

### set environment vars

- set below vars to environment vars
  - AWS access key
  - AWS secret access key
  - AWS default region

### set configurations

- sls_configuration/config/common.yml
  - edit and set below vars
    - ACCOUNT_ID : AWS Account ID

### install required softwares and libs

- install required softwares
  - serverless framework
    ```
    npm install -g serverless
    ```
  - aws cli
    - ref: `https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-windows.html`
- install plugins of servereless framework
  - node modules
    ```
    npm install serverless-prune-plugin
    ```
  - ref: `https://www.npmjs.com/package/serverless-prune-plugin`

### build app at local and deploy to AWS

- deploy serverless app
  ```
  sls deploy
  ```

## Reference
- Serverless Framework : https://serverless.com/
- serverless-prune-plugin : https://www.npmjs.com/package/serverless-prune-plugin
- AWS : https://aws.amazon.com/
- thilog : https://thilog.com/aws-lambda-provisioned-concurrency/
