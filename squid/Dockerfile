from debian

run apt update
run apt install -y squid3

RUN squid3 -z -F

expose 3128

CMD squid3 -NCd1
