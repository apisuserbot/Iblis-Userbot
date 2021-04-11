# IBLIS USERBOT
FROM koala21/kampangbot:buster

#
# IBLIS
#
RUN git clone -b Iblis-Userbot https://github.com/rimuru07/Iblis-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/rimuru07/Iblis-Userbot/Iblis-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
