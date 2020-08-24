# Docker + Flask + CAC Demo

Demo Application demonstrating DoD CAC Authentication

## Usage

This application demonstrates how to protect a web application with CAC Authentication. To run the demo;

1. Create a hostname record that points `127.0.0.1` to `serverbuilder.dc3n.navy.mil`
2. Ensure **Docker** is running on your workstation.
3. Ensure your workstation is configured to use CAC. For example, when you navigate to OWA, you get prompted for a CAC.
4. Navigate your terminal to the directory containing these files and run `docker-compose up --build -d`
5. Navigate to `serverbuilder.dc3n.navy.mil`. You will be prompted for you CAC. This application does nothing with the credentials other than display the DN.

## Production Notes

This demonstration isn't a true PKI as this application doesn't perform revokation checks. To make this application closer to production ready, NGINX will need to be configured to perform those checks. However, this demonstration will not allow EXPIRED certificates to authenticate.

## SSL Certificate

The SSL Certificate used in this demonstration is a **Self-Signed Certificate**. This certificate can be easily replaced following using traditional certifcate request guidelines.

## DoD Certificates

For more information of the DoD CA Certificates click [here](server/ssl/README.md).
