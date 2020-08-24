# DoD Certificate Information

These Certificates were obtained on **24 Aug 2020** from [Cyber.mil](https://public.cyber.mil/pki-pke/pkipke-document-library/?_dl_facet_pkipke_type=popular-dod-certs). To gain access to these downloads, you do not need a CAC.

## Update DoD CA Certificates

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