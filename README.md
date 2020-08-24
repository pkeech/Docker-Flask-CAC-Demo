# Docker + Flask + CAC Demo

### Table of Contents

1. [Description](#description)
2. [Usage](#usage)
3. [SSL Certificates](#ssl-certificate)
4. [DoD Root Certificates](#dod-certificates)

## Description

> **NOTE**: This demo isn't a true PKI as this application doesn't perform revocation checks.

This application was created to demonstrate how NGINX and Flask can be configured to utilize DoD Common Access Card (CAC) authentication. NGINX will prompt the browser for a certificate which is then passed onto the application for further processing (i.e. EDIPI mapping to User Account). 

To make this application closer to production ready, certificate checks need to be performed prior to authentication. This is done via Certificate Revocation Checks and can be accomplished within NGINX with some additional configurations.

## Usage

In order to run this demo on your workstation you will need the following prerequisites:

* Administrative permissions on the Workstation to update your local hostfile.
* Docker
* OpenSSL

Once the prerequisites have been furfilled, the following steps need to be followed:

1. Determine a hostname to use for the demo (eg. `demo.domain.com`)

2. Create a local hostname record that points `127.0.0.1` to `demo.domain.com`

3. Ensure your workstation is configured to use CAC. For example, when you navigate to OWA, you get prompted for a CAC. For more help on this visit [MilitaryCac](https://militarycac.com)

4. Using the directions below, generate Self-Signed Certs for `demo.domain.com`. Be sure to complete all the steps to include modifing the `Dockerfile` and `nginx.conf`

5. Navigate your terminal to the directory containing the `docker-compose.yml` file and run `docker-compose up --build -d`

5. Navigate to `demo.domain.com`. You will be prompted for you CAC. **Note**: This does nothing with the credentials other than display the DN.

## SSL Certificate

The SSL Certificate used in this demonstration is a **Self-Signed Certificate**. This certificate can be easily replaced following using traditional certifcate request guidelines.

On a workstation with **OpenSSL** installed, use the following steps to generate new Self-Signed Certifcates.

1. Generate a CSR and Private Key

    Run the following command and complete the questions when prompted.

    ``` 
    openssl req -newkey rsa:2048 -nodes -keyout demo.domain.com.key -out demo.domain.com.csr
    ```

    This will result in two new files `demo.domain.com.key` and `demo.domain.com.csr`

2. Genearate Public Key

    ``` 
    openssl x509 -signkey domain.key -in demo.domain.com.csr -req -days 365 -out demo.domain.com.crt
    ```

    This will result in one new file `demo.domain.com.crt`

3. Convert CRT to PEM

    ```
    openssl x509 -in demo.domain.com.crt -out demo.domain.com.pem -outform PEM
    ```

    This will result in one new file `demo.domain.com.pem`

4. Copy `demo.domain.com.pem` and `demo.domain.com.key` to the SSL Directory `./Server/ssl/`.

5. Update `./Server/nginx.conf` and `./Server/Dockerfile` to point to the newly created files. Lines 14 and 15 in the Dockerfile and Lines 8, 9 and 10 in the NGINX.conf file.

## DoD Certificates

The Certificates in this repo were obtained on **24 Aug 2020** from [Cyber.mil](https://public.cyber.mil/pki-pke/pkipke-document-library/?_dl_facet_pkipke_type=popular-dod-certs). To gain access to these downloads, you do not need a CAC.

### Update DoD CA Certificates

Follow these simple steps to update the DoD CA Certificates. This requires your workstation has **OpenSSL** installed.

1. Stop the application with `docker-compose down`
2. Navigate to the above link and download the latest and greatest.
3. Extract the zip file.
4. Open up a terminal and navigate to the extracted zip file.
5. Run the following command

```
openssl pkcs7 -in Certificates_PKCS7_v5.6_DoD.pem.p7b -print_certs -out DoD_CAs.pem
```

6. Copy the generated `DoD_CAs.pem` file to the SSL directory in this demo.
7. Recreate the Demo containers with the following command

```
docker-compose build
```
