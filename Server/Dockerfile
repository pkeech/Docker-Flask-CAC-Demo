## BASE IMAGE
FROM nginx:1.18 AS BUILDER

## IMAGE METADATA
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"

## IMAGE DEPENDENCIES
FROM Builder AS Dependencies
RUN apt-get update && apt-get upgrade -y
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /etc/ssl/certs
## TODO: Determine Best Approach To Include SSL Certificates.
COPY ./ssl/DoD_CAs.pem /etc/ssl/certs
COPY ./ssl/serverbuilder.pem /etc/ssl/certs
COPY ./ssl/serverbuilder.key /etc/ssl/certs
## TODO: Determine Best Approach To Include SSL Certificates
COPY nginx.conf /etc/nginx/conf.d/

## DEV IMAGE
FROM Dependencies AS Development

## TEST IMAGE
FROM Dependencies AS Test

## PRODUCTION IMAGE
FROM Dependencies AS Production